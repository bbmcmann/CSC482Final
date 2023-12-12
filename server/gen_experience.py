import os
import random

import custom_llm
import experiences_model
import pandas as pd

bullet_file = os.getcwd() + '/../data/bulletpoints.txt'
company_file = os.getcwd() + '/../data/companies.txt'

with open(bullet_file, 'r') as file:
    all_bullets = [b.rstrip() for b in file.readlines()]

# with open(company_file, 'r') as file:
#     all_companies = [c.rstrip() for c in file.readlines()]

companies = pd.read_csv(os.getcwd() + '/../data/allcompanies.csv')

all_projects = [
    "Artificial CSC Student",
    "Movie Review App",
    "Computer Vision Project",
    "GUI Interface",
    "Platformer Video Game",
    "Social Network Website",
    "Image Captioning AI",
    "Stellar Classification AI",
    "SLO Hikes Software",
    "Cal Poly Hack4Impact",
    "Cal Poly Racing",
    "Cal Poly Robotics",
    "SLOHacks Hackathon",
    "Volunteer Management System WebApp",
    "Idiom Identifier",
    "Custom Mobile App",
    "Personal Portfolio Website",
    "Virtual World Simulator",
    "Programming Language Interpreter",
    "Discord Server and Bot"
]

work_positions = [
    "Software Engineering Intern",
    "Software Development Intern",
    "Software Development Co-op",
    "Software Developer",
    "DevOps Intern",
    "UI/UX Developer",
    "Student Researcher"
]

project_roles = [
    "Creator",
    "Team Lead",
    "Team Member"
]


def get_work(year, use_custom):
    work = []
    worklen = max(0, year-1-random.randint(0, 1))

    for i in range(worklen):
        workyear = 2023 - i
        bullets = []
        company = get_company()
        position = random.choice(work_positions)
        if use_custom:
            for j in range(3):
                bullets.append(generate_bullet(use_custom, company, position))
        else:
            bullets = generate_bullet(use_custom, company, position)
        workinfo = {
            'company': company,
            'start': 'June ' + str(workyear),
            'end': 'September ' + str(workyear),
            'location': 'California',
            'position': position,
            'description': bullets
        }
        work.append(workinfo)
    return work


def get_projects(year, use_custom):
    projects = []
    plen = max(2, 1 + (year//2) - random.randint(0, 1))

    for i in range(plen):
        projectyear = 2023 - i
        if projectyear == 2023:
            end = 'Present'
        else:
            end = random.choice(['January', 'February', 'March']) + ' ' + str(projectyear + 1)
        bullets =[]
        projectName = random.choice(all_projects)
        if use_custom:
            for j in range(2):
                bullets.append(generate_bullet(use_custom))
        else:
            bullets = generate_bullet(use_custom, projectName)

        projectinfo = {
            'name': projectName,
            'role': random.choice(project_roles),
            'start': 'September ' + str(projectyear),
            'end': end,
            'description': bullets
        }
        projects.append(projectinfo)
    return projects


def generate_bullet(use_custom, company, position=None):
    ret_bullet = ""
    if use_custom:
        # use Ben custom
        primer_strings = ["Developed a", "Led a", "Assisted in", "Implemented a", "Led the", "Assisted the",
                          "Worked on", "Collaborated with", "Created a", "Developed web", "Participated in"]
        model_used = ".\\pytorch_models\experience_model_1.1_100.pth"
        ret_bullet = experiences_model.make_version1_bullet_point(model_used, 15, random.choice(primer_strings))
    else:
        # use Kelly chat gpt
        if position is None:
            ret_bullet = custom_llm.generate_project_bullets(company)
        else:
            ret_bullet = custom_llm.generate_exp_bullets(company, position)
    return ret_bullet


def get_company():
    total = companies['Number'].sum()
    pcts = (companies['Number']/total).tolist()
    return random.choices(companies['Company'].tolist(), pcts, k=1)[0]