import requests
from src.const import LOG_URL

def log(tag:str, message:str):
      if LOG_URL is not None:
            requests.post(LOG_URL, json={
                  'tag':tag,
                  'message':message,
            }, timeout=1)