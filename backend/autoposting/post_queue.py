queue = []

def add_to_queue(platform, content):
    queue.append({"platform": platform, "content": content})

def get_queue():
    return queue
