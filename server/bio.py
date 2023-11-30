import random
import random

def get_bio(input_name, skills):
    # Read the bio.txt file
    with open('/Users/kellybecker/Desktop/NLP/CSC482Final/data/bio.txt', 'r') as file:
        bios = file.readlines()

    # Select a random bio
    selected_bio = random.choice(bios)

    # Get adjectives
    adjectives = get_adjectives()

    # Substitute fields in the bio string
    formatted_bio = selected_bio.format(name=input_name, adj1 =adjectives[0], adj2=adjectives[1], skill1 = skills[0], skill2 = skills[1])

    return formatted_bio

def get_adjectives():

    # Read the adjectives.txt file
    with open('/Users/kellybecker/Desktop/NLP/CSC482Final/data/adjectives.txt', 'r') as file:
        adjectives = file.readlines()

    # Remove newline characters and select 5 random adjectives
    selected_adjectives = random.sample(adjectives, 5)
    selected_adjectives = [adj.strip() for adj in selected_adjectives]

    return selected_adjectives


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
    print(get_bio('John Doe', skills))