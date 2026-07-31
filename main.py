import speech_recognition as sr
import webbrowser       #built-in module so no need to install it...
import pyttsx3         #pyttsx3 is a Python library used for Text-to-Speech (TTS)....
import musicLibrary
import requests             
import pyjokes
from google import genai
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init

init(autoreset=True)

recog = sr.Recognizer()     # Recognizer is a class jo help krti h speech recogniztion functionality lene m mdd krti h..
engine = pyttsx3.init()      # will cretae and initialize a text to speech engine and store it in ttsx....
#init() is a function provided by the pyttsx3 library.It creates and starts a new speech engine.This engine is responsible for speaking text.
voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(Fore.BLUE + f"{i} | {voice.name} | {voice.id}")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
news_api = "15110dbccbd14ac4859845042262affe"
load_dotenv()

api_key = os.getenv("API_KEY_")

client = genai.Client(api_key=api_key)


def speak(text):
    

    engine.stop()
    engine.say(text)
    engine.runAndWait()

def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=question
        )
        return response.text

    except Exception as e:
        print(e)
        return "Sorry, I am unable to answer right now."    

        
def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://www.google.com")
   elif"open instagram" in c.lower():
      webbrowser.open("https://www.instagram.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com")
   elif"open spotify" in c.lower():
      webbrowser.open("https://www.spotify.com")    
   elif"open linkedin" in c.lower():
      webbrowser.open("https://www.linkedin.com") 
   elif c.lower().startswith("play"):
     song = c.lower().split(" ")[1]
     link = musicLibrary.music[song]   
     webbrowser.open(link) 
   elif "news" in c.lower():
      # r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
      r = requests.get(
    f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey={news_api}"
)
      if r.status_code == 200 :
         data = r.json()    # parse the jason response...
         print(Fore.WHITE + str(data))
         articles = data.get('articles',[])
         for article in articles:
            speak(article['title'])

   elif "joke" in c.lower():
     joke = pyjokes.get_joke()
     print(Fore.LIGHTMAGENTA_EX + joke)
     speak(joke)

   elif"exit" in c.lower() or "bye" in c.lower():
     speak("Goodbye")
     exit()

   else:
    reply = ask_ai(c)
    print(Fore.CYAN + Style.BRIGHT + f"\n🤖 Sugar:\n{reply}\n")
    speak(reply)
   


if __name__ == "__main__":
    speak("  Initializing sugar....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print(Fore.LIGHTGREEN_EX + "🎤 Recognizing...")
        try:
            with sr.Microphone() as source:
                print(Fore.GREEN + "🎧 Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if "sugar" in word.lower():
                print(Fore.YELLOW + "Before Speak")
                speak("Ya")
                print(Fore.LIGHTYELLOW_EX + "After Speak")
                # Listen for command
                with sr.Microphone() as source:
                    print(Fore.RED + "🤖 Sugar Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(Fore.MAGENTA + f"🗣️ Command: {command}")

                    processCommand(command)
     
        except Exception as e:
          print(Fore.LIGHTRED_EX + f"❌ Error: {e}")
