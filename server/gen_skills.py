import os
import random

otherSkillsfile = os.getcwd() + '/../data/otherSkills.txt'
languageSkillsfile = os.getcwd() + '/../data/languageSkills.txt'


def getSkills(year):
    skills = {}
    with open(languageSkillsfile, 'r') as file:
        all_skills = [s.rstrip() for s in file.readlines()]
        skills['languages'] = list(set(['Python'] + random.choices(all_skills, k=1+year)))
    with open(otherSkillsfile, 'r') as file:
        all_skills = [s.rstrip() for s in file.readlines()]
        skills['tools'] = list(set(['Git'] + random.choices(all_skills, k=1+year)))
        
    return skills
