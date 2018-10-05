"""
Module Containing all Speech Methods for Liei
"""
import os

from gtts import gTTS


def speak(message: str):
    """
    Method that outputs a message through the System
    Microphone
    """
    tts = gTTS(message)
    tts.save("speech.mp3")
    os.system("mpg321 -q speech.mp3")
    os.remove("speech.mp3")
