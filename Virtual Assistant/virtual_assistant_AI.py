import pyttsx3 # Text to speech 
import speech_recognition as sr # Speech recognizer
import pyaudio ## Library to enable audio
import datetime ## Library to retrieve date and time
import os 
import random
from requests import get
import wikipedia ## Library to search wikipedia
import webbrowser ## Library to open webbrowser
import pywhatkit as kit ## Library to send whatsapp text
import sys
import pyjokes ## Library to get random jokes

engine = pyttsx3.init('sapi5') ## Setting sapi5 as engine there are other which you can look for in documentation
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) ## Setting voice-1 (Female voice)
rate = engine.getProperty('rate') 
engine.setProperty('rate', 200) ## Setting the voice speed

def speak(audio): ## Defining function speak
    engine.say(audio) ## This line enables the engine to speak out the audio
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour) ##Retrieving Time(hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    elif hour>18 and hour<=20:
        speak("Good Evening")
    else:
        speak("Hello")
    speak("I am Kiara, How may I help you.")   


def recognize():
    r = sr.Recognizer() 
    with sr.Microphone() as source: ## Speech reccognition takes input from microphone
        print("Listening...")
        r.pause_threshold = 1 ## Pause for a second
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Recognized:{query}\n")

    except Exception as e: ##If the audio was not heard properly
        speak("Sorry I did not get you...")
        return "none"
    return query

if __name__ == "__main__":
    greet() 
    while True:
        query = recognize().lower() ## Turn the recognised audiotext to lowercase
        if "time" in query: ## If the query has "time" in it then read out time
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)

        elif "date" in query: ## If the query has "date" in it then read out date
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            date = datetime.datetime.now().day
            speak(f"Today's date is {date} {month} {year}")
            
        elif "chrome" in query: ## If the query has "chrome" in it then open chrome
            loc = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(loc)

        elif "movie" in query: ## If the audiotext has "movie" in it then open movies folder and play random movie
            movie_dir = r" " ## Give path of your movies folder here
            movie = os.listdir(movie_dir) ## Movie directory
            rd = random.choice(movie) ## Play random movie from the directory
            os.startfile(os.path.join(movie_dir, rd)) 
        
        elif "ip address" in query: ## If the query has "ip address" in it then read IP address
            ip = get('https://api.ipify.org').text ## Using API to get IP of computer
            speak(f"Your IP Adress is {ip}")
        
        elif "wikipedia" in query: ## If the query has "wikipedia" in it  
            speak("Looking into Wikipedia...")
            query = query.replace("wikipedia", "") ## Removing "wikipedia" from the query and keeping the rest to search for it 
            res = wikipedia.summary(query, sentences=2) ## Search wikipedia for the query and read out only 2 sentences
            speak("According to Wikipedia")
            speak(res)
            print(res)
        
        elif "open youtube" in query: ## If the query has "youtube" in it then open youtube website
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open netflix" in query:
            webbrowser.open("www.netflix.com")
        
        elif "open amazon" in query:
            webbrowser.open("www.amazon.in")

        #elif "whatsapp" in query:
            #kit.sendwhatmsg("NUMBER", "TEXT",2,25) ## Give number and text you have to send

        elif "play music" in query: 
            speak("Which song do you like listen")
            cm = recognize().lower()
            kit.playonyt(f"{cm}") ## Using pywhatkit and play the youtube video of the given query

        elif "search on google" in query:
            speak("What may I help you to find")
            lis = recognize().lower()
            kit.search(f"{lis}")

        elif "favourite song" in query:
            kit.playonyt("") ## Give link of you fav song here

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "take note" in query:
            speak("What should I write down")
            memory = recognize().lower()
            speak("Noted")
            note = open("note.txt", "w") ## Opening a note.txt file to note down the query
            note.write(memory)
            note.close()

        elif "remind me" in query:
            note = open("note.txt", "r") ## Opens the note.txt and reads out the text 
            speak("You asked me to remember that" +note.read())        

        elif "no thanks" in query: ## Exit the AI
            speak("Have a Nice Day")
            sys.exit()

        elif "shutdown the system" in query: ## To shutdown system
            os.system("shutdown /s /t 5")

        elif "restart the system" in query: ## To restart system
            os.system("shutdown /r /t 5")

        speak("May I help you with anything else")
