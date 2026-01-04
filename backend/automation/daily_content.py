from backend.marketing_ai.poster_generator import create_poster
from backend.marketing_ai.voice_generator import generate_voice
from backend.marketing_ai.shorts_generator import generate_short_script

def run_daily(topic):
    poster = create_poster(topic)
    voice = generate_voice(topic)
    script = generate_short_script(topic)

    return {
        "poster": poster,
        "voice": voice,
        "script": script
    }
