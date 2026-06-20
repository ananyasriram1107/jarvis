import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 220)  # Adjust the speech rate (optional)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
def voice_input():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source,timeout = 5,phrase_time_limit=15)
            # the phrase limit is how much continous speaking you can do
            text = recognizer.recognize_google(audio)
            return text.lower()
    except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
        return None
    