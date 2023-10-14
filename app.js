from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    model = whisper.load_model("base")
    # ... rest of the processing code

    return jsonify({'text': result.text})

if __name__ == '__main__':
    app.run(debug=True)
