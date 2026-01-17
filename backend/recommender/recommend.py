import pandas as pd
import random
import os

BASE_DIR = os.path.dirname(__file__)           # backend/recommender
MUSIC_PATH = os.path.join(
    BASE_DIR,
    "..", "music", "songs.csv"
)

def recommend_songs(category, top_k=3):
    df = pd.read_csv(MUSIC_PATH)

    # Filter by emotion/category
    filtered = df[df["emotion"].str.lower() == category.lower()]

    if filtered.empty:
        return []

    # Randomize & pick top_k
    recommendations = filtered.sample(
        min(top_k, len(filtered))
    )

    return recommendations.to_dict(orient="records")
