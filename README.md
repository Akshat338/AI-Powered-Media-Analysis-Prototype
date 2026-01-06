# AI-Powered Sentiment Dashboard 🎥🎧

## Overview
This project is a **vertical prototype** demonstrating a full-stack AI application that:
- Accepts audio/video uploads
- Processes them asynchronously
- Transcribes speech using OpenAI Whisper
- Performs sentiment analysis
- Displays results on a clean dashboard


## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **AI Models:** OpenAI Whisper, TextBlob
- **Async Processing:** FastAPI BackgroundTasks

---

## Features
- Non-blocking background AI processing
- Real-time polling with progress feedback
- Clean, responsive UI
- Graceful error handling

---

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/sentiment-dashboard.git
cd sentiment-dashboard

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Install FFmpeg (Required for Whisper)
Windows
Download from https://ffmpeg.org
 and add to PATH.

5.Running the Application
uvicorn app:app --reload

Open browser:
http://127.0.0.1:8000










