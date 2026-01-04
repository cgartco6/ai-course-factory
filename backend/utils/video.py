import subprocess

def create_video(slides, audio, output):
    subprocess.run([
        "ffmpeg",
        "-i", slides,
        "-i", audio,
        "-shortest",
        output
    ])
