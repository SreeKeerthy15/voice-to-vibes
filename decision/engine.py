OPPOSITE_EMOTION_MAP = {
    "Sad": "Energetic",
    "Angry": "Calm",
    "Calm": "Happy",
    "Neutral": "Happy"
}

def decide_music_category(intent, emotion, user_choice):
    # Highest priority: explicit intent
    if intent:
        return intent.capitalize()

    # Second priority: uplift choice
    if user_choice == "Uplift me":
        return OPPOSITE_EMOTION_MAP.get(emotion, "Happy")

    # Default: match emotion
    return emotion
