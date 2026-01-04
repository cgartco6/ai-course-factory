TOPICS = [
    "You are not too old for AI",
    "AI explained calmly",
    "Feeling left behind by tech",
    "Learning at your own pace",
    "AI for normal adults",
    "No hype AI learning",
    "Staying relevant after 50"
]

def weekly_plan():
    return [{"day": i+1, "topic": t} for i, t in enumerate(TOPICS)]
