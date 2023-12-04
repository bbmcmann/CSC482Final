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

    # Substitute fields in the bio string
    formatted_bio = selected_bio.format(name=input_name, adj1 =adjectives[0], adj2=adjectives[1], skill1 = skills[0], skill2 = skills[1], skill3 = skills[3], end = input_end, year = get_formatted_year(input_year))

    print(formatted_bio)
    return formatted_bio

def get_adjectives():

    # Read the adjectives.txt file
    with open(os.getcwd() + '/../data/adjectives.txt', 'r') as file:
        adjectives = file.readlines()

    # Remove newline characters and select 5 random adjectives
    selected_adjectives = random.sample(adjectives, 5)
    selected_adjectives = [adj.strip() for adj in selected_adjectives]

    return selected_adjectives

def get_formatted_year(year):
    # Get formatted school year
    year_endings = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th'}
    return str(year) + year_endings[year]


if __name__ == "__main__":
    skills = [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "TypeScript",
            "React",
            "Go",
            "HTML",
            "CSS",
            "SQL",
            "Git",
          ]
    end = "September 2021"
    year = random.randint(1, 5)
    get_bio('John Doe', skills, end, year)