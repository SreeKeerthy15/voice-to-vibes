INTENT_KEYWORDS = {
    "romantic": ["romantic", "love", "cute", "crush"],
    "energetic": ["party", "dance", "energetic", "workout"],
    "calm": ["calm", "relax", "peace", "meditation"],
    "happy": ["happy", "joy", "cheerful"],
    "sad": ["sad", "lonely", "depressed"]
}

def detect_intent(transcript):
    transcript = transcript.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in transcript:
                return intent

    return None
