import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_file
from groq import Groq
from gtts import gTTS

# Load environment variables
load_dotenv()

# Groq FREE API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq Client
client = Groq(api_key=GROQ_API_KEY)

# ------------------------------
# FLASK CONFIG (SERVE FRONTEND)
# ------------------------------
app = Flask(
    __name__,
    static_folder="../frontend/static",
    template_folder="../frontend/templates"
)

# Ensure audio folder exists
AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# ------------------------------
#   HOME ROUTE (SERVE FRONTEND)
# ------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# ------------------------------
#   AI PROCESSING FUNCTION
# ------------------------------
def process_text_with_model(text):
    prompt = f"""
You are an English language learning assistant. Provide:

1. Urdu translation
2. Pronunciation guide
3. Definition + Urdu meaning
4. Synonyms + antonyms
5. Example sentence
6. Grammar explanation
7. Corrections (if any)
8. Roman Urdu translation

Input: {text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # FREE GROQ MODEL
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ ERROR: {str(e)}"


# ------------------------------
#   TEXT TO SPEECH
# ------------------------------
def text_to_speech(text):
    clean = text.replace("*", "").replace("#", "")
    tts = gTTS(text=clean, lang='en')

    # Unique filename
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join(AUDIO_FOLDER, filename)

    tts.save(audio_path)
    return filename  # return just the filename


# ------------------------------
#   ROUTES (API)
# ------------------------------
@app.route("/process", methods=["POST"])
def process():
    data = request.json
    user_text = data.get("text", "")

    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    ai_response = process_text_with_model(user_text)
    return jsonify({"response": ai_response})


@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    filename = text_to_speech(text)
    # Return a URL the frontend can fetch
    return jsonify({"audio": f"/audio/{filename}"})


@app.route("/audio/<filename>")
def get_audio(filename):
    audio_path = os.path.join(AUDIO_FOLDER, filename)
    return send_file(audio_path, mimetype="audio/mpeg")


# ------------------------------
#   START SERVER
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
