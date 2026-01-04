class ResearchAgent(BaseAgent):
    def run(self, outline):
        return self.llm.generate(
            f"Research accurate content for:\n{outline}"
        )
