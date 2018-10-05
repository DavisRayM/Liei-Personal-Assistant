"""
Module Containing all Recognition Methods for Liei
"""
import speech_recognition as sr

from speech import speak  # pylint: disable=import-error


def listen(prompt: str):
    """
    Method that listens to Microphone on Computer
    and returns what the speaker said
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak(prompt)
        audio = r.listen(source, timeout=5.0)

    translation = recognize_speech(audio)

    if translation is None:
        listen(prompt)
    else:
        return translation


def recognize_speech(audio):
    """
    Method that takes in an audio file and tries
    to recognize what the speaker has said
    """
    r = sr.Recognizer()

    try:
        translation = r.recognize_sphinx(audio)
        return translation
    except sr.UnknownValueError:
        speak("I did not quite get what you said.... Can you say that again ?")
        return None
    except sr.RequestError as e:
        print(f'Error: {e}')
        speak("Error Occurred. Please Say That Again.")
        return None
