from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Intent definitions (MEANING, not keywords)
INTENT_DESCRIPTIONS = {
    "happy": [
        "I feel happy and want upbeat music",
        "play something cheerful",
        "I want feel-good songs",
        "uplifting and positive music"
    ],
    "sad": [
        "I am feeling sad or low",
        "I had a bad day",
        "I feel lonely",
        "emotional and slow music"
    ],
    "energetic": [
        "I want energetic music",
        "play workout or gym songs",
        "party and dance music",
        "high energy fast beats"
    ],
    "calm": [
        "I want calm and peaceful music",
        "relaxing or soothing songs",
        "meditation or focus music",
        "soft and slow melodies"
    ],
    "romantic": [
        "romantic love songs",
        "music for crush or love",
        "soft romantic vibes"
    ],
    "uplift": [
        "cheer me up",
        "play something good",
        "make me feel better",
        "uplifting music after a bad day"
    ]
}

# Precompute embeddings
intent_embeddings = {
    intent: model.encode(sentences, convert_to_tensor=True)
    for intent, sentences in INTENT_DESCRIPTIONS.items()
}


def detect_intent(transcript: str):
    if not transcript or not transcript.strip():
        return None

    transcript = transcript.lower()

    # Encode user sentence
    query_embedding = model.encode(transcript, convert_to_tensor=True)

    best_intent = None
    best_score = 0.0

    # Compare with all intent meanings
    for intent, emb_list in intent_embeddings.items():
        similarity = util.cos_sim(query_embedding, emb_list).max().item()

        if similarity > best_score:
            best_score = similarity
            best_intent = intent

    # Threshold to avoid random matches
    if best_score < 0.45:
        return None

    return best_intent
