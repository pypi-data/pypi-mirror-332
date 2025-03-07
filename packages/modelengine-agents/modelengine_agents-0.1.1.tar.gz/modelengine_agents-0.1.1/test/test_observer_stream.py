import logging

from modelengine_agents.agent_en.agents import CodeAgent

from modelengine_agents.core.models.LiteLLMModelME import LiteLLMModelME
from modelengine_agents.agent_en.default_tools import DuckDuckGoSearchTool
from modelengine_agents.core.observer.observer import MessageObserver
from modelengine_agents.core.agents.CodeAgentME import CodeAgentME

"""
description: 测试observer中的内容是否有变动,测试 CodeAgentME 类
"""


def single_agent():
    # 通过观察者获取模型的流式输出
    observer = MessageObserver()

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

    search_request_agent.run("特朗普内阁成员")



def multi_agent():
    observer = MessageObserver()
    model = LiteLLMModelME(
        observer=observer,
        model_id="deepseek/deepseek-chat",
        api_key="sk-724c8ad763a042579ec6c93c77817281",
        api_base="https://api.deepseek.com")

    search_request_agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        name="web_search_agent",
        description="Runs web searches for you. Give it your query as an argument."
    )

    manager_agent = CodeAgent(
        tools=[],
        model=model,
        name="manager_agent",
        managed_agents=[search_request_agent]
    )
    manager_agent.run("对比DeepSeek和OpenAI的开源策略")




if __name__ == "__main__":
    single_agent()
    # multi_agent()
