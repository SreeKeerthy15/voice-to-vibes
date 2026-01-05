import whisper

model = whisper.load_model("small")

LANG_MAP = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi"
}

def speech_to_text(audio_path, preferred_language="English"):
    """
    Converts speech to text using Whisper
    """
    lang_code = LANG_MAP.get(preferred_language, None)

    result = model.transcribe(
        audio_path,
        language=lang_code,     # force if known, else auto
        task="transcribe"
    )

    transcript = result["text"]
    detected_language = result["language"]

    return transcript, detected_language
