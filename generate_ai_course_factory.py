import os
import shutil
from pathlib import Path

# Root folder
root = Path("AI_COURSE_FACTORY")

# Folder structure
folders = [
    "backend/marketing_ai",
    "backend/autoposting",
    "backend/finance",
    "backend/compliance",
    "backend/resilience",
    "backend/utils",
    "backend/automation",
    "frontend/landing/css",
    "frontend/landing/js",
    "frontend/dashboard/css",
    "frontend/dashboard/js",
    "media/images",
    "media/audio",
    "media/video",
    "automation_data",
    "course_package/videos",
    "course_package/audio",
    "course_package/images"
]

# Files with content
files = {
    "run_windows.bat": '''@echo off
call venv\\Scripts\\activate
python backend\\automation\\daily_content.py
pause
''',

    "requirements.txt": "flask\npillow\npyttsx3\npython-docx\n",

    "README.md": '''AI_COURSE_FACTORY
-----------------
Generates courses, marketing content, landing pages, and weekly reports.

Instructions:
1. Create virtual environment: python -m venv venv
2. Activate: venv\\Scripts\\activate
3. Install dependencies: pip install -r requirements.txt
4. Run: run_windows.bat
5. Open frontend/landing/index.html in browser
''',

    "frontend/landing/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Made Simple</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="hero">
<h1>AI Made Simple</h1>
<p>Learn AI calmly, step-by-step, at your own pace.</p>
<a href="#enroll" class="cta">Start Now</a>
</header>
<section id="enroll">
<p class="price">R199 — One-time</p>
<button onclick="enroll()">Enroll Now</button>
</section>
<script src="js/main.js"></script>
</body>
</html>
''',

    "frontend/landing/over50.html": '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>AI for 50+</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="hero"><h1>AI for Adults Over 50</h1>
<p>Learn AI calmly, step by step.</p>
<a href="#enroll" class="cta">Start Now</a></header>
<section id="enroll"><p class="price">R199 — One-time</p>
<button onclick="enroll()">Enroll Now</button></section>
<script src="js/main.js"></script>
</body></html>
''',

    "frontend/landing/business.html": '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>AI for Small Business</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="hero"><h1>AI for Small Business Owners</h1>
<p>Learn practical AI skills for your business.</p>
<a href="#enroll" class="cta">Start Now</a></header>
<section id="enroll"><p class="price">R199 — One-time</p>
<button onclick="enroll()">Enroll Now</button></section>
<script src="js/main.js"></script>
</body></html>
''',

    "frontend/landing/jobseekers.html": '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>AI for Job Seekers</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="hero"><h1>AI Skills to Get Hired</h1>
<p>Step-by-step AI training for adults looking to improve career opportunities.</p>
<a href="#enroll" class="cta">Start Now</a></header>
<section id="enroll"><p class="price">R199 — One-time</p>
<button onclick="enroll()">Enroll Now</button></section>
<script src="js/main.js"></script>
</body></html>
''',

    "frontend/landing/css/style.css": '''body{font-family:Arial,sans-serif;margin:0;padding:0;}
.hero{background:#f2f2f2;padding:50px;text-align:center;}
.cta{padding:10px 20px;background:#007BFF;color:white;border:none;cursor:pointer;}
.price{font-weight:bold;}''',

    "frontend/landing/js/main.js": '''function enroll(){alert("Enrollment coming soon.");}''',

    "frontend/dashboard/index.html": '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Dashboard</title>
<link rel="stylesheet" href="../landing/css/style.css">
</head>
<body>
<header class="hero"><h1>Operator Dashboard</h1></header>
<section>
<h2>Today's Status</h2>
<ul>
<li>Posters: <span id="poster-count">0</span></li>
<li>Shorts: <span id="shorts-count">0</span></li>
<li>Voices: <span id="voice-count">0</span></li>
<li>Queue: <span id="queue-count">0</span></li>
</ul></section>
<section>
<h2>Weekly Report</h2>
<pre id="weekly-report">No report yet</pre>
</section>
<script src="../landing/js/main.js"></script>
</body>
</html>
''',

    # Placeholders for course_package
    "course_package/workbook.docx": "",
    "course_package/refund_policy.pdf": "",
    "course_package/disclaimer.pdf": "",
    "course_package/README.txt": "This folder will be populated by AI-generated course content."
}

# Backend placeholder scripts
backend_files = [
    "poster_generator.py",
    "shorts_generator.py",
    "voice_generator.py",
    "music_generator.py",
    "combiner.py",
    "post_queue.py",
    "platform_rules.py",
    "facebook_api.py",
    "instagram_api.py",
    "youtube_api.py",
    "x_api.py",
    "manual_export.py",
    "audit_log.py",
    "refund_policy.py",
    "disclaimers.py",
    "data_protection.py",
    "watchdog.py",
    "self_heal.py",
    "document_creator.py",
    "daily_content.py",
    "weekly_scheduler.py",
    "report_generator.py"
]

# Create folders
for folder in folders:
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)

# Create files
for filepath, content in files.items():
    path = root / filepath
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Create backend placeholder scripts
for filename in backend_files:
    # Determine folder
    if filename in ["poster_generator.py", "shorts_generator.py", "voice_generator.py", "music_generator.py", "combiner.py"]:
        folder = root / "backend/marketing_ai"
    elif filename in ["post_queue.py","platform_rules.py","facebook_api.py","instagram_api.py","youtube_api.py","x_api.py","manual_export.py"]:
        folder = root / "backend/autoposting"
    elif filename in ["audit_log.py"]:
        folder = root / "backend/finance"
    elif filename in ["refund_policy.py","disclaimers.py","data_protection.py"]:
        folder = root / "backend/compliance"
    elif filename in ["watchdog.py","self_heal.py"]:
        folder = root / "backend/resilience"
    elif filename in ["document_creator.py"]:
        folder = root / "backend/utils"
    else:  # automation scripts
        folder = root / "backend/automation"
    folder.mkdir(parents=True, exist_ok=True)
    with open(folder / filename, "w", encoding="utf-8") as f:
        f.write(f"# Placeholder for {filename}\n")

# Create empty media and automation_data folders
for folder in ["media/images","media/audio","media/video","automation_data"]:
    (root / folder).mkdir(parents=True, exist_ok=True)

# Create empty course_package subfolders
for folder in ["course_package/videos","course_package/audio","course_package/images"]:
    (root / folder).mkdir(parents=True, exist_ok=True)

# Zip the folder
shutil.make_archive("AI_Course_Factory_v1", 'zip', root)
print("ZIP created: AI_Course_Factory_v1.zip")
