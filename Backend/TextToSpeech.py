import pyttsx3

def text_to_speech(text):
    """
    Convert text to speech using pyttsx3.

    Args:
        text (str): The text to convert to speech.

    Returns:
        None
    """
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'Microsoft Zira Desktop' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 100)  # Set speech rate to slow and deep
    engine.setProperty('volume', 2.0)  # Set volume to maximum
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        text = input("Enter the text : ")
        if text.lower() == 'exit':
            break
        text_to_speech(text)

if __name__ == "__main__":
    main()