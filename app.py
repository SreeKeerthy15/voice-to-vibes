import streamlit as st
import os
from asr.speech_to_text import speech_to_text
from audio_processing.features import extract_features
from emotion.predictor import predict_emotion
from intent.detect_intent import detect_intent
from decision.engine import decide_music_category
from recommender.recommend import recommend_songs
from tts.speak import speak_response

# ---------- Configuration ----------
AUDIO_FOLDER = "audio"
AUDIO_FILE = "user_audio.wav"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# ---------- UI ----------
st.set_page_config(page_title="Voice to Vibes", layout="centered")

st.title("🎧 Voice to Vibes")
st.write("Speak to express your mood. I'll handle the music 🎶")

# Language Selection
st.subheader("Select Language")
language = st.selectbox(
    "Choose your preferred language:",
    ("English", "Telugu", "Hindi")
)
st.write(f"Selected Language: **{language}**")

# Audio Recorder (Browser-based)
st.subheader("Record Your Voice")
audio_file = st.audio_input("Click to record")

# ------------------ IMPORTANT BLOCK ------------------
if audio_file is not None:
    file_path = os.path.join(AUDIO_FOLDER, AUDIO_FILE)

    # Save audio
    with open(file_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.success("Recording saved successfully!")
    st.audio(file_path)

    # Initialize ASR outputs safely
    transcript = None
    detected_lang = None


    # -------- PHASE 2 : ASR OUTPUT --------
    st.subheader("Speech Recognition Output")

    with st.spinner("Running speech recognition..."):
        try:
            transcript, detected_lang = speech_to_text(file_path, language)

            st.write("📝 Transcript:")
            st.write(transcript)

            st.write("🌐 Detected Language:")
            st.write(detected_lang)

        except Exception as e:
            st.error("Speech recognition failed")
            st.exception(e)


    # -------- PHASE 2 : AUDIO PREPROCESSING --------
    st.subheader("Audio Feature Extraction")

    mfcc, chroma, mel = extract_features(file_path)

    st.write("MFCC shape:", mfcc.shape)
    st.write("Chroma shape:", chroma.shape)
    st.write("Mel Spectrogram shape:", mel.shape)

    st.subheader("Emotion Detection")

    emotion, confidence = predict_emotion(mfcc, chroma, mel)

    st.write("Detected Emotion:", emotion)
    st.write("Confidence Score:", confidence)

        # -------- SAFE INTENT DETECTION --------
    if transcript:
        intent = detect_intent(transcript)
    else:
        intent = None


    st.subheader("Intent Detection")

    if intent:
        st.write("Explicit Intent Detected:", intent)
    else:
        st.write("No explicit intent detected")

    user_choice = None

    if intent is None and confidence > 0.7 and emotion in ["Sad", "Neutral", "Calm"]:
        st.subheader("Clarification")

        st.write(
            f"You sound {emotion.lower()}. "
            "Do you want music that matches your mood "
            "or music that uplifts you?"
        )

        user_choice = st.radio(
            "Choose one:",
            ("Match my mood", "Uplift me")
        )

    final_category = decide_music_category(
        intent,
        emotion,
        user_choice
    )

    st.subheader("Final Music Decision")
    st.write("Recommended Music Category:", final_category)

    st.subheader("🎶 Recommended Songs")

    songs = recommend_songs(final_category)

    if not songs:
        st.write("No songs found for this category.")
    else:
        for song in songs:
            st.write(f"**{song['title']}** — {song['artist']}")

            preview = song.get("preview_url")
            if isinstance(preview, str) and preview.strip() != "":
                st.audio(preview)

            col1, col2 = st.columns(2)
            with col1:
                st.button("👍 Like", key=f"like_{song['title']}")
            with col2:
                st.button("⏭ Skip", key=f"skip_{song['title']}")

    response_text = f"I will play something {final_category.lower()} for you."

    audio_response = speak_response(response_text, language)

    st.subheader("🔊 Voice Response")
    st.audio(audio_response)
