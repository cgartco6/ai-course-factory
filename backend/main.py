from fastapi import FastAPI
from api.dashboard import router as dashboard_router
from api.courses import router as courses_router
from database import init_db

app = FastAPI(title="AI Course Factory")

init_db()

app.include_router(dashboard_router)
app.include_router(courses_router)

@app.get("/")
def root():
    return {"status": "AI Course Factory running"}
