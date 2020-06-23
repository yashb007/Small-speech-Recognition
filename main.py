import speech_recognition as sr 
import time
import webbrowser
import os
import playsound
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
	with sr.Microphone() as source:
		if ask:
			 alexis_speak(ask)
		audio = r.listen(source)
		voice_data=''
		try:
			voice_data = r.recognize_google(audio)
			alexis_speak(voice_data)
		except sr.UnknownValueError:
			alexis_speak('Sorry, I didnot get that')
		except sr.RequestError:
			alexis_speak("Sorry , my service is down")	

		return voice_data	

def alexis_speak(audio_string):
		tts = gTTS(text = audio_string, lang='en')
	    r=random.randint(1,1000000)
	    audio_file = 'audio-' + str(r) + '.mp3' 
	    tts.save(audio_file)
	    playsound.playsound(audio_file)
	    print(audio_string)
	    os.remove(audio_file)


def respond(voice_data):
	if 'what is your name' in voice_data:
		alexis_speak('My name is Panda')
	if 'what time is it' in voice_data:
		alexis_speak(ctime())	
	if 'search' in voice_data:
		search = record_audio('what do you want to search')
		url = 'https://google.com/search?q='+search
		webbrowser.get().open(url)
		alexis_speak('Here is what i found for ' + search )
	if 'find location' in voice_data:
		location = record_audio('what is the location You want to search')
		url = 'https://google.nl/maps/place/'+location + '/&amp;'
		webbrowser.get().open(url)
		alexis_speak('Here is the location for ' + location )	
	if 'exit' in voice_data:
		exit()	


time.sleep(1)
print('How can I help You?')
while 1:
	voice_data = record_audio()
	respond(voice_data)