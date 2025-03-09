import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from airosentris import Config
from airosentris.logger.Logger import Logger

# Initialize session with retries
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

logger = Logger(__name__)


def fetch_data(endpoint, timeout=10):
    """Fetch data from the given API endpoint."""
    if not Config.API_URL or not Config.API_TOKEN:
        raise ValueError("❌ API_URL or API_TOKEN is missing. Initialize Airosentris with valid config.")

    url = f"{Config.API_URL}/{endpoint}"
    headers = {'Authorization': f"Bearer {Config.API_TOKEN}"}

    logger.info(f"📡 [GET] Fetching data from {url}")

    try:
        response = session.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise exception for HTTP errors

        response_data = response.json()
        if isinstance(response_data, dict) and not response_data.get("success", False):
            error_message = response_data.get("message", "Unknown error")
            logger.error(f"❌ [GET] Fetch failed: {error_message}")
            raise Exception(error_message)

        logger.info(f"✅ [GET] Data fetched successfully ({response.status_code})")
        return response_data
    except requests.Timeout:
        logger.error(f"⏳ [GET] Timeout while fetching data from {url}")
        raise
    except requests.RequestException as e:
        logger.error(f"❌ [GET] Request failed: {e}")
        raise


def post_data(endpoint, data, files=None, timeout=10):
    """Post data to the given API endpoint."""
    if not Config.API_URL or not Config.API_TOKEN:
        raise ValueError("❌ API_URL or API_TOKEN is missing. Initialize Airosentris with valid config.")

    url = f"{Config.API_URL}/{endpoint}"
    headers = {'Authorization': f"Bearer {Config.API_TOKEN}"}

    # Calculate payload size safely
    payload_size = len(data) if isinstance(data, (str, bytes, dict)) else "Unknown"

    logger.info(f"📡 [POST] Sending data to {url} (Payload size: {payload_size})")

    try:
        response = session.post(url, headers=headers, data=data, files=files, timeout=timeout)
        response.raise_for_status()  # Raise exception for HTTP errors

        response_data = response.json()
        if not response_data.get("success", False):
            error_message = response_data.get("message", "Unknown error")
            logger.error(f"❌ [POST] Upload failed: {error_message}")
            raise Exception(error_message)

        logger.info(f"✅ [POST] Data posted successfully ({response.status_code})")
        return response_data
    except requests.Timeout:
        logger.error(f"⏳ [POST] Timeout while posting data to {url}")
        raise
    except requests.RequestException as e:
        logger.error(f"❌ [POST] Request failed: {e}")
        raise


def mock_data():
    data = {
        "success": True,
        "data": [
            {
                "comment_id": 17943412448833336,
                "comment_text": "Sebelum bikin gorong\"seharusnya teknisi lapangan itu survey jalan mana yg harus digali. .gak asal gali aja dipikir donk dikit\"pipa PDAM bocor alasan gak berguna sekali duakali oke lah sudah hampir 1th alasan kok podo ae",
                "comment_date": "2024-07-16 13:06:28",
                "username": "miftachul_retna",
                "user_id": 1679854023,
                "replies": [
                    {
                        "reply_id": 18051102328815550,
                        "reply_text": "@miftachul_retna bener kak gara2 ada gorong hanya bikin warga sak SBY resah aja,,, gorong2 gk berguna hanya bikin masalah saja 😢😢😢",
                        "reply_date": "2024-07-20 03:55:17",
                        "username": "yuliana_saskia",
                        "user_id": 5604089480
                    },
                    {
                        "reply_id": 18037749367974156,
                        "reply_text": "@yuliana_saskia selamat siang bu silahkan DM kami data pelanggan alamat lengkap utk segera kami tindaklanjuti pengaduannya -w",
                        "reply_date": "2024-07-20 07:37:14",
                        "username": "pdamsuryasembada",
                        "user_id": 2019411880
                    }
                ],
                "total_reply": 2,
                "label_sentiment": "positive"
            },
            {
                "comment_id": 17869819218117332,
                "comment_text": "Pak PDAM yg terhormat mau sampai kapan air diwilayah gembong sekalaj ini seperti ini ini air got lho pak,sudah dari 3 hari yg lalu warga gembong yg air ya keluar air got laporan tapi kok masih belum ada perbaikan,klu bayar telat saja sehari denda langsung tapi klu keluhan lemot sekali penanganannya",
                "comment_date": "2024-07-09 23:04:44",
                "username": "indicantik25",
                "user_id": 60555859626,
                "replies": [
                    {
                        "reply_id": 17939344316846030,
                        "reply_text": "@indicantik25 Selamat pagi bu Indi, mohon maaf atas ketidaknyamanannya. Baik, kami follow up ke petugas terkait. -w",
                        "reply_date": "2024-07-12 02:50:26",
                        "username": "pdamsuryasembada",
                        "user_id": 2019411880
                    }
                ],
                "total_reply": 1,
                "label_sentiment": "negative"
            }
        ],
        "message": "Successfully fetched 2 comments for post C9MKTnUvtRv"
    }

    return json.dumps(data)