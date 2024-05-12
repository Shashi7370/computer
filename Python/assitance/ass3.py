import speech_recognition as sr
from gtts import gTTS
import os
from translate import Translator
from playsound import playsound

# Initialize the recognizer
recognizer = sr.Recognizer()
translator = Translator(to_lang='en')  # Set the target language to English

# Function to speak a given text in a specified language
def speak(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    #os.system("mpg321 output.mp3")  # You may need to adjust this command based on your OS and audio player
    playsound('output.mp3')

# Function to handle voice commands
def process_command(command, target_language='en'):
    try:
        translation = translator.translate(command)
        translated_command = translation

        if "hello" in translated_command:
            response = "Hello! How can I assist you?"
        elif "how are you" in translated_command:
            response = "I'm just a computer program, but I'm doing fine. How can I help you?"
        elif "what's the time" in translated_command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
        else:
            response = "I'm sorry, I don't understand that command."

        speak(response, lang=target_language)
    except Exception as e:
        print(f"Error: {e}")

# Main loop for listening to voice commands
while True:
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        process_command(command, target_language='en')  # You can change the target language here
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
    except sr.RequestError as e:
        print("Could not request results;{0}".format(e))