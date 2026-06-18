from fastapi import APIRouter, Body, HTTPException
import logging
from database.agent_db import AgentDB

agent_cls = AgentDB()
logger = logging.getLogger("app")
agent_router = APIRouter()


@agent_router.get('/')
def home():
    return {"message": "Successfuly connected -agents-"}


@agent_router.post('/agents')
def r_create_agents(data: dict = Body(...)):
    logger.info("POST create_agent called")
    try:
        logger.info("Creating agent...")
        result = agent_cls.create_agents(data)
        logger.info("Agent created successfully")
        return result
    except Exception as e:
        logger.error(f"Error while creating agent: {e}")
        raise HTTPException(status_code=400, detail=e)  # str de e ? pk 



@agent_router.get('/agents')
def r_get_agents():
    logger.info("GET get_agent called")
    try:
        logger.info("Displaying agents...")
        result = agent_cls.get_all_agents()
        logger.info("Agents displaying successfully")
        return result
    except Exception as e:
        logger.error(f"Error while displaying agents: {e}")
        raise HTTPException(status_code=400, detail=e)



@agent_router.get('/agents/{id}')
def r_get_agents_by_id(id: int):
    logger.info(f"GET get_agent_by_id:{id} called")
    logger.info("Displaying agent by id...")
    result = agent_cls.get_agent_by_id(id)
    if result is None:
        logger.error("Agent not found")
        raise HTTPException(status_code=404, detail="Agent not found")
    logger.info("Agent displayed successfully")
    return result


@agent_router.put('/agents/{id}')
def r_update_agent(id: int, data: dict = Body(...)):
    logger.info("PUT update_agent called")
    try:
        logger.info(f"U^pdating agent...")
        result = agent_cls.update_agent(id, data)
        logger.info("Agent updated successfully")
        return {"message": result}
    except Exception as e:
        logger.error(f"Error while updating agent: {e}")
        raise HTTPException(status_code=404, detail=e)


@agent_router.put('/agents/{id}/deactivate')
def r_deactivate_agent(id: int):
    logger.info("PUT deactivate_agent called")
    find = agent_cls.get_agent_by_id(id)
    if find is None:
        logger.error(f"Agent {id} not found")
        raise HTTPException(status_code=404, detail="Agent not found")
    logger.info("Deactivating agent...")
    result = agent_cls.deactivate_agent(id)
    logger.info("Deactivated successfully")
    return {"message": result}


@agent_router.get('/agents/{id}/performance')
def r_get_perf_by_id(id: int):
    logger.info("GET get_perf_of_agent called")
    find = agent_cls.get_agent_by_id(id)
    if find is None:
        logger.error("Agent not found")
        raise HTTPException(status_code=404, detail="Id agent not found")
    logger.info("Searching performance of agent")
    result = agent_cls.get_agent_performance(id)
    logger.info("Get performance with success")
    return result
