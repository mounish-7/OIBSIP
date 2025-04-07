# voice_assistant.py
'''Required speech_recognition and pyttsx3
install with:pip install
SpeechRecoginition pyttsx3'''
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."

def main():
    speak("Hello! How can I help you?")
    while True:
        command = listen_command()

        if "time" in command:
            speak("The current time is " + datetime.datetime.now().strftime("%I:%M %p"))
        elif "date" in command:
            speak("Today's date is " + datetime.datetime.now().strftime("%B %d, %Y"))
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't help with that yet.")

main()