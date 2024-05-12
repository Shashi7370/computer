import os

import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday Sir. Please tell me how can i help you")

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
#while True:
    if 1:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H %M")
            speak(f"sir, the time is{strTime}")
        elif "open sublime text" in query:
            codepath="C:\\Program Files\\Sublime Text\\sublime_text.exe"
            os.startfile(codepath)

        elif "open camera" in query:
            codepath="C:\\Users\\shash\\Desktop\\camera"
            os.startfile(codepath)