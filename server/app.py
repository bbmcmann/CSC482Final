import header
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../')
from data import generate_basic
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return {"message": "Hello World!"}

@app.route("/generate")
def generateStudent():
    home_region = generate_basic.get_home_region()
    homecity = generate_basic.get_home_city(home_region)
    areacode = generate_basic.get_area_code(homecity)
    genHeader = header.getHeader(areacode)
    start, end = generate_basic.get_years()
    spanishfluent = generate_basic.get_spanish_fluent()
    
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
    if spanishfluent:
        skills.append('Fluent in Spanish')
    
    return {
        'bio': '''I am a student at the Cal Poly SLO from {}, studying Computer Science. I am
              interested in a wide variety of topics, including but not limited to:
              web development, machine learning, and natural language processing.'''.format(homecity),
        'resume': {
          'name': genHeader['name'],
          'email': genHeader['email'],
          'phone': genHeader['phone'],
          'linkedin': genHeader['linkedin'],
          'education': {
            'school': "California Polytechnic State University, San Luis Obispo",
            'location': "San Luis Obispo, CA",
            'degree': "Bachelor of Science, Computer Science",
            'gpa': generate_basic.generate_gpa(),
            'start': start,
            'end': end,
            'courses': [
              "Data Structures and Algorithms",
              "Systems Programming",
              "Computer Architecture and Assembly Language",
              "Operating Systems",
              "Artificial Intelligence",
              "Natural Language Processing",
              "Machine Learning",
            ],
          },
          'experience': [
            {
              'company': "Google",
              'location': "Mountain View, CA",
              'position': "Software Engineering Intern",
              'start': "June 2021",
              'end': "September 2021",
              'description': [
                "Worked on the Google Search team",
                "Implemented a new feature for Google Search",
                "Used React, TypeScript, and Go",
              ],
            },
            {
              'company': "Facebook",
              'location': "Menlo Park, CA",
              'position': "Software Engineering Intern",
              'start': "June 2020",
              'end': "September 2020",
              'description': [
                "Worked on the Facebook Search team",
                "Implemented a new feature for Facebook Search",
                "Used React, TypeScript, and Go",
              ],
            },
          ],
          'projects': [
            {
              'name': "Artificial CSC Student",
              'role': "Creator",
              'start': "September 2021",
              'end': "Present",
              'description': ["Created an artificial CSC student", "Used Python"],
            },
            {
              'name': "Artificial CSC Student",
              'role': "Creator",
              'start': "September 2021",
              'end': "Present",
              'description': ["Created an artificial CSC student", "Used Python", "Used React"],
            },
            {
              'name': "Artificial CSC Student",
              'role': "Creator",
              'start': "September 2021",
              'end': "Present",
              'description': ["Created an artificial CSC student", "Used Python", "Used React", "Used Go"],
            },
          ],
          'skills': skills
        }
      }