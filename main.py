from fastapi import FastAPI
import uvicorn
from routes.agent_routes import agent_router
from routes.mission_routes import mission_router
from routes.report_routes import report_router

app = FastAPI()
app.include_router(agent_router)
app.include_router(mission_router)
app.include_router(report_router)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
