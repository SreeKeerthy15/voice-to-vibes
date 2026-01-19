import os
import librosa
import numpy as np
import pandas as pd

DATASET_PATHS = {
    "RAVDESS": "training/datasets/RAVDESS",
    "CREMA-D": "training/datasets/CREMA-D",
    "TESS": "training/datasets/TESS",
    "SAVEE": "training/datasets/SAVEE"
}

EMOTION_MAP = {
    "happy": "Happy",
    "sad": "Sad",
    "angry": "Angry",
    "calm": "Calm",
    "neutral": "Neutral"
}

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=3)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40), axis=1)
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr), axis=1)
    mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr), axis=1)
    return np.hstack([mfcc, chroma, mel])

data = []

for dataset, path in DATASET_PATHS.items():
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".wav"):
                emotion = None
                name = file.lower()
                for key in EMOTION_MAP:
                    if key in name:
                        emotion = EMOTION_MAP[key]

                if emotion:
                    full_path = os.path.join(root, file)
                    features = extract_features(full_path)
                    row = features.tolist()
                    row.append(emotion)
                    data.append(row)

columns = [f"f{i}" for i in range(len(data[0]) - 1)] + ["emotion"]
df = pd.DataFrame(data, columns=columns)

df.to_csv("training/features.csv", index=False)
print("✅ features.csv created")
