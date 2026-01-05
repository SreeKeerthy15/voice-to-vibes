# Voice to Vibes 🎧  
Speech Emotion Recognition & Music Recommendation System

## Project Overview
Voice to Vibes is a voice-based intelligent system that analyzes user speech to detect emotions
and recommends music accordingly. The system supports multilingual interaction, including
Indian regional languages.

---

## Phase 1: Frontend & Audio Capture
- Streamlit-based user interface
- Language selection (English, Telugu, Hindi)
- Browser-based audio recording with manual start/stop
- Audio stored in WAV format for processing

---

## Phase 2: Speech Recognition (ASR)
- Integrated Whisper-based multilingual speech recognition
- Supports English, Hindi, and Telugu speech
- Automatic language detection with user preference guidance
- ASR pipeline prepared for emotion analysis

> Note: Telugu transcription accuracy is an ongoing improvement area.

---

## Technologies Used
- Python
- Streamlit
- OpenAI Whisper
- FFmpeg

---

## Upcoming Phases
- Audio preprocessing & feature extraction
- Emotion detection using CNN/LSTM
- Emotion-aware music recommendation
- Multilingual voice response
