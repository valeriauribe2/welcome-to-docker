from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

# Load Whisper model
model = whisper.load_model("base")

@app.route("/")
def home():
    return "Welcome to the OpenWebUI for transcription!"

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["audio"]
    audio_path = "./uploaded_audio.wav"
    file.save(audio_path)

    # Transcribe the audio
    result = model.transcribe(audio_path)
    return jsonify({"transcription": result["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)