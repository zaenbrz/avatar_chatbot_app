from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from gtts import gTTS
import os
import uuid
from rhubarb_wrapper import run_rhubarb
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static folders
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/speak/")
async def speak_text(text: str = Form(...)):
    try:
        # Generate unique filenames
        audio_id = uuid.uuid4().hex
        mp3_filename = f"{audio_id}.mp3"
        mp3_path = os.path.join(UPLOAD_DIR, mp3_filename)

        # 1) Convert text → speech
        tts = gTTS(text)
        tts.save(mp3_path)

        # 2) Run Rhubarb → lipsync JSON (make sure it outputs inside uploads)
        json_path = run_rhubarb(mp3_path)

        with open(json_path, "r") as f:
            lipsync_data = f.read()

        # ✅ Return proper static URLs
        return JSONResponse(content={
            "audio_file": f"/uploads/{mp3_filename}",
            "lipsync": lipsync_data
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
async def root():
    return {"message": "Rhubarb FastAPI backend (Text → Audio + Lipsync) is running!"}
