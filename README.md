# Voice to Vibes 🎧  
### Speech Emotion Recognition & Intelligent Music Recommendation System

---

## 📌 Project Overview

**Voice to Vibes** is an intelligent voice-driven system that analyzes **how a user speaks**, understands their **emotional state**, and recommends music that best fits their mood.

Unlike traditional music recommendation systems that rely only on text or listening history, Voice to Vibes combines:

- **What the user says** (speech content)
- **How the user sounds** (acoustic emotion signals)
- **What the user wants** (explicit intent)

This fusion enables **human-like reasoning** for music recommendation.

---

## 🏗️ System Architecture (High Level)

Web Frontend
↓
Audio Capture (Mic / Upload)
↓
FastAPI Backend
↓
Speech Recognition (Whisper ASR)
↓
Audio Feature Extraction (MFCC, Chroma, Mel)
↓
Emotion Detection
↓
Intent Detection
↓
Decision Engine
↓
Music Recommendation (iTunes API)
↓
30s Audio Preview Playback


---

## 🟢 Phase 1: Frontend & Audio Capture (Completed)

- Modern **web-based UI** using HTML, CSS, JavaScript
- Dark, gradient-based professional design
- Language selection:
  - English
  - Hindi
  - Telugu
- Browser-based microphone recording
- Audio file upload support
- **Live animated waveform** during recording
- Card-based UI for analysis results
- Spotify-style music cards
- Play / Pause / Next / Previous controls

---

## 🟢 Phase 2: Speech Recognition (ASR) (Completed)

- Integrated **OpenAI Whisper** for multilingual speech recognition
- Supported languages:
  - English (EN)
  - Hindi (HI)
  - Telugu (TE)
- User-selected language improves transcription accuracy
- Original transcript preserved in spoken language
- Non-English speech translated to English for downstream processing

> **Note:**  
> ASR accuracy depends on audio quality and model size.  
> Whisper was selected for its multilingual robustness and real-world reliability.

---

## 🟢 Phase 3: Audio Feature Extraction (Completed)

To capture emotional cues beyond words, the system extracts:

- **MFCC (Mel-Frequency Cepstral Coefficients)**  
  Captures vocal tone and timbre

- **Chroma Features**  
  Represents pitch and harmonic characteristics

- **Mel Spectrogram**  
  Models energy distribution across frequencies

These features form the acoustic foundation for emotion inference.

---

## 🟢 Phase 4: Emotion Detection (Completed)

- Emotion inferred from extracted audio features
- Output includes:
  - Emotion label (Happy, Sad, Angry, Calm, Neutral, etc.)
  - Confidence score (0–100%)

### ⚠️ Important Principle

> **Emotion detection is a signal, not the truth.**

The confidence score reflects pattern strength, not a definitive emotional state.

---

## 🟢 Phase 5: Intent Detection (Completed)

- Rule-based intent detection using the speech transcript
- Identifies explicit requests such as:
  - “play happy songs”
  - “I want calm music”
  - “something energetic”

**Explicit intent always has higher priority than emotion.**

---

## 🟢 Phase 6: Decision Engine (Core Intelligence – Completed)

The decision engine fuses multiple signals to behave more like a human.

### Decision Logic

1. If **explicit intent exists** → follow intent  
2. Else → match detected emotion  

### Why This Matters

Instead of blindly following emotion or text alone, the system reasons about:
- Speech content
- Emotional tone
- User intent

This fusion is what makes **Voice to Vibes unique**.

---

## 🟢 Phase 7: Music Recommendation & Playback (Completed)

- Emotion-based and intent-based music recommendation
- Integrated with **Apple iTunes / Apple Music Preview API**
- 30-second audio previews (no premium account required)
- Single-card music player with:
  - Play / Pause
  - Next / Previous navigation
- External link to open full song source

---

## 🧪 Model Training (Academic Component)

For academic validation, a separate training pipeline was implemented:

- Public datasets used:
  - RAVDESS
  - CREMA-D
  - TESS
  - SAVEE
- Extracted MFCC, Chroma, and Mel features
- Trained a **Random Forest emotion classifier**
- Achieved high validation accuracy on curated datasets

> **Note:**  
> The deployed system prioritizes real-time inference and currently uses a simplified emotion inference pipeline, while the trained model is retained for academic evaluation and future integration.

---

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- OpenAI Whisper
- Librosa
- NumPy
- FFmpeg

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap (CDN)
- Browser MediaRecorder API
- Web Audio API (Waveform visualization)

### APIs & Tools
- Apple Music / iTunes Preview API
- Git & GitHub
- VS Code

---

## 📊 Current Project Status

- Fully functional end-to-end system
- Stable frontend–backend integration
- Multilingual voice support (EN / HI / TE)
- Ready for:
  - Academic review
  - Live demos
  - Portfolio showcase

---

## 🚀 Future Enhancements

- Playlist-level recommendations
- Advanced multilingual music filtering
- Artist based filtering

---

## 🎯 Key Takeaway

**Voice to Vibes is not just a music recommender.**

It is an **emotion-aware conversational system** that blends:
- Speech processing
- Audio signal analysis
- Machine learning
- Human-centered design

to create a more natural and intelligent listening experience.
