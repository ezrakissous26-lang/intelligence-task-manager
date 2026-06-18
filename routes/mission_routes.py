from fastapi import APIRouter

mission_router = APIRouter()


@mission_router.get('/missions')
def home():
    return {"message": "Successfuly connected -missions-"}
