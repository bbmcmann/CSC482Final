import random
import os


def get_bio(input_name, skills, input_end, input_year):
    # Read the bio.txt file
    with open(os.getcwd() + '/../data/bio.txt', 'r') as file:
        bios = file.readlines()

    # Select a random bio
    selected_bio = random.choice(bios)

    # Get adjectives
    adjectives = get_adjectives()

    # Get skills
    skills = get_skills(skills)

    # Substitute fields in the bio string
    formatted_bio = selected_bio.format(name=input_name, 
                                        adj1 =adjectives[0], 
                                        adj2=adjectives[1], 
                                        skill1 = skills[0], 
                                        skill2 = skills[1], 
                                        skill3 = skills[3],
                                        focus_area = get_focus_area(),
                                        company = get_company(),
                                        end = input_end, 
                                        year = get_formatted_year(input_year))

    print(formatted_bio)
    return formatted_bio

def extract_company_names():
    company_names = []
    with open(os.getcwd() + '/../data/allcompanies.csv', 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line
        for line in lines:
            company_name = line.split(',')[0].strip()
            company_names.append(company_name)
    return company_names

def get_company():
    company_names = extract_company_names()
    selected_company = random.choice(company_names)
    return selected_company

def get_adjectives():

    # Read the adjectives.txt file
    with open(os.getcwd() + '/../data/adjectives.txt', 'r') as file:
        adjectives = file.readlines()

    # Remove newline characters and select 5 random adjectives
    selected_adjectives = random.sample(adjectives, 5)
    selected_adjectives = [adj.strip().lower() for adj in selected_adjectives]

    return selected_adjectives

def get_focus_area():
    with open(os.getcwd() + '/../data/focus_areas.txt', 'r') as file:
        focus_areas = file.readlines()
    selected_area = random.choice(focus_areas).lower().strip()

    return selected_area

def get_formatted_year(year):
    # Get formatted school year
    year_endings = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th'}
    return str(year) + year_endings[year]

def get_skills(skills):
    skills_flat = skills.get('languages') + skills.get('tools')
    # Remove newline characters and select 5 random skills
    selected_skills = random.sample(skills_flat, 5)
    selected_skills = [skill.strip() for skill in selected_skills]

    return selected_skills

if __name__ == "__main__":
    skills = {
            "languages":["Python",
                        "Java",
                        "C++",
                        "JavaScript",
                        "TypeScript",
                        "Go",
                        "HTML",
                        "CSS",
                        "SQL"],
            "tools": ["Flask", "React", "Git"]
    }
    end = "September 2021"
    year = random.randint(1, 5)
    get_bio('John Doe', skills, end, year)