import speech_recognition as sr
import pyttsx3 as pt
import wikipedia, webbrowser
import datetime as dt

def speak(audio):
    engine = pt.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1])
    engine.say(audio)
    engine.runAndWait()

def tell_me():
    hr = int(dt.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning")
    elif hr>=12 and hr<=18:
        speak("Good Afternoon")
    else:
        speak("Good Night")

def take_cmd():
    rec = sr.Recognizer()
    with sr.Microphone() as main:
        print("Say something...!")
        rec.pause_threshold = 0.5
        audio = rec.listen(main)
    
    try:
        query = rec.recognize_google(audio).lower()
        print("You said: ",query)
        if 'hey jarvis' in query:
            speak('Hello, how can i help u?')
        elif 'how are you' in query:
            speak('Im doing well thank you!')
        elif 'end program' in query:
            speak('good bye,see you soon!')
            exit()
        return query
    except sr.UnknownValueError:
        speak("Sorry I couldn't understand your voice!")
        return None

def search_wiki(command):
    try:
        result = wikipedia.summary(command, sentences=2)
        return result
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found. Please try a different query. {e}")
        return None

def main():
    command = take_cmd()
    if command:
        wiki_cmd = search_wiki(command)
        if wiki_cmd:
            speak(wiki_cmd)
            print(wiki_cmd)

if __name__ == '__main__':
    tell_me()
    speak("I'm your voice assistant Jarvis, how can I assist U?")
    while True:
        main()
        qry = take_cmd()
        if 'The time' in qry.lower():
            time = dt.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir the time is {time}")
        elif 'open google' in qry.lower():
            webbrowser.open('google.com')
