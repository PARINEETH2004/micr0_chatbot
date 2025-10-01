# Microplastic Chatbot

A web-based chatbot that uses Google Gemini API to answer user questions. Styled with modern CSS, supports code highlighting, and has a responsive chat interface.

## Features

- Clean, modern chat interface with user and bot bubbles
- Supports multi-line messages
- Highlights code blocks automatically
- Auto-scrolls to the latest messages
- Flask backend connecting to Google Gemini API

## Demo

<img width="1839" height="945" alt="Screenshot 2025-10-01 070629" src="https://github.com/user-attachments/assets/df7921e6-eced-468c-acdf-f1a889dc6623" />


## Prerequisites

- Python 3.9+
- pip

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/microplastic-chatbot.git
cd microplastic-chatbot


pip install -r requirements.txt

# macOS/Linux
export GEMINI_API_KEY="your_api_key_here"

# Windows (PowerShell)
setx GEMINI_API_KEY "your_api_key_here"


python app.py
