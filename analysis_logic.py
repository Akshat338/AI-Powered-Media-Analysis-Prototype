import whisper
import os
import json
from textblob import TextBlob

RESULT_DIR = "results"

# Load Whisper model ONCE (important)
model = whisper.load_model("base")

def process_media(job_id: str, file_path: str):
    try:
        # Transcription
        result = model.transcribe(file_path)
        transcript = result["text"]

        # Sentiment analysis
        blob = TextBlob(transcript)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        output = {
            "status": "completed",
            "transcript": transcript,
            "sentiment": sentiment,
            "polarity": polarity
        }

    except Exception as e:
        output = {
            "status": "error",
            "message": str(e)
        }

    with open(os.path.join(RESULT_DIR, f"{job_id}.json"), "w") as f:
        json.dump(output, f)
