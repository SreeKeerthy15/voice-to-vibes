# Voice to Vibes 🎧  
Speech Emotion Recognition & Music Recommendation System

## Project Overview
Voice to Vibes is an intelligent voice-driven system that analyzes how a user speaks, understands
their emotional state, and recommends music that best fits their mood.  
The system combines **speech emotion recognition**, **intent detection**, and **user preference
logic** to make human-like music recommendations.

Unlike traditional recommendation systems, Voice to Vibes does not rely only on text or emotion.
It fuses **what the user says**, **how they sound**, and **what they want**, making the experience
more natural and adaptive.

---

## System Architecture (High Level)

Frontend (Web UI)
→ Audio Capture (Mic / Upload)
→ Backend API (FastAPI)
→ Speech Recognition (ASR)
→ Audio Feature Extraction
→ Emotion Detection
→ Intent Detection
→ Decision Engine
→ Music Recommendation
→ Audio Preview Playback

---

## Phase 1: Frontend & Audio Capture (Completed)
- Modern web-based UI (HTML, CSS, JavaScript)
- Dark, gradient-based professional design
- Language selection (English, Hindi)
- Browser-based microphone recording
- Upload support for audio files
- Animated mic waveform during recording
- Card-based UI for analysis results
- Spotify-style song cards with audio previews

---

## Phase 2: Speech Recognition (ASR) (Completed)
- Integrated Whisper-based multilingual speech recognition
- Supports:
  - English
  - Hindi
- User-selected language guidance for higher accuracy
- Original transcript preserved in spoken language
- Hindi speech can be translated to English for downstream processing

> Note: ASR accuracy depends on audio quality and model size.  
> The system is designed to support future multilingual expansion.

---

## Phase 3: Audio Feature Extraction (Completed)
To understand emotion beyond words, the system extracts acoustic features:

- **MFCC (Mel-Frequency Cepstral Coefficients)**  
  Captures timbral and vocal tone characteristics

- **Chroma Features**  
  Represents pitch and harmonic content

- **Mel Spectrogram**  
  Models energy distribution across frequencies

These features form the foundation of emotion inference.

---

## Phase 4: Emotion Detection (Completed)
- Emotion prediction based on extracted audio features
- Outputs:
  - Emotion label (Happy, Sad, Angry, Calm, Neutral, etc.)
  - Confidence score (0–100%)

### Important Concept
**Emotion detection is a signal, not the truth.**

The confidence score indicates how strongly the model perceives a pattern,
not an absolute emotional state.

---

## Phase 5: Intent Detection (Completed)
- Rule-based intent detection using speech transcript
- Identifies explicit requests such as:
  - “play something energetic”
  - “I want calm music”
  - “romantic songs”

Intent has higher priority than emotion when clearly expressed.

---

## Phase 6: Decision Engine (Core Intelligence – Completed)

The decision engine combines multiple signals to behave more like a human.

### Decision Logic
1. If **explicit intent exists** → follow intent  
2. Else if **user preference = uplift** → recommend opposite emotion  
3. Else → match detected emotion  

### Why This Matters
Instead of blindly following emotion or text, the system reasons about:
- What the user said
- How they sounded
- What experience they want

This fusion is what makes **Voice to Vibes unique**.

---

## Phase 7: Music Recommendation & Playback (Completed)
- Emotion-based and intent-based song recommendation
- Integrated with iTunes / Apple Music preview APIs
- 30-second audio previews (no premium account required)
- Multiple recommendations per session
- Play, pause, next, and previous controls
- External link to open full song source

---

## Technologies Used

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

### APIs & Tools
- Apple Music / iTunes Preview API
- Git & GitHub

---

## Current Project Status
- Core system complete and stable
- Fully functional end-to-end pipeline
- Frontend and backend integrated
- Ready for demos, reviews, and portfolio showcase

---

## Future Enhancements
- Explore page with mood-based carousels
- About page with explainable AI visuals
- Improved emotion confidence visualization
- Playlist-level recommendations
- Advanced multilingual support

---

## Key Takeaway
Voice to Vibes is not just a music recommender.  
It is an **emotion-aware conversational system** that blends signal processing,
machine learning, and user-centric design to create a more human experience.
