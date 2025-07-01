import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID")

def create_trello_card(task):
    url = "https://api.trello.com/1/cards"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "idList": TRELLO_LIST_ID,
        "name": task["task"],
        "desc": f"Due: {task.get('due')}, Priority: {task.get('priority')}"
    }
    response = requests.post(url, params=params)
    return response.status_code == 200
 
