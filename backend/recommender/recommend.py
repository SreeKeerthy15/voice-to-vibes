from backend.music.itunes_client import search_songs_by_emotion

def recommend_songs(category):
    return search_songs_by_emotion(category)
