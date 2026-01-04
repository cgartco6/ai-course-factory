def create_course(topic, agents):
    outline = agents["strategic"].run(topic)
    research = agents["research"].run(outline)
    validated = agents["validator"].run(research)
    fixed = agents["fixer"].run(validated)
    lessons = agents["creator"].run(fixed)
    return lessons
