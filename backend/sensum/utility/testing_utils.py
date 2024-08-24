import re

def createRegex(string):
  return re.compile(string, flags=re.IGNORECASE)
