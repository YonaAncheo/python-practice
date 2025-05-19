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
    pass

  def  view_vehicle():
    pass
  pass
# this is an example how work
def Main():
  user_1: User = User('yona','yona1234','yona',1000, '987654321')
  print(user_1.to_dict())
  car_1: Vehicle = Vehicle('Renault', 'Symbol','Plate', 900)
  car_1.to_dict()
  if not user_1.purchase_car(car_1):
    print('You require more credit')
  else: print(f'{user_1._name}, you bought the car {car_1._brand}, {car_1._model}, {car_1._color}, and now is on your collection')
  print(user_1._my_vehicles)

Main()