from flask import Flask, render_template, request
from langdetect import detect,detect_langs
from googletrans import Translator, constants
from googletrans import LANGUAGES
from werkzeug.utils import secure_filename
from gtts import gTTS
import os
import openai
import codecs
from pprint import pprint

app = Flask(__name__)

openai.api_key = "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"

language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Marathi": "mr",
    "Afrikaans": "af",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Belarusian": "be",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese": "zh",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "Finnish": "fi",
    "Galician": "gl",
    "German": "de",
    "Greek": "el",
    "Hebrew": "he",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malay": "ms",
    "Maori": "mi",
    "Nepali": "ne",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog": "tl",
    "Tamil": "ta",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy",
    
}
          

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "transcribe" in request.form:
            return render_template("transcribe.html")
        elif "translate" in request.form:
            return render_template("translate.html")
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["file"]
    if audio_file.filename.split(".")[-1] not in [
        "flac",
        "m4a",
        "mp3",
        "mp4",
        "mpeg",
        "mpga",
        "oga",
        "ogg",
        "wav",
        "webm",
    ]:
        return "Invalid file format. Supported formats: flac, m4a, mp3, mp4, mpeg, mpga, oga, ogg, wav, webm"

    filename = secure_filename(audio_file.filename)  # Secure the filename before saving
    audio_file.save(filename)
    with open(filename, "rb") as audio:
        transcript = openai.Audio.transcribe("whisper-1", audio)
        if isinstance(transcript, dict) and "text" in transcript:
            decoded_text = transcript["text"]
            try:
                detected_language_code = detect_langs(decoded_text)[0].lang
                detected_language = LANGUAGES.get(detected_language_code, "Unknown")
                detected_language = detected_language.capitalize()
            except IndexError:
                detected_language = "Unknown Language"
            print("Detected language:", detected_language)
            print("Decoded Text:", decoded_text)
            return render_template("transcribe.html", decoded_text=decoded_text, detected_language=detected_language)

        elif decoded_text is not None:  # Check if the transcript exists
            return decoded_text

        else:
            print("Transcription not found or incorrect format.")
    # return render_template("tra.html")



@app.route("/translate", methods=["GET", "POST"])
def translate_audio():
    if request.method == "POST":
        audio_file = request.files["file"]
        if audio_file.filename.split(".")[-1] not in [
            "flac",
            "m4a",
            "mp3",
            "mp4",
            "mpeg",
            "mpga",
            "oga",
            "ogg",
            "wav",
            "webm",
        ]:
            return "Invalid file format. Supported formats: flac, m4a, mp3, mp4, mpeg, mpga, oga, ogg, wav, webm"

        filename = secure_filename(audio_file.filename)
        audio_file.save(filename)

        with open(filename, "rb") as audio:
                selected_language = request.form.get("language")
                print(f"Selected Language: {selected_language}")

            # try:
                response = openai.Audio.transcribe("whisper-1", audio)
                if isinstance(response, dict) and "text" in response:
                    decoded_text = response["text"]
                    try:
                        detected_language_code = detect_langs(decoded_text)[0].lang
                        detected_language = LANGUAGES.get(detected_language_code, "Unknown")
                        detected_language = detected_language.capitalize()
                    except IndexError:
                        detected_language = "Unknown Language"
                    translator = Translator()
                    translated_text = translator.translate(decoded_text, dest=selected_language).text
                    print("Detected language:", detected_language)
                    print("Decoded Text:", decoded_text)
                    return render_template("translate.html", decoded_text=translated_text, detected_language=detected_language)

                else:
                    return "Transcription failed or returned no data."

            # except openai.error.OpenAIError as e:
            #     return f"OpenAI API error: {str(e)}"
            # except Exception as e:
            #     return f"Error: {str(e)}"

                if selected_language not in language_codes.keys():
                    return "Invalid language selected."



if __name__ == "__main__":
    app.run(debug=True)
