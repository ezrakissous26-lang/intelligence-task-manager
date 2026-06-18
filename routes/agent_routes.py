from fastapi import APIRouter

agent_router = APIRouter()


@agent_router.get('/agents')
def home():
    return {"message": "Successfuly connected -agents-"}
