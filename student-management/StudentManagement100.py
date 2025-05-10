# this doc contain my solution using python language.
# I used the layered architecture pattern for this example

class Student:
  def __init__(self,id,name,grade1,grade2):
    self.name = name
    self.id = id
    self.grade1 = grade1
    self.grade2 = grade2
    self.average = (grade1 + grade2)/2
  def ListAttributes(self):
    return f'id: {self.id} name: {self.name} grade1: {self.grade1} grade2: {self.grade2} average: {self.average}'
  
class Repository:
  studentList = []
  def AddStudent(self,student):
    self.studentList.append(student)

  def GetAll(self):
    return self.studentList

class Service:
  repo = Repository()
  def AddStudent(self,id,name,grade1,grade2):
    student = Student(id,name,grade1,grade2)
    self.repo.AddStudent(student)
    return 'Student added successfully'
  def GetAll(self):
    return self.repo.GetAll()

class MyUI:
  service = Service()
  
  def AddStudent(self):
    print('Enter ID:')
    id = input()
    print('Enter name: ')
    name = input()
    print('Enter grade 1:')
    grade1 = int(input())
    print('Enter grade 2: ')
    grade2 = int(input())
    print(self.service.AddStudent(id,name,grade1,grade2))

  def GetAll(self):
    for item in self.service.GetAll():
      print(item.ListAttributes())
    
  def MySwitch(self,option):
    return {
      '1': lambda: self.AddStudent(),
      '2': lambda: self.GetAll(),
      '3': 'You choose exit'
    }.get(option, lambda: None)
  
  def Start(self):
    while(True):
      print('Welcome to Student management')
      print('Choose an option: 1. Add Student / 2. List Students / 3. Exit')
      x = input()
      if x == '3':
        break
      if x == '1':
        self.AddStudent()
      if x == '2':
        self.GetAll()
    print('you are out of the while')
    
student = MyUI()
student.Start()