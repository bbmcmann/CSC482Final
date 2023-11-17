import pandas as pd
import requests
from bs4 import BeautifulSoup

# fetch csc catalog page
response = requests.get('https://catalog.calpoly.edu/coursesaz/csc/')
soup = BeautifulSoup(response.content, "html.parser")

# find all course divs
courselist = soup.findAll('div', {"class": 'courseblock'})

# create a dataframe to store course data
courses = []
for course in courselist:
  course_name = course.find('p', {'class': 'courseblocktitle'}).find('strong').text.split('.')
  course_code = course_name[0]
  course_name = course_name[1].strip()
  grade_level = course_code[4]
  description = course.find('div', {'class': 'courseblockdesc'}).find('p').text.strip()


  courses.append({
      'code': course_code,
      'name': course_name,
      'grade_level': grade_level,
      'description': description, 
  })
pd.DataFrame(courses)

# save to csv
pd.DataFrame(courses).to_csv('courses.csv', index=False)