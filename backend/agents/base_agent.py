class BaseAgent:
    def __init__(self, name, llm):
        self.name = name
        self.llm = llm

    def run(self, task):
        raise NotImplementedError
