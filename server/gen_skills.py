import random
import os

skillsfile = os.getcwd() + '/../data/skills.txt'


def getSkills(year):
    with open(skillsfile, 'r') as file:
        all_skills = [s.rstrip() for s in file.readlines()]
        langs = list(set(['Python'] + random.choices(all_skills, k=3+year)))
        tools = list(set(['Git'] + random.choices(all_skills, k=1+year)))
        skills = {"languages": langs,
                  "tools": tools}
        return skills
