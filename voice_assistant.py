import speech_recognition as sr
import pyttsx3 as pt
import wikipedia
import datetime as dt

def speak(audio):
    engine = pt.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1])
    engine.say(audio)
    engine.runAndWait()

def tell_me():
    hr = int(dt.datetime.now().hour)
    if hr>=0 and hr<=12:
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
        query = rec.recognize_google(audio)
        print("You said: ",query)
        if 'stop the program' in query:
            print("Ending the program")
            exit()
        
    except sr.UnknownValueError:
        # print("Sorry could not understand the audio!")
        speak("Sorry could not understand the audio! say it again please!")
        # return None
    except sr.RequestError as e:
        print("Couldn't request results! sorry ,{0}", e)
        return None
    return query


if __name__ == '__main__':
    tell_me()
    speak("I'm your voice assistant Jarvis, how can I help U?")
    while True:
        qry = take_cmd().lower()
        if 'what\'s the time' in qry:
            time = dt.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir the time is {time}")
        elif 'wikipedia' in qry:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query) 
            speak("According to Wikipedia")
            print(results)
            speak(results)



