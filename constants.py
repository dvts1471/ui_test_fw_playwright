import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")