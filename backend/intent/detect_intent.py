INTENT_KEYWORDS = {
    "romantic": ["romantic", "love", "cute", "crush"],
    "energetic": ["party", "dance", "energetic", "workout", "gym", "boost", "hype", "power", "fast", "beats"],
    "calm": ["calm", "relax", "peace", "peaceful", "soothing", "meditation", "melodious", "slow", "soft", "instrumental", "ambient", "chill"],
    "happy": ["happy", "joy", "cheerful", "positive", "feel good", "bright", "fun", "uplifting"],
    "sad": ["sad", "lonely", "depressed", "low", "heartbroken", "cry", "emotional", "blue"]
}

def detect_intent(transcript):
    transcript = transcript.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in transcript:
                return intent

    return None
