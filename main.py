import sys
from sys import *

def fileopen(filename):
  data = open(filename+".zaki", "r").read()
  return data

def zaki(filecontent):
  data = open("test.zaki","r").read()
  try:
    y = eval(data)
    print(y)
  except:
    try:
      exec(data)
    except Exception as e:
      print("error:"+e)

def run():
  data = fileopen("test")
  zaki(data)

run()