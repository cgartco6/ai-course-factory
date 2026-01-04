import pyttsx3

class VoiceAgent:
    def generate(self, text, filename):
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
