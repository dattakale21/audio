from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator
from werkzeug.utils import secure_filename
from gtts import gTTS
import os
import openai

app = Flask(__name__)

openai.api_key = "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"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["GET", "POST"])
def transcribe_audio():
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

        filename = secure_filename(audio_file.filename)  # Secure the filename before saving
        audio_file.save(filename)
        with open(filename, "rb") as audio:
            selected_language = request.form.get("language")
            transcript = openai.Audio.translate("whisper-1", audio, target_language=selected_language)

            # Convert the transcript to a string
            transcript = str(transcript)

            # Perform language detection on the string format of the transcript
            detected_language = detect(transcript)

            # Further processing or rendering logic
            parsed_transcript = transcript  # Set as the parsed transcript
            parsed_transcript = (
                parsed_transcript.replace(' , "text": "', "").replace('" ,', "")
            )  # Parsing the transcript text
            return render_template(
                "transcript.html",
                transcript=parsed_transcript,
                detected_language=detected_language,
                audio_language=detected_language,
            )



@app.route("/listen", methods=["GET", "POST"])
def listen_transcript():
    if request.method == "POST":
        transcript = request.form["transcript"]
        tts = gTTS(transcript)
        tts.save("transcript.mp3")
        os.system("start transcript.mp3")
        return "Playing the transcript..."


if __name__ == "__main__":
    app.run(debug=True)
