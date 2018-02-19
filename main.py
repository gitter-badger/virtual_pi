import sys
import yaml
import speech_recognition as sr
from GreyMatter.SenseCells.tts import tts
profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close
from brain import brain

 
name = profile_data['name']
city_name = profile_data['city_name']

tts('Welcome ' + name + ' systems are now ready to run.  How can I help you?')

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something interesting if possible! ")
        audio = r.listen(source)
     
    try:
        speech_text =  r.recognize_google(audio).lower().replace("'","").strip()
        print ("I think you said '" + speech_text + "'")
        brain(name, speech_text) 
    except sr.UnknownValueError:
        print("Sorry I could not understand the audio message")
    
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service {0}".format(e))
        



main()    
