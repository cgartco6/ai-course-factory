import os
from pathlib import Path

root = Path("AI_Course_FACTORY")

# --- MEDIA PLACEHOLDERS ---
media_images = root / "media/images"
media_audio = root / "media/audio"
media_video = root / "media/video"

media_images.mkdir(parents=True, exist_ok=True)
media_audio.mkdir(parents=True, exist_ok=True)
media_video.mkdir(parents=True, exist_ok=True)

# Create sample image placeholders
for i in range(1, 4):
    path = media_images / f"sample_image_{i}.txt"  # using .txt as placeholder
    with open(path, "w") as f:
        f.write(f"This is placeholder image {i} (replace with real AI-generated image)")

# Create sample audio placeholders
for i in range(1, 3):
    path = media_audio / f"sample_audio_{i}.txt"
    with open(path, "w") as f:
        f.write(f"This is placeholder audio {i} (replace with AI-generated voice/music)")

# Create sample video placeholders
for i in range(1, 3):
    path = media_video / f"sample_video_{i}.txt"
    with open(path, "w") as f:
        f.write(f"This is placeholder video {i} (replace with AI-generated short/reel)")

# --- COURSE PACKAGE PLACEHOLDERS ---
course_package_root = root / "course_package"
course_videos = course_package_root / "videos"
course_audio = course_package_root / "audio"
course_images = course_package_root / "images"

for folder in [course_videos, course_audio, course_images]:
    folder.mkdir(parents=True, exist_ok=True)

# Sample video
with open(course_videos / "sample_course_video.txt", "w") as f:
    f.write("Sample course video placeholder")

# Sample audio
with open(course_audio / "sample_course_audio.txt", "w") as f:
    f.write("Sample course audio placeholder")

# Sample images
for i in range(1, 3):
    with open(course_images / f"sample_course_image_{i}.txt", "w") as f:
        f.write(f"Sample course image {i}")

# Sample documents
for doc in ["workbook.docx", "refund_policy.pdf", "disclaimer.pdf"]:
    path = course_package_root / doc
    with open(path, "w") as f:
        f.write(f"Placeholder for {doc}")

print("Sample media and course_package populated!")
