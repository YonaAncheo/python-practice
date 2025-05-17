# Calculator.

class Calculator:
  def __init__(self):
    self._record: list = []

  def sum(self,a:float, b:float) -> float:
    return a+b
  
  def substract(self,a:float, b:float) -> float:
    return a-b
  
  def mult(self,a:float, b:float) -> float:
    return a*b
  
  def div(self,a:float, b:float) -> float:
    if b == 0: return None
    return a+b
  
  def save_operation(self, operation:str, a:float, b: float, result: float) -> None:
    self._record.append({'operation': operation, 'a': a, 'b': b, 'result': result})

  def somethig(self, a):
    pass
  
def main() -> None:
  calc: Calculator = Calculator()

  while(True):
    try:
      option: int = int(input('Basic Calculator\nChoose an option: 1 SUM, 2 MINUS, 3 MULT, 4 DIV, 5 List Record, 6 EXIT:\n'))
    except:
      print('INVALID INPUT')
      continue
    if option == 6:
      print('Closing app...')
      break

    elif option == 5:
      counter: int = 0
      print('Record:')
      for item in calc._record:
        counter += 1
        print(f'{counter}: {item}')
      input('Press enter for continue...')
      continue

    elif option not in [1,2,3,4]:
      print('INVALID OPTION')
      input('Press enter for continue...')
      continue
    
    while(True):
      try:
        a: float = float(input('Enter the first number: '))
        b: float = float(input('Enter the second number: '))
      except:
        print('Invalid option')
        continue
      break
    operations: dict = { 1: {'operation': 'sum', 'return':calc.sum(a,b)}, 
                    2: {'operation': 'subs', 'return': calc.substract(a,b)},
                    3: {'operation': 'mult', 'return': calc.mult(a,b)},
                    4: {'operation': 'divi', 'return': calc.div(a,b)}}
    result: float = operations[option]['return']
    calc.save_operation(operations[option]['operation'], a, b, result)
    print('the result is:',result)
    input('Press enter for continue...')

main()

    
    