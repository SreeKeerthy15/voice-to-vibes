from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import os

from backend.asr.speech_to_text import speech_to_text
from backend.audio_processing.features import extract_features
from backend.emotion.predictor import predict_emotion
from backend.intent.detect_intent import detect_intent
from backend.decision.engine import decide_music_category
from backend.recommender.recommend import recommend_songs

app = FastAPI(title="Voice to Vibes API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚨 MOVE TEMP AUDIO OUTSIDE PROJECT FOLDER
AUDIO_DIR = os.path.join(os.path.expanduser("~"), "voice_to_vibes_audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"status": "Voice to Vibes backend running"}

@app.post("/analyze")
async def analyze_audio(
    audio: UploadFile = File(...),
    preferred_language: str = "English"
):
    try:
        file_path = os.path.join(AUDIO_DIR, "input.wav")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        # 🔤 Speech processing
        speech_data = speech_to_text(file_path, preferred_language)

        original_text = speech_data["original_text"]
        translated_text = speech_data["translated_text"]
        language = speech_data["language"]

        # 🎵 Audio features
        mfcc, chroma, mel = extract_features(file_path)

        # 🧠 Emotion uses ENGLISH meaning
        emotion, confidence = predict_emotion(mfcc, chroma, mel)

        emotion = str(emotion) if emotion else "Unknown"
        confidence = float(confidence) if confidence else 0.0

        # 🎯 Intent detection on English text
        intent = detect_intent(translated_text) if translated_text else None

        final_category = decide_music_category(
            intent=intent,
            emotion=emotion,
            user_choice=None
        )

        from backend.music.itunes_client import search_songs_by_emotion
        songs = search_songs_by_emotion(final_category)

        response = {
            "transcript_original": original_text,
            "transcript_english": translated_text,
            "language": language,
            "emotion": emotion,
            "confidence": confidence,
            "intent": intent,
            "final_category": final_category,
            "songs": songs
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            content={"error": "Audio analysis failed", "details": str(e)},
            status_code=500
        )
