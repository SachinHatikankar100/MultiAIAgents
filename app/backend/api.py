from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.common.custom_exception import CustomException
from app.common.logger import get_logger
from app.core.ai_agent import ai_agent_response

logger = get_logger(__name__)

app = FastAPI()

class RequestState(BaseModel):
    provider:str
    model:str
    user_input:str
    allow_search:bool
    system_prompt:str


@app.post("/chat")
def chat_endPoint(request:RequestState):

    
    try:
        response = ai_agent_response(
            request.provider,
            request.model,
            request.user_input,
            request.system_prompt,
            request.allow_search,
        )

        return {"response":response}
    except CustomException as e:
        print(str(e))
        logger.error("Error while processing the request in backend")



