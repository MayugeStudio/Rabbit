"""
Json Configuration such as Json key, content, etc.
"""

# --- Standard Library ---
import json

# Tasks dict key
TASKS_KEY = "tasks"
# Initial tasks content
INITIAL_TASKS_CONTENT = json.dumps({TASKS_KEY: []})
