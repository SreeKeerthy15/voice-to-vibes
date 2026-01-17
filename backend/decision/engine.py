

def decide_music_category(intent, emotion, user_choice):
    # Highest priority: explicit intent
    if intent:
        return intent.capitalize()

    # Second priority: uplift choice
    if user_choice == "Uplift me":
        return "Happy"
    
    if user_choice == "Match my mood":
        return emotion


    # Default: match emotion
    return emotion
