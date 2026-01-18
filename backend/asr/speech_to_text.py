import whisper

model = whisper.load_model("small")

def speech_to_text(audio_path, preferred_language="English"):
    if preferred_language == "Hindi":
        # 1️⃣ Transcribe Hindi ONLY
        hindi_result = model.transcribe(
            audio_path,
            language="hi",
            task="transcribe"   # 🚨 NO translation here
        )
        hindi_text = hindi_result.get("text", "").strip()

        # 2️⃣ Translate Hindi → English
        english_result = model.transcribe(
            audio_path,
            language="hi",
            task="translate"
        )
        english_text = english_result.get("text", "").strip()

        return {
            "original_text": hindi_text,
            "translated_text": english_text,
            "language": "HI"
        }

    else:
        # English path
        result = model.transcribe(
            audio_path,
            language="en",
            task="transcribe"
        )
        text = result.get("text", "").strip()

        return {
            "original_text": text,
            "translated_text": text,
            "language": "EN"
        }
