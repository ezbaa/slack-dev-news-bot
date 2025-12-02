import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

data = {"text": "Hello World!"}

response = requests.post(WEBHOOK_URL, json=data)  

print("Status code:", response.status_code)  
print("Response:", response.text)