from fastapi import APIRouter

mission_router = APIRouter()


@mission_router.get('/')
def home():
    return {"message": "Successfuly connected -missions-"}
