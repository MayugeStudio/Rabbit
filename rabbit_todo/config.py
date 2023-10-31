"""
Rabbit Todo Config File
"""


# --- Standard Library ---
import json
from pathlib import Path

TASKS_KEY = "tasks"
INITIAL_TASKS_CONTENT = json.dumps({TASKS_KEY: []})

ROOT_DIR = ".rabbit"
ROOT_DIR_PATH = Path(ROOT_DIR)
TASKS_FILE_NAME = "tasks.json"
