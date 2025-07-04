import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Listening...")
        audio = recognizer.record(source)
        print("Transcribing...")
        try:
            text = recognizer.recognize_google(audio)
            print("Transcription:", text)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results:", e)

# Example usage
transcribe_audio(r"path to audio file")

