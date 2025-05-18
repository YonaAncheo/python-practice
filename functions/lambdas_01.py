example = lambda x,y:  x+y

result = example(3,4)

print(result)
print(example(5,2))

numbers: list = list(range(1,11))

squares = list(map(lambda x: x**2,numbers))

print('squares numbers', squares)

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print('even numbers',even_numbers)

# Factorial

def factorial (n:int) -> int:
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(f'Factorial 6 = {factorial(6)}' )

# Fibonacci
# Gauss wouldn't do it that way, but that's just an example.
def fibonacci(n: int) -> int:
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n + fibonacci(n - 1)
  
print(f'Fibonacci 6 = {fibonacci(6)}')