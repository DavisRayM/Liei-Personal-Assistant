"""
Main Liei Module
Contains the main loop for Liei
"""
from speech import speak  # pylint: disable=import-error
from recognition import listen  # pylint: disable=import-error


def main():
    """
    Main loop for Liei
    """
    saying = listen('Welcome to the Test Zone. What can i help you with ?')

    speech_array = saying.split(" ")

    # Lowercase the entire array
    words = [word.lower() for word in speech_array]

    if 'retry' in words:
        saying = listen('What else do you want me to do ?')
    if 'good' and 'bye' in words:
        speak('Goodbye User')

if __name__ == "__main__":
    main()
