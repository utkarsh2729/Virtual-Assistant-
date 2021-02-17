import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Zaara, How can I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        # speak("Sorry! didn't get that,Please repeat...")
          
    try:
       print("Recognizing....")
       query = r.recognize_google(audio, language = 'en-in')
       print("You Said:",query)
    
    except Exception as e:
       # print(e)
        # print("Sorry! didn't get that , Please repeat...")
       
        return "None"
    return query
     
if __name__ == '__main__':
    wishMe()
    while True:
      query = takeCommand().lower()
     
      if 'wikipedia' in query:
          speak("Searching.....")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences = 2)
          speak("According to wikipedia")
          print(results)
          speak(results)
        
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
          
      elif 'open google' in query:
          webbrowser.open("google.com")
          
      elif 'open instagram' in query:
          webbrowser.open("instagram.com")
          
      elif 'open quora' in query:
          webbrowser.open("quora.com")
          
      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")
          
      
      elif 'open vs code' in query:
          codepath = "C:\\Users\\UTKARSH KUSHWAHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)
          
      elif 'open intellij' in query:
          code_path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.3.2\\bin\\idea64.exe"
          os.startfile(code_path)
          
          
      elif 'open download' in query:
          dpath = "Downloads"
          os.startfile(dpath)
          
      elif 'stop' in query:
          speak("Thank you, Bye Bye")
          exit()
          