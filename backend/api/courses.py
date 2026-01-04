from fastapi import APIRouter
from workflows.course_workflow import create_course
from database import get_db

router = APIRouter()

@router.post("/courses")
def create(topic: str):
    content = create_course(topic)
    conn = get_db()
    conn.execute(
        "INSERT INTO courses (title, content) VALUES (?,?)",
        (topic, content)
    )
    conn.commit()
    return {"created": topic}
