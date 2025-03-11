from modelengine_agents.agent_en.agents import CodeAgent

from modelengine_agents.core.models.OpenAIServerModelME import OpenAIServerModelME
from modelengine_agents.agent_en.default_tools import DuckDuckGoSearchTool
from modelengine_agents.core.observer.observer import MessageObserver
from modelengine_agents.core.agents.CodeAgentME import CodeAgentME

"""
description: 测试observer中的内容是否有变动,测试 CodeAgentME 类
"""


def single_agent():
    # 通过观察者获取模型的流式输出
    observer = MessageObserver()

    model = OpenAIServerModelME(
        observer=observer,
        model_id="deepseek-ai/DeepSeek-V3",
        api_key="sk-",
        api_base="https://api.siliconflow.cn")

    search_request_agent = CodeAgentME(
        observer=observer,
        tools=[DuckDuckGoSearchTool()],
        model=model,
        name="web_search_agent"
    )

    search_request_agent.run("特朗普内阁成员")


if __name__ == "__main__":
    single_agent()