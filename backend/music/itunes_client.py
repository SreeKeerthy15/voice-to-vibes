import requests

def search_songs_by_emotion(emotion, limit=10):
    emotion_query_map = {
        "Happy": "happy upbeat pop",
        "Sad": "sad acoustic slow",
        "Angry": "rock metal workout",
        "Calm": "chill ambient lofi",
        "Neutral": "indie pop"
    }

    query = emotion_query_map.get(emotion, "pop")

    params = {
        "term": query,
        "media": "music",
        "limit": limit
    }

    response = requests.get("https://itunes.apple.com/search", params=params)
    response.raise_for_status()

    results = response.json().get("results", [])

    songs = []
    for item in results:
        preview = item.get("previewUrl")
        if preview:
            songs.append({
                "title": item.get("trackName", "Unknown"),
                "artist": item.get("artistName", "Unknown"),
                "preview_url": preview,
                "source_url": item.get("trackViewUrl", "")
            })

    return songs
