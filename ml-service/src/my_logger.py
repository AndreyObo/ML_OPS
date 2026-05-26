import requests
from src.const import LOG_URL

def log(tag:str, message:str):
      requests.post(LOG_URL, json={
            'tag':tag,
            'message':message,
        }, timeout=1)