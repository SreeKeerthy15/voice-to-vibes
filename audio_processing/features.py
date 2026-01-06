import librosa
import numpy as np

def extract_features(audio_path):
    # Load audio
    y, sr = librosa.load(audio_path, sr=22050)

    # Trim silence
    y, _ = librosa.effects.trim(y)

    # Normalize
    y = librosa.util.normalize(y)

    # MFCC (40 coefficients)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)

    # Chroma
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma = np.mean(chroma.T, axis=0)

    # Mel Spectrogram
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    mel = np.mean(mel.T, axis=0)

    return mfcc, chroma, mel
