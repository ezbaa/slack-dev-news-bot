import os
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def fetch_articles():
    url = "https://dev.to/api/articles?per_page=5"
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()
        results = []

        for article in articles:
            results.append(
                {
                    "title": article["title"],
                    "description": article["description"],
                    "link": article["url"],
                }
            )

        return results
    else:
        print(f"Error fetching articles: {response.status_code}")
        return []


def summarize_with_ai(articles):
    articles_text = ""
    for a in articles:
        articles_text += f"Title: {a['title']}\nDescription: {a['description']}\n\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You summarize groups of tech articles for developers. You are concise, clear, and neutral. Focus on trends, themes, and insights, not individual article summaries. Include concrete examples if possible.",
            },
            {
                "role": "user",
                "content": f"""
Here are today's top developer articles:

{articles_text}

Write a Slack-friendly AI summary (3–5 sentences, ~90–100 words) that:
- Describes the main trends or themes across these articles
- Includes at least one concrete tool, project, or discussion from the articles as an example
- Explains why these trends are relevant today
- Avoids summarizing each article individually
- Does not repeat titles or snippets
- Focuses on actionable insight or meaningful context for developers
""",
            },
        ],
    )
    return response.choices[0].message.content


articles_list = fetch_articles()
ai_insights = summarize_with_ai(articles_list)

message = ":newspaper: *Today's Top 5 Dev Articles*\n\n"
message += f":robot_face: *AI Insights:* {ai_insights}\n\n---\n\n"
for article in articles_list:
    message += f"• *{article['title']}*\n"
    message += f"   _{article['description']}_\n"
    message += f"   {article['link']}\n\n"
payload = {"text": message}
response = requests.post(WEBHOOK_URL, json=payload)

print("Status code:", response.status_code)
print("Response:", response.text)
