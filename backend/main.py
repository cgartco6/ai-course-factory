from fastapi import FastAPI
from workflows.course_workflow import create_course

app = FastAPI()

@app.post("/create-course")
def create(topic: str):
    course = create_course(topic, AGENTS)
    return {"course": course}
