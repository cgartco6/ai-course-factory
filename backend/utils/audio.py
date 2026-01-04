import pyttsx3
from pathlib import Path
from utils.audio import text_to_audio

def lesson_to_audio(text):
    Path("media/audio").mkdir(parents=True, exist_ok=True)
    text_to_audio(text, "media/audio/lesson1.mp3")

def text_to_audio(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
