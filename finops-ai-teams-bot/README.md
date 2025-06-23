# 🤖 FinOps AI Teams Bot

A conversational Microsoft Teams bot built with Azure Bot Framework + Azure OpenAI that:

- 💰 Analyzes underutilized Azure resources
- 🧠 Summarizes cost-saving recommendations using GPT
- 💬 Responds to FinOps-related queries in Teams

![FinOpsBot Logo](assets/logo.png)

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.WebApp)
[![CI](https://github.com/Deepanshukatara123/finops-ai-teams-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/Deepanshukatara123/finops-ai-teams-bot/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📦 Features

- Azure-native cost + usage analysis
- GPT-powered report summarization
- Deployed on Azure Web App Bot
- Teams-integrated chatbot interface
- Container-ready (Docker)
- CI/CD pipeline integration

---

## 🚀 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Deepanshukatara123/finops-ai-teams-bot.git
cd finops-ai-teams-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Required Environment Variables
Create a `.env` file with the following:
```env
AZURE_SUBSCRIPTION_ID=<your-sub-id>
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
```

### 4. Run Locally
```bash
python bot_app.py
```

### 5. Deploy to Azure
- Create a Web App Bot in Azure
- Connect to Microsoft Teams (Channels > Add)
- Set Messaging Endpoint: `https://<your-app>.azurewebsites.net/api/messages`
- Deploy via Azure CLI or GitHub Actions

---

## 🐳 Docker Support

### Dockerfile
```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot_app.py"]
```

### Build & Run
```bash
docker build -t finops-ai-teams-bot .
docker run -p 3978:3978 --env-file .env finops-ai-teams-bot
```

---

## ✅ GitHub Actions CI/CD

### `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [ main ]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Deploy to Azure Web App
        uses: Azure/webapps-deploy@v2
        with:
          app-name: finops-ai-teams-bot
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
```

---

## 📁 Code Overview

| File | Purpose |
|------|---------|
| `bot_app.py` | Flask server routing incoming messages |
| `teams_bot.py` | Core logic of how bot responds to Teams chats |
| `finops_tools.py` | Azure SDK usage analyzer agent |
| `report_agent.py` | Azure OpenAI summarizer agent |
| `.env.example` | Template for required environment variables |
| `Dockerfile` | Build container image for the bot |
| `.github/workflows/ci.yml` | CI/CD deployment pipeline |

---

## ✅ Tests

Add unit tests with `pytest`:
```
tests/
├── test_finops_tools.py
├── test_report_agent.py
```

---

## 📌 Future Enhancements
- AutoGen integration for multi-agent orchestration
- Adaptive Cards for rich Teams responses
- Terraform optimizer agent
- Web dashboard for FinOps reports

---

## 📄 License
MIT
