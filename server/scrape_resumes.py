from pyresparser import ResumeParser
import nltk
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning)
outfile = os.getcwd() + '/../data/bulletpoints.txt'
badout = os.getcwd() + '/../data/badbullets.txt'
skillsfile = os.getcwd() + '/../data/skills.txt'

def parse_experience(experience: list):
    if experience is None:
        return []
    exp_sents = []

    for item in experience:
        bullet = (item.startswith('•') or item.startswith('●') or item.startswith('·')) and len(item) > 1
        tokenized = nltk.word_tokenize(item)
        pos_tagged = nltk.pos_tag(tokenized)
        verb = pos_tagged[0][1] in ['VBN', 'VBD'] and item[0].isupper()
        if bullet or verb:
            if bullet:
                sent = item[1:].lstrip()
            else:
                sent = item
            i = experience.index(item) + 1
            while i < len(experience):
                extension = experience[i]
                if extension[0].islower() or extension[0].isnumeric():
                    sent += ' ' + extension
                else:
                    break
                i+=1

            exp_sents.append(sent)

    return exp_sents

pdfs = []
for root, dirs, files in os.walk(os.getcwd() + '/../data/resumes'):
    for filename in files:
        if filename.endswith('.pdf'):
            pdfs.append(os.getcwd() + '/../data/resumes/' + filename)

bullets = []
bad_bullets = []
skills = []
for pdf in pdfs:
    data = ResumeParser(pdf).get_extracted_data()
    if data['experience'] is not None:
        bad_bullets += data['experience']
    new_bullets = parse_experience(data['experience'])
    bullets += new_bullets
    if data['skills'] is not None:
        skills += data['skills']


with open(outfile, 'w') as out:
    for bullet in bullets:
        out.write(f"{bullet}\n")

with open(badout, 'w') as out:
    for bullet in bad_bullets:
        out.write(f"{bullet}\n")

with open(skillsfile, 'w') as out:
    skills = set(skills)
    for skill in skills:
        out.write(f"{skill}\n")
