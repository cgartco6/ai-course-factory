from agents.strategic_agent import StrategicAgent
from agents.research_agent import ResearchAgent
from agents.validator_agent import ValidatorAgent
from agents.fixer_agent import FixerAgent
from agents.course_creator_agent import CourseCreatorAgent
from utils.llm import LocalLLM

llm = LocalLLM()

def create_course(topic):
    strategic = StrategicAgent("Strategic", llm)
    research = ResearchAgent("Research", llm)
    validator = ValidatorAgent("Validator", llm)
    fixer = FixerAgent("Fixer", llm)
    creator = CourseCreatorAgent("Creator", llm)

    outline = strategic.run(topic)
    researched = research.run(outline)
    validated = validator.run(researched)
    fixed = fixer.run(validated)
    lessons = creator.run(fixed)

    return lessons
