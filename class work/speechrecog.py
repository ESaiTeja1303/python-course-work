#pip install pyttsx3 SpeechRecognition pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

#Function to listen to user's voice
def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
        try:
            command =recognizer.recognize_google(audio,language='en-in')
            print(" you said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print(" Sorry, i didn't understand. ")
            speak("sorry, i didn't catch that.")
            return ""
        except sr.RequestError:
            print("Speech Service error.")
            speak("Sorry, my speech service is down.")
            return ""

#function to respond to voice commands

def run_assistant():
    speak("Hello! I'm your virtual assistant, How can i help you?")
    while True:
        command=listen()

        if 'time' in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif 'date' in command:
            today=datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'your name' in command:
            speak("I am your python assistant!")
        
        elif 'python' in command or 'java' in command or 'c' in command or 'sea' in command or 'see' in command:
            speak("Okay bye bye! Have a good day")
            break
        else:
            speak("Sorry, I can't do that yet.")

#Run the assistant
run_assistant()