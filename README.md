# 🌦️ Weather Analyzer

A modular, cloud-ready weather analysis tool built for real-world deployment. Designed with CLI/GUI flexibility, Docker containerization, and EC2 compatibility for scalable, public-facing access.

---

## 🚀 Features

- 🔍 **Live Weather Data** via API integration
- 🖥️ **Dual Interface**: CLI for headless/cloud use, GUI for local interaction
- 🐳 **Dockerized** for portable deployment
- ☁️ **EC2-Compatible**: Seamless volume mounting and persistent output
- 🔐 **Secure Secrets Management** with `.env` support
- 📊 **JSON Output** for easy logging and downstream integration

---

## 🛠️ Tech Stack

- Python (requests, tkinter, argparse)
- Docker
- AWS EC2 (Ubuntu)
- Git Bash (Windows) & Linux shell compatibility

---

## 📦 Setup Instructions

### Local (CLI/GUI)
```bash
git clone https://github.com/myshra777-ai/weather-analyzer.git
cd weather-analyzer
pip install -r requirements.txt
python app/main.py --city "Delhi"
