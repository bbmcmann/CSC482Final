import random

import pandas as pd

courses = pd.read_csv('../data/courses.csv')

def getCourses(year):
  """Given year in college, return a random list of courses taken."""
  taken = []
  if year == 1:
    taken = ['Fundamentals of Computer Science', 'Calculus I']
    if random.random() > 0.5:
      taken.append('Data Structures and Algorithms')
      if random.random() > 0.5:
        taken.append('Project-Based Object-Oriented Programming and Design')
    if random.random() > 0.5:
      taken.append('Public Speaking')
    if random.random() > 0.3:
      taken.append('Technical Writing')
  elif year == 2:
    taken = courses[(courses['grade_level'] < year) & (courses['required'] == 1)]['name'].tolist()
    taken.append('Project-Based Object-Oriented Programming and Design')
    taken.append('Introduction to Computer Organization')
    if random.random() > 0.5:
      taken.append('Systems Programming')
    if random.random() > 0.5:
      taken.append('Discrete Structures')
    if random.random() > 0.3:
      taken.append('Computer Architecture')
  elif year == 3:
    taken = ['Data Structures']
    taken.extend(courses[(courses['grade_level'] < year) & (courses['grade_level'] > 1) & (courses['required'] == 1)]['name'].tolist())
    if random.random() > 0.8:
      taken.append('Design and Analysis of Algorithms')
    if random.random() > 0.5:
      taken.append('Introduction to Software Engineering')
    possibleElectives = courses[(courses['grade_level'] == 3) | (courses['grade_level'] == 3)]['name'].tolist()
    numElectives = random.randint(1, 3)
    taken.extend(random.sample(possibleElectives, numElectives))
  else:
    taken = ['Data Structures', 'Systems Programming', 'Project-Based Object-Oriented Programming and Design']
    taken.extend(courses[(courses['grade_level'] < year) & (courses['grade_level'] > 2) & (courses['required'] == 1)]['name'].tolist())
    possibleElectives = courses[(courses['grade_level'] == 3) & (courses['required'] == 0)]['name'].tolist()
    possibleElectives.extend(courses[(courses['grade_level'] >= 4)]['name'].tolist())
    numElectives = random.randint(2, 4)
    taken.extend(random.sample(possibleElectives, numElectives))
  return list(set(taken))

if __name__ == '__main__':
  for i in range(10):
    print(getCourses(4))
