# tts
from gtts import gTTS
from time import sleep
import os
import pyglet.media


def output_tts(text):

    tts = gTTS(text=text, tld="ca", lang="en", slow=False, lang_check=False)

    filename = "voice.mp3"
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()
    
    os.remove(filename)  # remove temperory file

def tts_default():
    #copy pasted 100%
    # The text that you want to convert to audio
    mytext = "hello there i am diganta"

    # Passing the text and language to the engine,

    tts = gTTS(text=mytext, tld="ca", lang="en", slow=False, lang_check=False)

    filename = "temp.mp3"
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()

    sleep(audio.duration)  # prevent from killing
    os.remove(filename)  # remove temperory file
