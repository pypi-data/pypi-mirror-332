from sympy.strategies.core import switch

from modelengine_agents.core.observer.subject import ModelSubject
from enum import Enum


class Observer:
    def update(self, subject):
        # 被订阅者调用，更新自身
        pass


class ProcessType(Enum):
    STEP_COUNT = "step_count"            # 当前处于agent的哪一步
    MODEL_OUTPUT = "model_output"        # 模型流式输出
    PARSE = "parse"                      # 代码解析结果
    EXECUTION_LOGS = "execution_logs"    # 代码执行结果
    AGENT_NEW_RUN = "agent_new_run"      # Agent基本信息打印



class MessageObserver(Observer):
    def __init__(self):
        # 分段记录所有message
        self.message = []

        # 统一输出给前端的字符串
        self.str_buffer = ""

        # 记录流程所有的字符串信息
        self.now_message = ""

        # 判断输出是否结束
        self.is_output_end = False


    def update(self, subject):
        new_token = subject.get_new_token()
        self.str_buffer += new_token


    def add_message(self, agent_name, process_type, content):
        # 用于返回特定任务字符串给前端
        self.message.append({
            "agent_name": agent_name,
            "process_name": process_type,
            "content": content
        })

        if ProcessType.AGENT_NEW_RUN == process_type:
            self.str_buffer += f"\n\n{content}\n\n"
        elif ProcessType.STEP_COUNT == process_type:
            self.str_buffer += f"\n**Step {content}** \n"


    def add_new_data(self, new_str):
        # 用于适配smolagent输出，返回给前端
        self.str_buffer += new_str


    def get_output_str(self):
        # 对外输出输出
        if len(self.str_buffer):
            cached_str = self.str_buffer
            self.now_message += self.str_buffer
            self.str_buffer = ""
            return cached_str
        else:
            return ""
