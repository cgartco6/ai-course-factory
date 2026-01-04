from fastapi import APIRouter

router = APIRouter()

@router.get("/owner/stats")
def stats():
    return {
        "courses": 1,
        "automation": "active",
        "status": "scaling"
    }
