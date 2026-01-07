from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uuid
import os
import json

from analysis_logic import process_media

app = FastAPI()

UPLOAD_DIR = "uploads"
RESULT_DIR = "results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception:
        return JSONResponse({"error": "File upload failed"}, status_code=500)

    background_tasks.add_task(process_media, job_id, file_path)

    return {"job_id": job_id, "status": "processing"}


@app.get("/status/{job_id}")
def check_status(job_id: str):
    result_path = os.path.join(RESULT_DIR, f"{job_id}.json")

    if not os.path.exists(result_path):
        return {"status": "processing", "progress": 50}

    with open(result_path) as f:
        return json.load(f)

