import json
import os
import time
from threading import Thread
from airosentris.algorithm.BERT.BERTRunner import BERTRunner
from airosentris.client.APIClient import APIClient
from airosentris.logger.Logger import Logger
from airosentris.message.Comment import Comment
from airosentris.config.ConfigFetcher import get_config
from airosentris import get_agent
from airosentris.client.RabbitMQClient import RabbitMQClient
from airosentris.runner.RunnerRegistry import RunnerRegistry
from airosentris.runner.RunnerFactory import RunnerFactory
from airosentris.message.AgentStatus import AgentStatusRequest
from airosentris.hardware.SystemInfo import SystemInfo
from airosentris.agent.Agent import Agent
from minio import Minio
import tempfile
import requests
from tqdm import tqdm
import zipfile

class Runner:
    def __init__(self):        
        self.rabbitmq_client = None
        self.evaluation_queue = "airosentris.evaluate.queue"
        self.evaluation_thread = None
        self.scopes = ["complaint_category", "sentiment", "statement_type"]
        self.runners = {}
        self.runner_cache = {}
        self.api_client = APIClient()
        self.logger = Logger(__name__)

    def setup_rabbitmq_client(self):
        """Initialize RabbitMQ client."""
        config = get_config()
        self.rabbitmq_client = RabbitMQClient(config=config, name="evaluation_request")
        self.rabbitmq_client.connect()
        self.logger.info("RabbitMQ client initialized successfully.")

    def initialize_evaluation_queue(self):
        """Declare the evaluation queue."""
        if not self.rabbitmq_client:
            self.setup_rabbitmq_client()
        self.rabbitmq_client.declare_queue(self.evaluation_queue, durable=True)
        self.logger.info(f"✅ Evaluation queue initialized: {self.evaluation_queue}")

    def start_listening(self):
        """Listen to incoming messages for evaluation."""
        while True:
            try:
                self.initialize_evaluation_queue()
                self.rabbitmq_client.consume_messages(
                    self.evaluation_queue,
                    self._process_incoming_message,
                )
                self.logger.info(f"[*] Waiting for messages in {self.evaluation_queue}. To exit press CTRL+C")
            except Exception as e:
                self.logger.error(f"Error in start_listening: {e}. Reconnecting in 5 seconds...")
                time.sleep(5)

    def _process_incoming_message(self, ch, method, properties, body):
        """Process incoming RabbitMQ message."""
        try:
            message_data = json.loads(body)
            message = Comment(
                id=message_data.get("id"),
                timestamp=message_data.get("timestamp"),
                content=message_data.get("content"),
            )
            self.process_evaluation_message(message)
            # If trial comment this 
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON message: {e}")
            if not ch.is_closed:
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                self.logger.warning("Cannot ack message; channel is already closed.") 
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")
            if not ch.is_closed:
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                self.logger.warning("Cannot ack message; channel is already closed.") 

    def process_evaluation_message(self, message: Comment):
        """Spawn threads to evaluate the message across all scopes."""
        self.logger.warning(f"Processing message: {message.content}")
        threads = [
            Thread(target=self.evaluate, args=(message, scope))
            for scope in self.scopes
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def evaluate(self, message: Comment, scope_code: str):
        """Evaluate the message for a specific scope using the appropriate runner."""
        try:
            runner = self.runners.get(scope_code)
            if not runner:
                self.logger.warning(f"No runner found for scope: {scope_code}")
                return
            result = runner.evaluate(message)
            self.logger.info(f"Result for {scope_code}: {result}")
        except Exception as e:
            self.logger.error(f"Error evaluating {scope_code}: {e}")

    def get_active_model(self, scope_code: str):
        """Fetch active model details for a given scope."""
        try:
            response = self.api_client.post_data(
                endpoint="api/v1/ai-model/active/detail",
                data={"scope_code": scope_code},
            )
            if response.get('success') == True:
                return response.get("data")
            self.logger.error(f"Error retrieving active model for {scope_code}: {response.text}")
        except Exception as e:
            self.logger.error(f"Error fetching active model for {scope_code}: {e}")
        return None

    def download_model(self, run_id: str):
        """Download the model associated with a specific run_id with a progress bar."""
        try:
            download_url = f"https://apisentris.pdam-sby.go.id/api/v1/ai-model/download/{run_id}"
            data_folder = "data"
            model_path = f"artifacts/models/{run_id}/"
            download_path = os.path.join(data_folder, f"{run_id}.zip")

            # Ensure the 'data' folder exists
            os.makedirs(data_folder, exist_ok=True)

            # Check if the model directory already exists
            if os.path.exists(model_path) and os.path.isdir(model_path):
                self.logger.info(f"✅ Model for {run_id} already exists at {model_path}. Skipping download.")
                return model_path

            # Send a request to get the model file
            response = requests.get(download_url, stream=True)
            response.raise_for_status()  # Raise an error for bad status codes

            # Get total file size from headers (if available)
            total_size = int(response.headers.get("content-length", 0))
            
            # Download with progress bar
            with open(download_path, "wb") as f, tqdm(
                desc=f"Downloading {run_id}",
                total=total_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024
            ) as bar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive new chunks
                        f.write(chunk)
                        bar.update(len(chunk))  # Update progress bar

            # Ensure the model directory exists before extracting
            os.makedirs(model_path, exist_ok=True)

            # Extract the zip file
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(model_path)

            self.logger.info(f"✅ Model downloaded and extracted for {run_id} at {model_path}")
            return model_path

        except requests.RequestException as e:
            self.logger.error(f"❌ HTTP error while downloading model for {run_id}: {e}")
        except Exception as e:
            self.logger.error(f"❌ Error downloading model for {run_id}: {e}")

        return None
    def update_model_for_scope(self, scope_code: str):
        """Update the model for a given scope by fetching, downloading, and loading it."""
        active_model = self.get_active_model(scope_code)
        if not active_model:
            self.logger.warning(f"No active model found for {scope_code}")
            return 

        run_id = active_model.get("run_id")
        if run_id and (scope_code not in self.runner_cache or self.runner_cache[scope_code] != run_id):
            model_path = self.download_model(run_id)
            if model_path:
                runner_class = RunnerFactory.get_runner(active_model["algorithm_code"])
                runner_instance = runner_class()
                runner_instance.load_model(scope_code, model_path)
                self.runners[scope_code] = runner_instance
                self.runner_cache[scope_code] = run_id
        else:
            self.logger.info(f"Model for {scope_code} is already up-to-date.")

    def auto_update_models(self):
        """Periodically update models for all scopes."""
        while True:
            for scope in self.scopes:
                self.update_model_for_scope(scope)
            self.logger.info("🔄 Models updated successfully.")

    def start_auto_update(self):
        """Start a thread for automatic model updates."""
        Thread(target=self.auto_update_models).start()

    def start_message_listener(self):
        """Start a thread for evaluation listener."""
        Thread(target=self.start_listening).start()

    def start(self):
        """Start all runner processes."""
        # self.auto_update_models()
        req = AgentStatusRequest("sentiment")
        self.process_agent_status_request(req)

        for scope in self.scopes:
            self.update_model_for_scope(scope)
        
        self.logger.info("🔄 Models updated successfully.")
        self.start_listening()
        
        # self.start_auto_update()
        # self.start_message_listener()

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