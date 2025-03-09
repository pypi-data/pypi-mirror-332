import json
import os
import time
import signal
import sys
from threading import Thread, Event

import pika
from airosentris.agent.Agent import Agent
from airosentris.config.ConfigFetcher import get_config
from airosentris import get_agent
from airosentris.client.RabbitMQClient import RabbitMQClient
from airosentris.hardware.SystemInfo import SystemInfo
from airosentris.logger.Logger import Logger
from airosentris.message.AgentStatus import AgentStatusRequest
from airosentris.message.TrainParams import TrainParams
from airosentris.trainer.TrainerFactory import TrainerFactory


class Trainer:
    def __init__(self):
        self.threads = []
        self.agent = get_agent()
        self.agent_id = str(self.agent['id'])

        self.training_exchange = 'airosentris.train'
        self.training_queue = f'airosentris.train.queue.{self.agent_id}'
        self.agent_status_queue = f'airosentris.agent-{self.agent_id}'

        self.on_agent_status_request = self.process_agent_status_request
        self.on_training_request = self.process_training_request
        
        self.config = get_config()

        self.training_rabbitmq_client = None
        self.agent_rabbitmq_client = None
        self.training_listener_thread = None
        self.agent_listener_thread = None

        self.logger = Logger(__name__)

        # Event untuk menghentikan thread secara terkontrol
        self.stop_event = Event()

        signal.signal(signal.SIGINT, self.shutdown_handler)
        signal.signal(signal.SIGTERM, self.shutdown_handler)

    def shutdown_handler(self, signum, frame):
        """
        Handles `Ctrl+C` (SIGINT) or system termination (SIGTERM).
        """
        self.logger.info("🛑 Shutdown signal received. Stopping all listeners...")
        self.stop_event.set()

        if self.agent_rabbitmq_client:
            self.agent_rabbitmq_client.close()
        if self.training_rabbitmq_client:
            self.training_rabbitmq_client.close()


    def initialize_trainer_queue(self):
        self.training_rabbitmq_client = RabbitMQClient(self.config, heartbeat=3600, blocked_connection_timeout=600, name="training_request")
        self.training_rabbitmq_client.connect()
        self.training_rabbitmq_client.declare_exchange(self.training_exchange, exchange_type='direct')
        self.training_rabbitmq_client.declare_queue(self.training_queue)
        self.training_rabbitmq_client.bind_queue(self.training_exchange, self.training_queue, self.agent_id)

    def handle_agent_queries(self):
        if not callable(self.on_agent_status_request):
            raise ValueError("on_agent_status_request callback must be callable")
        
        while not self.stop_event.is_set(): 
            try:
                self.agent_rabbitmq_client = RabbitMQClient(config=self.config, name="agent_status_request")
                self.agent_rabbitmq_client.connect()
                self.agent_rabbitmq_client.declare_exchange('airosentris.agent', exchange_type='fanout')
                self.agent_rabbitmq_client.declare_queue(self.agent_status_queue, durable=False, auto_delete=True)
                self.agent_rabbitmq_client.bind_queue('airosentris.agent', self.agent_status_queue, '')

                def on_message(ch, method, properties, body):
                    try:
                        if self.stop_event.is_set():
                            self.logger.info("🛑 Stop event received. Stopping message consumption.")
                            ch.stop_consuming()
                            return
                        
                        message = json.loads(body)
                        message_receive = AgentStatusRequest(code=message.get("code"))
                        self.on_agent_status_request(message_receive)
                        if not ch.is_closed:
                            ch.basic_ack(delivery_tag=method.delivery_tag)
                        else:
                            self.logger.warning("Cannot ack message; channel is already closed.")
                    except Exception as e:
                        self.logger.error(f"❌ Error processing agent info message: {e}")
                        if not ch.is_closed:
                            ch.basic_ack(delivery_tag=method.delivery_tag)
                        else:
                            self.logger.warning("Cannot ack message; channel is already closed.")       
                
                self.agent_rabbitmq_client.consume_messages(self.agent_status_queue, on_message)                
            except pika.exceptions.AMQPConnectionError as e:
                self.logger.error(f"❌ Connection error: {e}. Retrying in 5s...")
                time.sleep(5)
            except pika.exceptions.StreamLostError as e:
                self.logger.error(f"❌ Stream connection lost: {e}. Reconnecting in 5 seconds...")
                time.sleep(5)
            except Exception as e:
                self.logger.error(f"❌ Unexpected error in handle_agent_queries: {e}")
                break

    def watch_training_requests(self):
        if not callable(self.on_training_request):
            raise ValueError("on_training_request callback must be callable")
        while not self.stop_event.is_set():  # Loop will break if stop_event is set
            try:
                self.initialize_trainer_queue()

                def on_message(ch, method, properties, body):
                    try:
                        if self.stop_event.is_set():
                            self.logger.info("🛑 Stop event received. Stopping message consumption.")
                            ch.stop_consuming()
                            return
                        
                        message_dict = json.loads(body)
                        train_params = TrainParams(
                            project_id=message_dict.get("project_id"),
                            run_id=message_dict.get("run_id"),
                            algorithm=message_dict.get("algorithm"),
                            scope=message_dict.get("scope"),
                            label=message_dict.get("label"),
                            dataset=message_dict.get("dataset"),
                            params=message_dict.get("params"),
                            epoch=message_dict.get("epoch")
                        )

                        # Handle tuples in train_params
                        for key, value in train_params.__dict__.items():
                            if isinstance(value, tuple):
                                setattr(train_params, key, value[0])

                        self.on_training_request(train_params)
                        if not ch.is_closed:
                            ch.basic_ack(delivery_tag=method.delivery_tag)
                        else:
                            self.logger.warning("Cannot ack message; channel is already closed.")
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Invalid JSON message: {e}")
                        if not ch.is_closed:
                            ch.basic_ack(delivery_tag=method.delivery_tag)
                        else:
                            self.logger.warning("Cannot ack message; channel is already closed.")
                    except Exception as e:
                        self.logger.error(f"Error processing training message: {e}")
                        if not ch.is_closed:
                            ch.basic_ack(delivery_tag=method.delivery_tag)
                        else:
                            self.logger.warning("Cannot ack message; channel is already closed.")

                self.training_rabbitmq_client.channel.basic_qos(prefetch_count=1)
                self.training_rabbitmq_client.consume_messages(self.training_queue, on_message)
                self.logger.info("Waiting for training requests...")
            except pika.exceptions.AMQPConnectionError as e:
                self.logger.error(f"Connection error: {e}. Reconnecting in 5 seconds...")
                time.sleep(5)
            except pika.exceptions.StreamLostError as e:
                self.logger.error(f"Stream connection lost: {e}. Reconnecting in 5 seconds...")
                time.sleep(5)
            except Exception as e:
                self.logger.error(f"Error in watch_training_requests: {e}")
                break

    def process_training_request(self, train_params: TrainParams):

        self.logger.info(
            f"\n📌 [TRAINING REQUEST] Received:\n"
            f"   ├── 🆔 Project ID   : {train_params.project_id}\n"
            f"   ├── 📌 Run ID       : {train_params.run_id}\n"
            f"   ├── 🧠 Algorithm    : {train_params.algorithm}\n"
            f"   ├── 🎯 Scope        : {train_params.scope}\n"
            f"   ├── 🔖 Labels       : {train_params.label}\n"
            f"   ├── 📂 Dataset      :\n"
            f"   │   ├── 📄 Train  : {train_params.dataset.get('train', 'N/A')}\n"
            f"   │   └── 📄 Test   : {train_params.dataset.get('test', 'N/A')}\n"
            f"   ├── ⚙️ Parameters   : {train_params.params if train_params.params else 'Default'}\n"
            f"   └── 🚀 Training started..."
        )

        try:
            trainer_class = TrainerFactory.get_trainer(train_params.algorithm)
            trainer_algorithm = trainer_class()
            trainer_algorithm.init(train_params)
            trainer_algorithm.train()
            trainer_algorithm.evaluate()
            trainer_algorithm.save_model()
            trainer_algorithm.upload_model()    
        except Exception as e:
            self.logger.error(f"Error processing training request: {e}")

    def process_agent_status_request(self, message_receive: AgentStatusRequest):
        self.logger.info(f"🔍 Processing agent status request: {message_receive}")
        try:
            system_info = SystemInfo.get_common_info()
            # Build GPU information as a properly formatted multi-line string
            gpu_info = "\n".join(
                [
                    f"      ├── 🎮 GPU-{idx} Name  : {gpu['gpu_name']}\n"
                    f"      ├── 🔢 GPU-{idx} UUID  : {gpu['gpu_uuid']}\n"
                    f"      └── 💾 GPU-{idx} Memory: {gpu['gpu_total_memory']}"
                    for idx, gpu in enumerate(system_info.get("gpu", []), start=1)
                ]
            )

            # Construct the full system info log as a single string
            system_info_log = (
                f"\n🖥️ [SYSTEM INFO] Retrieved successfully:\n"
                f"   ├── 🏎️  CPU Model    : {system_info['cpu_processor']}\n"
                f"   ├── 🏗️  Physical Cores: {system_info['cpu_physical_core']}\n"
                f"   ├── 🚀 Total Cores   : {system_info['cpu_total_core']}\n"
                f"   ├── 💻 OS Platform   : {system_info['system_platform']} {system_info['system_platform_version']}\n"
                f"   ├── 🛠️  RAM          : {system_info['system_ram']}\n"
                f"   └── 🎮 GPU(s):\n"
                f"{gpu_info}"
            )
            
            self.logger.info(system_info_log)

            agent = Agent()
            result = agent.update(system_info)
            if not result.get("success", False):
                raise Exception(f"❌ Agent update failed!")
            
            self.logger.info(f"✅ Successfully sent agent info to server")

        except Exception as e:
            self.logger.error(f"❌ Error processing agent status request: {e}")

    def start_agent_query_listener(self):
        """Start the agent query listener thread only if it's not running."""
        if self.agent_listener_thread and self.agent_listener_thread.is_alive():
            self.logger.warning("⚠️ Agent query listener is already running.")
            return
        
        self.logger.info("📩 Starting agent query listener...")

        self.agent_listener_thread = Thread(target=self.handle_agent_queries, daemon=True)
        self.threads.append(self.agent_listener_thread)
        self.agent_listener_thread.start()        

    def start_training_request_listener(self):
        """Start the training request listener thread only if it's not running."""
        if self.training_listener_thread and self.training_listener_thread.is_alive():
            self.logger.warning("⚠️ Training request listener is already running.")
            return

        self.logger.info("📩 Starting training request listener...")
        
        self.training_listener_thread = Thread(target=self.watch_training_requests, daemon=True)
        self.threads.append(self.training_listener_thread)
        self.training_listener_thread.start()

    def start(self):
        """
        Starts the trainer and listens for `Ctrl+C` to exit gracefully.
        """
        if not callable(self.on_training_request):
            raise ValueError("on_training_request callback must be set before starting the trainer")

        self.logger.info("🚀 Starting AIROSENTRIS Trainer...")

        self.start_agent_query_listener()
        self.start_training_request_listener()

        try:
            # Keep the program running until interrupted by `Ctrl + C`
            while not self.stop_event.is_set():
                time.sleep(1)  # Prevent CPU overuse, keeps checking stop_event
        except KeyboardInterrupt:
            self.logger.info("🛑 Ctrl+C detected. Shutting down gracefully...")
            self.stop_event.set()

        # Wait for all threads to finish
        for thread in self.threads:
            thread.join()

        self.logger.info("✅ Trainer stopped successfully.")

