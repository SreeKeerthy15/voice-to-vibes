import random

# Dummy safe song database
SONG_DB = {
    "Happy": [
        {"title": "Happy Vibes", "artist": "Artist A"},
        {"title": "Sunshine Mood", "artist": "Artist B"}
    ],
    "Sad": [
        {"title": "Blue Nights", "artist": "Artist C"},
        {"title": "Silent Tears", "artist": "Artist D"}
    ],
    "Angry": [
        {"title": "Fire Mode", "artist": "Artist E"},
        {"title": "Rage Beats", "artist": "Artist F"}
    ],
    "Calm": [
        {"title": "Peaceful Flow", "artist": "Artist G"},
        {"title": "Soft Waves", "artist": "Artist H"}
    ],
    "Neutral": [
        {"title": "Easy Listening", "artist": "Artist I"},
        {"title": "Daily Chill", "artist": "Artist J"}
    ]
}

def recommend_songs(category):
    songs = SONG_DB.get(category, SONG_DB["Neutral"])
    return random.sample(songs, min(2, len(songs)))
