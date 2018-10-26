import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

MAX_WORKERS = os.cpu_count()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")
