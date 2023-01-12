import os 
import argparse
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from PyPDF2 import PdfReader

def speak(text):
    tts = gTTS(text=text, lang=args.lang)
    filename="voice.mp3"
    tts.save(filename)

    print(":::: START OF FILE ::::")
    print(text)
    print(":::: END OF FILE ::::")

    playsound.playsound(filename)


# Initialize parser
parser = argparse.ArgumentParser(
    prog = 'PyText2Speech',
    description = 'Script to read a text file, create a voice audio from the reading and run it',
    epilog = 'End of help',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

# Adding optional arguments
parser.add_argument("filename", help = "File to be read")
parser.add_argument("-p", "--page", default=1, help = "Page to be read")
parser.add_argument("-l", "--lang", default="en", help = "Language to use on voicing. Usually the same of the file")

# Read arguments from command line
args = parser.parse_args()

# Read file contents if specified
if args.filename:
    reader = PdfReader(args.filename)

text = ""
# # for page in reader.pages:
# #     text += page.extract_text() + "\n"
text += reader.pages[args.page - 1].extract_text()

speak(text)
