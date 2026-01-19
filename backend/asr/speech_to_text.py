import whisper

# Load Whisper model once
model = whisper.load_model("small")

def speech_to_text(audio_path, preferred_language="English"):
    """
    Returns:
    {
        original_text: text in spoken language,
        translated_text: English translation,
        language: EN / HI / TE
    }
    """

    # ---------- HINDI ----------
    if preferred_language == "Hindi":
        # Transcribe Hindi (NO translation)
        hi_transcribe = model.transcribe(
            audio_path,
            language="hi",
            task="transcribe"
        )

        # Translate Hindi → English
        hi_translate = model.transcribe(
            audio_path,
            language="hi",
            task="translate"
        )

        return {
            "original_text": hi_transcribe.get("text", "").strip(),
            "translated_text": hi_translate.get("text", "").strip(),
            "language": "HI"
        }

    # ---------- TELUGU ----------
    elif preferred_language == "Telugu":
        # Transcribe Telugu (NO translation)
        te_transcribe = model.transcribe(
            audio_path,
            language="te",
            task="transcribe"
        )

        # Translate Telugu → English
        te_translate = model.transcribe(
            audio_path,
            language="te",
            task="translate"
        )

        return {
            "original_text": te_transcribe.get("text", "").strip(),
            "translated_text": te_translate.get("text", "").strip(),
            "language": "TE"
        }

    # ---------- ENGLISH (default) ----------
    else:
        en_result = model.transcribe(
            audio_path,
            language="en",
            task="transcribe"
        )

        text = en_result.get("text", "").strip()

        return {
            "original_text": text,
            "translated_text": text,
            "language": "EN"
        }
