import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import sys



engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices[0].id)
#engine.say("Hello World")
#engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour< 12:
        speak("Good Morning")
    elif hour >=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis, Please tell me how I can help you")


def takeCommand():
    '''
    It takes microphone input from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source,timeout=3)
    
    try:
        print("Recognizng")
        query = r.recognize_google(audio)
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        return 'None'

    return query


if __name__ == '__main__':
    wishMe()
    
    while True:
        query = takeCommand().lower()
        print(query)
        if 'wikipedia' in query:
            print("Yeah")
            speak("Searching Wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=1)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open gmail" in query:
            webbrowser.open("gmail.com")
        elif "play music" in query:
            music_dir = "/home/ashwani/Music/"
            songs = os.listdir(music_dir)
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            cmd = "vlc "+music_dir+songs[0]
            os.system(cmd)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'visual studio' in query:
            os.system('code')
        

            
            




        

