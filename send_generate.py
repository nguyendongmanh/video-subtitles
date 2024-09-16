import os
import requests

URL = f"http://localhost:8000/generate/{os.environ['v']}"
response = requests.post(URL)