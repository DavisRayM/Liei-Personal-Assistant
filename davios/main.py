"""
Main Davios Module
Contains the main loop for Davios
"""
from davios.speech import speak
from davios.recognition import listen


def main():
    """
    Main loop for Davios
    """
    saying = listen('Welcome to the Test Zone. What can i help you with ?')

    print(saying)
    speak('You said. ' + saying)


if __name__ == "__main__":
    main()
