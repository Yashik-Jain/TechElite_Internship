# 🗣️ Basic Speech-to-Text System using SpeechRecognition

This project is a simple implementation of a **Speech-to-Text system** using the `SpeechRecognition` library and Google Web Speech API. It transcribes short `.wav` audio files into readable text.

---

## 📌 Task Description

**Task:** Build a basic Speech-to-Text system using pre-trained models and libraries like `SpeechRecognition` or `Wav2Vec`.  
**Deliverable:** A Python script capable of transcribing short audio clips.

---

## ✅ Features

- 🎧 Accepts `.wav` audio files
- 🔁 Transcribes speech into text using Google’s Web Speech API
- 🔍 Handles common errors (like unrecognizable audio or connection issues)
- 🧠 Lightweight, fast, and easy to use

---

## 📁 Project Structure<br/>

speech_to_text/<br/>
│<br/>
├── app.py # Main Python script<br/>
├── sample.wav # Example audio file<br/>
├── requirements.txt # Python dependencies<br/>
└── README.md # Project documentation<br/>

---

## ⚙️ Setup Instructions

Follow these steps to set up the project and run the transcription tool:

### 1️⃣ Create a Virtual Environment

```bash
python -m venv stt_env
```
### 2️⃣ Activate the Environment
On Windows:
```
stt_env\Scripts\activate
```
On macOS/Linux:
```
source stt_env/bin/activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
## ▶️ How to Run the Script
Replace the file path in app.py with your own .wav file:<br/>
```
transcribe_audio(r"sample.wav")
```
## Run the script:
```
python app.py
```
Example Output:<br/>

Listening...<br/>
Transcribing...<br/>
Transcription: This is a sample transcription.<br/>
