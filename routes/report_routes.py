from fastapi import APIRouter

report_router = APIRouter()


@report_router.get('/')
def home():
    return {"message": "Successfuly connected -reports-"}
