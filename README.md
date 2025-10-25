---

# Micr0 Chatbot

A web-based chatbot using the Google Gemini API.
Built with a modern chat interface (HTML/CSS) + a Python backend (Flask) to handle user-bot conversation.

---

## Features

* Clean, modern chat UI with user and bot bubbles.
* Multi-line message support from both user and bot.
* Automatic code-block highlighting in messages (so code snippets appear nicely).
* Automatic “scroll to latest message” behaviour.
* Flask backend that connects to the Google Gemini API (so the bot is powered by a large-language model).
* Simple setup (see prerequisites & installation below).

---

## Demo

> A screenshot of the interface:
> <img width="1839" height="945" alt="Screenshot 2025-10-01 070629" src="https://github.com/user-attachments/assets/4228ffd6-e4ff-4762-a5ee-95b134b6ae43" />


---

## Prerequisites

* Python 3.9 or higher.
* `pip` (Python package installer).
* A valid Google Gemini API key (or access token) with permissions to use the model.

---

## Installation & Running

1. Clone the repository:

   ```bash
   git clone https://github.com/PARINEETH2004/micr0_chatbot.git
   cd micr0_chatbot
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key in your environment:

   * On macOS/Linux:

     ```bash
     export GEMINI_API_KEY="your_api_key_here"
     ```
   * On Windows (PowerShell):

     ```powershell
     setx GEMINI_API_KEY "your_api_key_here"
     ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000` (or the address shown in your terminal) to start chatting.

---

## Architecture & Files

* `app.py` – Python Flask server, handles HTTP endpoints, sends user input to the Gemini API, returns responses.
* `index.html` – The front-end chat interface (web page) involving HTML + CSS + JS.
* `static/` – Folder containing static assets (CSS, JS, images) used by the front end.
* `requirements.txt` – List of Python dependencies.
* README.md – This file (project documentation).

---

## Usage Notes

* Enter a question or prompt in the chat UI; the bot will respond using the Gemini model.
* You can include code snippets in your prompts; the interface will highlight them (use triple back-ticks ``` for code blocks).
* Make sure your API key is valid and has quota/permissions for Gemini usage — errors will show if the key is missing or invalid.
* This is a simple proof-of-concept; for production use you may want to add authentication, logging, error-handling, rate-limiting, etc.

---

## Customisation Ideas

* Swap in a different LLM or model endpoint (if you want a lighter or domain-specific model).
* Change the front-end styling (CSS) to match your brand/theme.
* Add features like conversation history persistence, user sessions, chat export.
* Add deployment scripts (e.g., Dockerfile or Heroku/Cloud Run setup) so the bot can run in production.
* Add file-upload, image-input or multimodal support (depending on Gemini capabilities) to handle images + text.

---

## About

This chatbot project is a simple, clean interface layered over a large-language-model backend. It’s meant as a starting point — you can build on it, customise it, extend it for your use case.

---
