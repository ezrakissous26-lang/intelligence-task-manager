from fastapi import APIRouter

report_router = APIRouter()


@report_router.get('/reports')
def home():
    return {"message": "Successfuly connected -reports-"}
