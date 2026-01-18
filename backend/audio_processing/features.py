import librosa
import numpy as np
import math

def extract_features(audio_path):
    # Load audio
    y, sr = librosa.load(audio_path, sr=22050)

    # 🚨 SAFETY: empty or silent audio
    if y is None or len(y) == 0:
        return zero_features()

    # Trim silence
    y, _ = librosa.effects.trim(y)

    if y is None or len(y) == 0:
        return zero_features()

    # Normalize safely
    max_val = np.max(np.abs(y))
    if max_val == 0 or np.isnan(max_val) or np.isinf(max_val):
        return zero_features()

    y = y / max_val

    # -------- MFCC --------
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)

    # -------- Chroma --------
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma = np.mean(chroma.T, axis=0)

    # -------- Mel --------
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    mel = np.mean(mel.T, axis=0)

    # 🚨 FINAL SANITIZATION
    mfcc = sanitize_array(mfcc)
    chroma = sanitize_array(chroma)
    mel = sanitize_array(mel)

    return mfcc, chroma, mel


# ---------- HELPERS ----------

def zero_features():
    return (
        np.zeros(40),
        np.zeros(12),
        np.zeros(128)
    )

def sanitize_array(arr):
    arr = np.array(arr, dtype=np.float32)
    arr[np.isnan(arr)] = 0.0
    arr[np.isinf(arr)] = 0.0
    return arr
