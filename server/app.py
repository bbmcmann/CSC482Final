import os
import random
import sys

import courses
import gen_experience
import gen_skills
import header

cwd = os.getcwd()
sys.path.append(cwd + '/../')
import bio
from flask import Flask, request
from flask_cors import CORS, cross_origin

from data import generate_basic

app = Flask(__name__)
cors = CORS(app, resources = {"/": {"origins": "http://localhost:5178/"}})

@app.route("/")
def hello_world():
    return {"message": "Hello World!"}

@app.route("/generate")
@cross_origin()
def generateStudent():
    home_region = generate_basic.get_home_region()
    homecity = generate_basic.get_home_city(home_region)
    areacode = generate_basic.get_area_code(homecity)
    genHeader = header.getHeader(areacode)
    year = int(request.args.get('year'))
    useCustomModel = request.args.get('custom_model')
    if useCustomModel == "true":
        useCustomModel = True
    else:
        useCustomModel = False
    if year >= 6:
      year = random.randint(1, 5)
    else:
      year = year

    start, end = generate_basic.get_years(year)
    skills = gen_skills.getSkills(year)
    genBio = bio.get_bio(genHeader['name'], skills, end, year)
    degree = "B.S." if year < 5 else "M.S."
    

    return {
        'bio': genBio,
        'resume': {
          'year': year,
          'name': genHeader['name'],
          'email': genHeader['email'],
          'phone': genHeader['phone'],
          'linkedin': genHeader['linkedin'],
          'education': {
            'school': "California Polytechnic State University, San Luis Obispo",
            'location': "San Luis Obispo, CA",
            'degree': degree + " Computer Science",
            'gpa': generate_basic.generate_gpa(),
            'start': start,
            'end': end,
            'courses': courses.getCourses(year),
          },
          'experience': gen_experience.get_work(year, useCustomModel), 
          'projects': gen_experience.get_projects(year, useCustomModel),
          'skills': skills
        }
      }