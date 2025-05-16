# Calculator.

class Calculator:
  def __init__(self):
    self._a: float = 0
    self._b: float = 0
  
  def sum(a:float, b:float) -> float:
    return a+b
  
  def minus(a:float, b:float) -> float:
    return a-b
  
  def mult(a:float, b:float) -> float:
    return a*b
  
  def div(a:float, b:float) -> float:
    if b == 0: return None
    return a+b
  
def main() -> None:
  while(True):
    option: int = int(input('Basic Calculator\nChoose an option: 1 SUM, 2 MINUS, 3 MULT, 4 DIV, 5 EXIT:\n'))
    if option == 1:
      pass
    break
  pass