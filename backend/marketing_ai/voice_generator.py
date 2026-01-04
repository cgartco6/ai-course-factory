import pyttsx3

def generate_voice(text, output="media/audio/voice.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output)
    engine.runAndWait()
    return output
