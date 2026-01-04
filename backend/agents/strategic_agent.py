from agents.base_agent import BaseAgent

class StrategicAgent(BaseAgent):
    def run(self, topic):
        prompt = f"""
        Create a full course outline for: {topic}
        Include modules, lessons, outcomes.
        """
        return self.llm.generate(prompt)
