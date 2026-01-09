import pandas as pd
import random

def recommend_songs(category, top_k=3):
    df = pd.read_csv("music/songs.csv")

    # Filter by emotion/category
    filtered = df[df["emotion"].str.lower() == category.lower()]

    if filtered.empty:
        return []

    # Randomize & pick top_k
    recommendations = filtered.sample(
        min(top_k, len(filtered))
    )

    return recommendations.to_dict(orient="records")
