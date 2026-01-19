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

# Store temp audio outside repo
AUDIO_DIR = os.path.join(os.path.expanduser("~"), "voice_to_vibes_audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"status": "Voice to Vibes backend running"}

@app.post("/analyze")
async def analyze_audio(
    audio: UploadFile = File(...),
    preferred_language: str = "English"  # English | Hindi | Telugu
):
    try:
        # ---------- SAVE AUDIO ----------
        file_path = os.path.join(AUDIO_DIR, "input.wav")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        # ---------- ASR ----------
        speech_data = speech_to_text(file_path, preferred_language)

        original_text = speech_data.get("original_text", "")
        translated_text = speech_data.get("translated_text", "")
        language = speech_data.get("language", "EN")

        # ---------- AUDIO FEATURES ----------
        mfcc, chroma, mel = extract_features(file_path)

        # ---------- EMOTION ----------
        emotion, confidence = predict_emotion(mfcc, chroma, mel)

        emotion = str(emotion) if emotion else "Unknown"
        confidence = float(confidence) if confidence else 0.0

        # ---------- INTENT (ALWAYS ON ENGLISH) ----------
        intent = detect_intent(translated_text) if translated_text else None

        # ---------- DECISION ----------
        final_category = decide_music_category(
            intent=intent,
            emotion=emotion,
            user_choice=None
        )

        # ---------- MUSIC (iTunes) ----------
        from backend.music.itunes_client import search_songs_by_emotion
        songs = search_songs_by_emotion(final_category)


        # ---------- RESPONSE ----------
        response = {
            "transcript_original": original_text,
            "transcript_english": translated_text,
            "language": language,          # EN / HI / TE
            "emotion": emotion,
            "confidence": confidence,
            "intent": intent,
            "final_category": final_category,
            "songs": songs
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            content={
                "error": "Audio analysis failed",
                "details": str(e)
            },
            status_code=500
        )

@app.get("/explore")
def explore(category: str):
    from backend.recommender.recommend import recommend_songs
    songs = recommend_songs(category)
    return {"songs": songs}
