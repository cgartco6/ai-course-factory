class CourseCreatorAgent(BaseAgent):
    def run(self, clean_content):
        return self.llm.generate(
            f"Write full course lessons:\n{clean_content}"
        )
