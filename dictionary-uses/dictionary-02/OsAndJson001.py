import os
import json

print('enter a path to create a file')
myPath = input()
if not os.path.exists(myPath):
  with open(myPath,'w') as myFile:
    myFile.write('this is my file, created by python')

with open(myPath,'r') as myFile:
  contents = myFile.readline()
  print(contents)

with open(myPath, 'a') as myFile:
  myFile.write('this is a new line appendened on my file')

with open(myPath,'r') as myFile:
  contents = myFile.readline()
  print(contents)



