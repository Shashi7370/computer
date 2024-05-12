import speech_recognition as sr
from gtts import gTTS
import os
from translate import Translator
from playsound import playsound

# Initialize the recognizer
recognizer = sr.Recognizer()
translator_to_hindi = Translator(to_lang='hi')  # Set the target language to Hindi ('hi')
translator_to_english = Translator(to_lang='en')  # Set the target language to English ('en')

# Function to speak a given text in a specified language
def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    #os.system("mpg321 output.mp3")  # You may need to adjust this command based on your OS and audio player
    playsound('output.mp3')

# Function to handle voice commands
def process_command(command, target_language='hi'):  # Set the target language to Hindi ('hi')
    try:
        translation = translator_to_english.translate(command)
        translated_command = translation

        if "hello" in translated_command:
            response = "Hello! How can I assist you?"
        elif "how are you" in translated_command:
            response = "I'm just a computer program, but I'm doing fine. How can I help you?"
        elif "what's the time" in translated_command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
        elif "open camera" in translated_command:
            codepath="C:\\Users\\shash\\Desktop\\camera"
            os.startfile(codepath)
        else:
            response = "I'm sorry, I don't understand that command."

        # Translate the response to Hindi for speaking
        translated_response = translator_to_hindi.translate(response)
        speak(translated_response, lang=target_language)
    except Exception as e:
        print(f"Error: {e}")

# Main loop for listening to voice commands
while True:
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-IN')  # Recognize Hindi commands
        command = translator_to_english.translate(command)
        print("You said (in Hindi): " + command)        
        process_command(command, target_language='en')  # Set the target language to Hindi ('hi')
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
    except sr.RequestError as e:
        print("Could not request results;{0}".format(e))