import header
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources = {"/": {"origins": "http://localhost:5178/"}})

@app.route("/")
def hello_world():
    return {"message": "Hello World!"}

@app.route("/generate")
@cross_origin()
def generateStudent():
    genHeader = header.getHeader()
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
    genBio = bio.get_bio(genHeader['name'], skills)
    

    return {
        'bio': genBio,
        'resume': {
          'name': genHeader['name'],
          'email': genHeader['email'],
          'phone': genHeader['phone'],
          'linkedin': genHeader['linkedin'],
          'education': {
            'school': "California Polytechnic State University, San Luis Obispo",
            'location': "San Luis Obispo, CA",
            'degree': "Bachelor of Science, Computer Science",
            'gpa': 3.5,
            'start': "September 2018",
            'end': "June 2022",
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
          'skills': [
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
          ],
        }
      }