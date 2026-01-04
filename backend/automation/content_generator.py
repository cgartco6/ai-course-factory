from utils.llm import LocalLLM

llm = LocalLLM()

def generate_daily_content(course_name):
    post = llm.generate(
        f"Create a short motivational post for {course_name}"
    )
    short = llm.generate(
        f"Create a 30-second short script promoting {course_name}"
    )
    return post, short
