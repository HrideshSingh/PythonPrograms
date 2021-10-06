import speech_recognition as sr 
AUDIO_FILE=("Song.wav")
#use audio file as source

r=sr.Recognizer() #intialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file 

try :
    print("Audio file contains"+r.recognize_google(audio))
except sr.UnkownValueError :
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError :
    print("couldn't get the results from Google Speech Recognition")