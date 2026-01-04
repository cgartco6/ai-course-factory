def generate_video(script, voice, music):
    return {
        "resolution": "4K",
        "format": "mp4",
        "layers": [script, voice, music]
    }
