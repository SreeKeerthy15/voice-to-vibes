import whisper

model = whisper.load_model("small")

def speech_to_text(audio_path, preferred_language=None):
    options = {
        "task": "transcribe",
        "fp16": False,
        "condition_on_previous_text": False
    }

    if preferred_language == "Telugu":
        options["language"] = "te"
    elif preferred_language == "Hindi":
        options["language"] = "hi"
    elif preferred_language == "English":
        options["language"] = "en"

    result = model.transcribe(audio_path, **options)

    transcript = result["text"]
    detected_lang = result.get("language", "unknown")

    return transcript, detected_lang
