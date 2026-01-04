class ValidatorAgent(BaseAgent):
    def run(self, content):
        return self.llm.generate(
            f"Validate facts and flag errors:\n{content}"
        )
