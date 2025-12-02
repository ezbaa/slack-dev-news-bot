import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

def fetch_articles():
    url = "https://dev.to/api/articles?per_page=5&top=7"
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()
        results = []

        for article in articles:
            results.append({  
            "title":article["title"],
            "description":article["description"],
            "link":article["url"]
            })

        return results
    else:
        print(f"Error fetching articles: {response.status_code}")
        return []
        
articles_list = fetch_articles()

message = ":newspaper: *Today's Top 5 Dev Articles*\n\n"
for article in articles_list:
    message += f"• *{article['title']}*\n"
    message += f"   _{article['description']}_\n"
    message += f"   {article['link']}\n\n"
payload = {"text": message}
response = requests.post(WEBHOOK_URL, json=payload)        

print("Status code:", response.status_code)  
print("Response:", response.text)
