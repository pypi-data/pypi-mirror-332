import json
from typing import Optional
import re

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import time
import uvicorn
from threading import Thread
import asyncio

from starlette.exceptions import HTTPException

from modelengine_agents.agent_en.agents import CodeAgent, ActionStep
from modelengine_agents.agent_en.memory import MemoryStep

from modelengine_agents.core.models.LiteLLMModelME import LiteLLMModelME
from modelengine_agents.agent_en.default_tools import DuckDuckGoSearchTool
from modelengine_agents.core.observer.observer import MessageObserver
from modelengine_agents.core.agents.CodeAgentME import CodeAgentME



def agent_run(agent: CodeAgentME, query: str):
    if not isinstance(agent, CodeAgentME):
        raise HTTPException(status_code=400, detail="Create Agent Object with CodeAgentME")
    if not isinstance(agent.model, LiteLLMModelME):
        raise HTTPException(status_code=400, detail="Create Model Object with LiteLLMModelME")
    if not isinstance(agent.observer, MessageObserver):
        raise HTTPException(status_code=400, detail="Create Observer Object with MessageObserver")

    observer = agent.observer

    # 目前已知的遗留问题，当前端主动中断后，该线程不会停止，仍会执行
    thread_agent = Thread(target=agent.run, args=(query,))
    thread_agent.start()

    yield f"接收到任务：{query}, 正在调用{agent.name}进行处理"

    while thread_agent.is_alive():
        if observer.has_new_content_flag:
            yield observer.get_output_str()

        time.sleep(0.2)


# 创建server，需要在这里构建自己的Agent
def create_single_agent():
    observer = MessageObserver()
    # model和Agent必须使用同一个observer
    model = LiteLLMModelME(
        observer=observer,
        model_id="deepseek/deepseek-chat",
        api_key="sk-724c8ad763a042579ec6c93c77817281",
        api_base="https://api.deepseek.com")

    search_request_agent = CodeAgentME(
        observer=observer,
        tools=[DuckDuckGoSearchTool()],
        model=model,
        name="web_search_agent"
    )
    return search_request_agent


app = FastAPI()

class FrontQuery(BaseModel):
    query: str


@app.post(path='/single_agent', summary="这是一个测试agent")
async def single_agent(request: FrontQuery):
    try:
        query = request.query
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        agent = create_single_agent()
    except Exception as e:
        raise HTTPException(status_code=400, detail="ERROR IN: create agent! Exception:" + str(e))

    return StreamingResponse(agent_run(agent, query), media_type="text/event-stream")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)