from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import traceback

# -------- Import internal modules (backend package) --------
from backend.asr.speech_to_text import speech_to_text
from backend.audio_processing.features import extract_features
from backend.emotion.predictor import predict_emotion
from backend.intent.detect_intent import detect_intent
from backend.decision.engine import decide_music_category
from backend.recommender.recommend import recommend_songs
from backend.tts.speak import speak_response

# -------- App initialization --------
app = FastAPI(title="Voice to Vibes API")

# Allow frontend (React later) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- Audio storage --------
AUDIO_DIR = "temp_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# -------- Health check (optional but recommended) --------
@app.get("/")
def root():
    return {"status": "Voice to Vibes backend running"}

# -------- Core API --------
@app.post("/analyze")
async def analyze_audio(
    audio: UploadFile = File(...),
    preferred_language: str = "English"
):
    
        # Always use a fixed filename (Swagger-safe, Whisper-safe)
        file_path = os.path.join(AUDIO_DIR, "input.wav")

        # Save uploaded audio
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        # Debug safety logs
        print("Saved audio to:", file_path)
        print("File size (bytes):", os.path.getsize(file_path))

        if os.path.getsize(file_path) == 0:
            raise ValueError("Uploaded audio file is empty")

        # 1️⃣ Speech to text
        transcript, detected_lang = speech_to_text(
            file_path,
            preferred_language
        )

        # 2️⃣ Audio features
        mfcc, chroma, mel = extract_features(file_path)

        # 3️⃣ Emotion detection
        emotion, confidence = predict_emotion(
            mfcc,
            chroma,
            mel
        )

        # 4️⃣ Intent detection
        intent = detect_intent(transcript) if transcript else None

        # 5️⃣ Decision engine
        final_category = decide_music_category(
            intent=intent,
            emotion=emotion,
            user_choice=None
        )

        # 6️⃣ Song recommendation
        songs = recommend_songs(final_category)

        return {
            "transcript": transcript,
            "detected_language": detected_lang,
            "emotion": emotion,
            "confidence": confidence,
            "intent": intent,
            "final_category": final_category,
            "songs": songs
        }


