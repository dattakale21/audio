from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route("/transcribe-and-translate", methods=["POST"])
def transcribe_and_translate():
    try:
        target_language = request.form["targetLanguage"]
        audio_file = request.files["audioFile"]

        # Transcribe the audio file using OpenAI GPT-3
        with open("audio.mp3", "wb") as file:
            file.write(audio_file.read())

        with open("audio.mp3", "rb") as file:
            response = openai.Completion.create(
                engine="davinci",
                audio=file,
                prompt="Transcribe the following audio:",
                max_tokens=200
            )

        # Extract the transcription from the response
        transcription_result = response.choices[0].text.strip()

        return jsonify({
            "transcriptionResult": transcription_result,
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)


#  "express": "^4.18.2",
#     "multer": "^1.4.5-lts.1",
#     "openai": "^4.12.0",
#     "whisper"