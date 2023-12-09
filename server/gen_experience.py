import random
import os
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
    "Social Network Website"
]

work_positions = [
    "Software Engineering Intern",
    "Software Development Intern",
    "Software Development Coop"
]

project_roles = [
    "Creator",
    "Team Lead",
    "Team Member"
]

def get_work(year):
    work = []
    worklen = max(0, year-1-random.randint(0, 1))

    for i in range(worklen):
        workyear = 2023 - i
        bullets = []
        for j in range(3):
            bullets.append(generate_bullet())
        workinfo = {
            'company': get_company(),
            'start': 'June ' + str(workyear),
            'end': 'September ' + str(workyear),
            'location': 'California',
            'position': random.choice(work_positions),
            'description': bullets
        }
        work.append(workinfo)
    return work

def get_projects(year):
    projects = []
    plen = max(1, 1 + (year//2) - random.randint(0, 1))

    for i in range(plen):
        projectyear = 2023 - i
        if projectyear == 2023:
            end = 'Present'
        else:
            end = random.choice(['January', 'February', 'March']) + ' ' + str(projectyear + 1)
        bullets =[]
        for j in range(2):
            bullets.append(generate_bullet())

        projectinfo = {
            'name': random.choice(all_projects),
            'role': random.choice(project_roles),
            'start': 'September ' + str(projectyear),
            'end': end,
            'description': bullets
        }
        projects.append(projectinfo)
    return projects

def generate_bullet():
    ###
    # PUT NLP GENERATOR FUNCTION HERE!!!! #
    ###

    return random.choice(all_bullets)


def get_company():
    total = companies['Number'].sum()
    pcts = (companies['Number']/total).tolist()
    return random.choices(companies['Company'].tolist(), pcts, k=1)[0]