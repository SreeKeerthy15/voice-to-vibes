import streamlit as st
import os
from asr.speech_to_text import speech_to_text

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
