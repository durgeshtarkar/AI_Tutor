📘 AI Tutor – English Learning Assistant
An AI-powered English learning assistant built with Flask, Groq API, and gTTS. The app provides Urdu translations, pronunciation guides, grammar explanations, synonyms/antonyms, and text-to-speech audio for learners.

🚀 Features
🌐 Urdu translation + Roman Urdu

📖 Definitions with grammar explanations

🔄 Synonyms and antonyms

📝 Example sentences + corrections

🔊 Text-to-speech audio playback

🎨 Frontend served via Flask templates

🛠 Tech Stack
Backend: Python, Flask

AI Model: Groq (LLaMA 3.1)

Text-to-Speech: gTTS

Frontend: HTML, CSS, JS (served via Flask)

⚙️ Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/durgeshtarkar/AI_Tutor.git
cd AI_Tutor
2. Create Python Virtual Environment
bash
python -m venv myenv
Activate it:

Windows (PowerShell):

powershell
myenv\Scripts\Activate
Linux/Mac:

bash
source myenv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
(Make sure you have Flask, python-dotenv, groq, gTTS installed.)

▶️ Run the App
Start the Flask server:

bash
python app.py
The app will run at:

Code
http://127.0.0.1:5000/
