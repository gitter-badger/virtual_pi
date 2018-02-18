# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#stt

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something interesting if possible! ")
    audio = r.listen(source)
    
with open ("recording.wave", "wb") as f:
    f.write(audio.get_wav_data())   
    

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    
except sr.RequestError:
    print("Could not requeset results from Google Speech Recognition service {0}".format(e))


#tts    
import os
import sys

def tts(message):
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + ' "')
    
#sudo apt-get install espeak        
tts(r.recognize_google(audio))    
    

    
            
    
    