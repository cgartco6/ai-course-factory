from automation.content_generator import generate_daily_content
from datetime import datetime

def run_daily(course):
    post, short = generate_daily_content(course)
    with open("automation_data/daily_posts.txt", "a") as f:
        f.write(f"\n[{datetime.now()}]\nPOST:\n{post}\nSHORT:\n{short}\n")
