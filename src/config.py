import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

DOCUMENT_PATH = "data/documents.txt"
MAX_TOKENS = 512
TEMPERATURE = 0.7
TOP_P = 0.9
MODEL_NAME = "google/gemini"

if not API_KEY:
    raise ValueError("未找到 API_KEY，请检查根目录下的 .env 文件！")