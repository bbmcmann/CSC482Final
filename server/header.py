import random

# open the name data files on start up
boyfile = open('../data/boynames.txt', 'r')
boynames = boyfile.readlines()
girlfile = open('../data/girlnames.txt', 'r')
girlnames = girlfile.readlines()
lastfile = open('../data/lastnames.txt', 'r')
lastnames = lastfile.readlines()


def getHeader():
  '''Get the header data for the resume. Returns dictionary with name, email, phone, and linkedin url'''
  name = getRandomName()
  email = getEmail(name)
  phone = getPhone()
  linkedin = getLinkedIn(name)
  return {
    'name': name,
    'email': email,
    'phone': phone,
    'linkedin': linkedin,
  }

def getRandomName():
  '''Get a random name from the name data files based on gender distribution. Returns string with first and last name'''
  if random.random() < 0.71:
    return random.choice(boynames).strip() + " " + random.choice(lastnames).strip()
  else:
    return random.choice(girlnames).strip() + " " + random.choice(lastnames).strip()

def getEmail(name):
  '''Get an email based on the name. Returns string with email'''
  domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", '@calpoly.edu']
  return name.lower().replace(" ", "") + random.choice(domains)

def getPhone():
  '''Get a random phone number. Returns string with phone number'''
  return str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))

def getLinkedIn(name):
  '''Get a linkedin url based on the name. Returns string with linkedin url'''
  return "linkedin.com/in/" + name.lower().replace(" ", "")

if __name__ == "__main__":
  print(getHeader())