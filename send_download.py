import os
import requests

URL = "http://localhost:8000/download/"

data = {
    "url": os.environ["URL"]
}

response = requests.post(URL, json=data)