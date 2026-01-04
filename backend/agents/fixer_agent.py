class FixerAgent(BaseAgent):
    def run(self, issues):
        return self.llm.generate(
            f"Fix and improve this content:\n{issues}"
        )
