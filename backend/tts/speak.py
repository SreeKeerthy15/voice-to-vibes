from gtts import gTTS
import os

LANG_MAP = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi"
}

def speak_response(text, language):
    lang_code = LANG_MAP.get(language, "en")

    tts = gTTS(text=text, lang=lang_code)
    output_file = "audio/response.mp3"
    tts.save(output_file)

    return output_file
