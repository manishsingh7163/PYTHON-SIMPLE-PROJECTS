import speech_recognition as sr
sr.__version__

audio_file = ("harvard.wav")
r=sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    
try :
    print("audio file contains \n" + r.recognize_google(audio))
    
except sr.UnknownValueError:
    print("Google speech Recognition could not understand audio")

except sr.RequestError:
    print("couldn't get the results from google speech recognition")
    
    
