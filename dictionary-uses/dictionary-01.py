#creating a dictionay
information = [{
  'name': 'Jhon',
  'age': '30',
  'address': '22 Acacia Avenue',
},{
  'name': 'Sam',
  'age': '20',
  'address': '44 Campus Street',
}]

mySwitch = {
  1: lambda a: a + 2,
  2: lambda a: a**2,
  3: lambda a: 'this is a: '+str(a),
  4: False
}

def MySwitch(option,a):
  print(mySwitch[option](a))
  pass

myLambda = lambda a,b: a**b

while(True):
  print('enter a number in [1,2,3,4]')
  option = int(input())
  if option == 4:
    break
  print('enter a integer')
  a = int(input())
  MySwitch(option,a)

#print(mySwitch[1](a=2,b=3))
#print(mySwitch[2](3))
#print(mySwitch[3]('hello world'))
#print(myLambda(2,3))
#print('end')
#print(information)
#print(type(information))
#print(type(information[0]))
#print(information[0]['name'])
#print(len(information))
#or i in len(information)-1:
  #print(information[i]['name']) 