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

---

## Phase 3: Intelligence Layer (Completed)

### Features Implemented
- Text-based intent detection using keyword rules
- Emotion-aware clarification dialogue
- Priority-based decision engine
- Intelligent resolution between:
  - Explicit user intent
  - Detected emotion
  - User preference (match vs uplift)

### Decision Logic
1. If explicit intent exists → intent-based recommendation
2. Else if user chooses uplift → opposite emotion mapping
3. Else → emotion-matching recommendation

### Outcome
The system can now reason like a human by combining
what the user says, how they sound, and what they prefer.


## Technologies Used
- Python
- Streamlit
- OpenAI Whisper
- FFmpeg
- Librosa
- NumPy
- GitHub

---

