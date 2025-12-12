
# Tech News Slack Bot

This bot posts daily tech articles from DEV.to into a Slack channel using GitHub Actions.

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

### 3. Add the Webhook to GitHub

In your fork:

* Go to **Settings → Secrets and variables → Actions**
* Add a new secret:

```
Name: SLACK_WEBHOOK_URL
Value: <your webhook URL>
```

---

### 4. Daily Automation (GitHub Actions)

The workflow is in:

```
.github/workflows/schedule.yaml
```

It runs once per day using a cron schedule and executes the Python script.

If you want to change the time, edit the `cron:` line in the file.

---

### 5. Test it once

If you want to test right away:

* Go to **Actions**
* Open the workflow
* Click **Run workflow**

You should get a message in Slack if everything is set up correctly.