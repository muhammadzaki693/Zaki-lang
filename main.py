import sys
from sys import *

tokens = []

def fileopen(filename):
  data = open(filename+".zaki", "r").read()
  return data

def zaki(filecontent):
  tok = ""
  state = 0
  string = ""
  data = list(filecontent)
  for char in data:
    tok += char
    if tok == " ":
      if state == 0:
        tok = ""
      else:
        tok = " "
    elif tok == "\n":
      tok = ""
    elif tok == "print":
      tokens.append("print")
      tok = ""
    elif tok == "\"":
      if state == 0:
        state = 1
      elif state == 1:
        tokens.append("\""+string+"\"")
        string = ""
        state = 0
        tok = ""
    elif state == 1:
      string += char
      tok = ""
  print(tokens)

def run():
  data = fileopen("test")
  zaki(data)

run()