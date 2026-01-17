import random

EMOTIONS = ["Happy", "Sad", "Angry", "Calm", "Neutral"]

def predict_emotion(mfcc, chroma, mel):
    emotion = random.choice(EMOTIONS)
    confidence = round(random.uniform(0.65, 0.9), 2)
    return emotion, confidence
