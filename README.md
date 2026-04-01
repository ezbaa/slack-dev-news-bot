# Tech News Slack Bot

## About

This bot delivers daily tech articles from DEV.to straight to your Slack channel. For each article, it provides an AI-generated summary so you can catch up quickly.
---

## Setup

### 1. Fork this repository

Click **Fork** to create your own copy.

---

### 2. Create a Slack Incoming Webhook

1. Go to https://api.slack.com/messaging/webhooks
2. Create or choose a Slack app
3. Enable **Incoming Webhooks**
4. Choose the channel you want to post to
5. Copy the Webhook URL

---

### 3. Get a Groq API Key

1. Go to https://console.groq.com
2. Create a free account 
3. Go to **API Keys** and create a new key
4. Copy the key

---

### 4. Add Secrets to GitHub

In your fork:

* Go to **Settings → Secrets and variables → Actions**
* Add two secrets:
```
Name: SLACK_WEBHOOK_URL
Value: <your Slack webhook URL>

Name: GROQ_API_KEY
Value: <your Groq API key>
```

---

### 5. Daily Automation (GitHub Actions)

The workflow is in:
```
.github/workflows/schedule.yaml
```

It runs once per day using a cron schedule and executes the Python script.
If you want to change the time, edit the `cron:` line in the file.

---

### 6. Test it once

If you want to test right away:

* Go to **Actions**
* Open the workflow
* Click **Run workflow**

You should get a message in Slack with AI-powered summaries if everything is set up correctly.

---

## Local Development

If you want to run the bot locally, create a `.env` file in the project root:
```
SLACK_WEBHOOK_URL=your_slack_webhook_url
GROQ_API_KEY=your_groq_api_key
```

---
