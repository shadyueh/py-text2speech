import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from PyPDF2 import PdfReader

lang = "en"

PAGE = 1

def speak(text):
    tts = gTTS(text=text, lang=lang)
    filename="voice.mp3"
    tts.save(filename)
    
    print(":::: START OF FILE ::::")
    print(text)
    print(":::: END OF FILE ::::")

    playsound.playsound(filename)


reader = PdfReader("The Sore Feet Song by Ally Kerr (Mushishi Opening).pdf")

text = ""
# for page in reader.pages:
#     text += page.extract_text() + "\n"
text += reader.pages[PAGE - 1].extract_text()

speak(text)
