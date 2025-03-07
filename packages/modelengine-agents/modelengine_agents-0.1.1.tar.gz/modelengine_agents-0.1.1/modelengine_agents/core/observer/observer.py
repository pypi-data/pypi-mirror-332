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
        # 记录所有message
        self.message = []

        # 统一输出给前端的字符串
        self.output_str = ""

        # 记录当前流程的message
        self.now_message = ""

        # 如果有字段变化，则设置True
        self.has_new_content_flag = False


    def update(self, subject):
        if isinstance(subject, ModelSubject):
            stream_output = subject.get_stream_token()
            self.now_message = "".join(stream_output)


            self.output_str += stream_output[-1]
            self.has_new_content_flag = True



    def add_message(self, agent_name, process_type, content):
        self.message.append({
            "agent_name": agent_name,
            "process_name": process_type,
            "content": content
        })

        if ProcessType.MODEL_OUTPUT != process_type:
            self.output_str += f"\n\n{content}\n\n"
            self.has_new_content_flag = True

    def get_output_str(self):
        self.has_new_content_flag = False
        return self.output_str
