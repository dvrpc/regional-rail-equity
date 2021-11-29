import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DATABASE_URL = os.getenv("DATABASE_URL")
GDRIVE_PROJECT_FOLDER = Path(os.getenv("GDRIVE_PROJECT_FOLDER"))
