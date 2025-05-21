import json
import os

class Vehicle:
  def __init__(self, brand: str, model: str, color:str, price:int) -> None:
    self._brand = brand
    self._model = model
    self._color = color
    self._price = price

  def to_dict(self):
    return {'brand': self._brand,'model':self._model, 'color':self._color, 'price': self._price}

  def on_engine():
    pass
  
  def radio_on():
    pass
  pass


class User:
  def __init__(self, user: str, password:str, name:str, credit:int, fone:str, my_vehicles = {}) -> None:
    self._user = user
    self._password = password
    self._name = name
    self._credit = credit
    self._fone = fone
    self._id_vehicles = 0
    self._my_vehicles = my_vehicles


  def purchase_car(self, car: Vehicle) -> bool:
    if not self._credit > car._price:
      return False
    self._id_vehicles += 1
    self._my_vehicles[self._id_vehicles] = car.to_dict()
    return True

  def to_dict(self) -> dict:
    return {'user': self._user,'password':self._password, 'name':self._name, 'credit': self._credit, 'fone': self._fone, 'my_vehicles':self._my_vehicles}


class Dealership:
  def __init__(self) -> None:
    self._vehicles_avaibles: dict = {}
    self.add_vehicles()
    self._custumers: dict = {}
    self.add_custumers()
    pass

  def  view_vehicle():
    pass
  pass

  def add_vehicles(self) -> bool:
    car_1: Vehicle = Vehicle('Renault', 'Symbol','Plate', 900)
    car_2: Vehicle = Vehicle('Toyota', 'Yaris','White', 1000)
    car_3: Vehicle = Vehicle('Suzuki', 'Swift','Blue', 850)
    self._vehicles_avaibles['car_1'] = car_1.to_dict()
    self._vehicles_avaibles['car_2'] = car_2.to_dict()
    self._vehicles_avaibles['car_3'] = car_3.to_dict()
    return True
  
  def add_custumers(self) -> bool:
    user_1: User = User('yona','yona1234','yona',1000, '987654321')
    user_2: User = User('joan','joan1234','Joan',860, '987766442')
    self._custumers['user_1'] = user_1.to_dict()
    self._custumers['user_2'] = user_2.to_dict()
    return True
    

# this is an example how work
def Example1():
  user_1: User = User('yona','yona1234','yona',1000, '987654321')
  print(user_1.to_dict())
  car_1: Vehicle = Vehicle('Renault', 'Symbol','Plate', 900)
  car_1.to_dict()
  if not user_1.purchase_car(car_1):
    print('You require more credit')
  else: print(f'{user_1._name}, you bought the car {car_1._brand}, {car_1._model}, {car_1._color}, and now is on your collection')
  print(user_1._my_vehicles)

# Example1()

def Main():
  dealer: Dealership = Dealership()
  while(True):
    print('Welcome')
    try:
      option: int = int(input('Choose an option: 1 Vehicle available, 2 Contact us, 3 show your vehicles, 4. Exit program\n'))
    except Exception as e:
      print('Invalid option, try again. Error:',e)
      continue
    if option==4:
      print('closing program...')
      break
    elif option == 1:
      print('Vehicles avaible:')
      print(dealer._vehicles_avaibles)
  pass

Main()