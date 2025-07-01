import os
import requests
from dotenv import load_dotenv

load_dotenv()
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def notify_slack(task):
    message = f"*New Task:* {task['task']}\n*Due:* {task.get('due')}\n*Priority:* {task.get('priority')}"
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return response.status_code == 200
 
