# filter and transform in one line

words: list = ['sun','sea','mountain','river','star']
print('words:', words)
# create a new list of words with more 3 words, like 'mountain','river' and 'star'
filter_words: list = [word for word in words if len(word) > 3]
print('filter_words:',filter_words)

# Creating a Dictionary with List Comprehension
# You have two lists, one of keys ["name", "age", "occupation"] and another of 
# values ​​["John", 30, "Engineer"]. Create a dictionary by combining both lists using List Comprehension.

keys: list = ["name", "age", "occupation"]
values: list = ["John", 30, "Engineer"]

contacts: dict = { keys[i]:values[i] for i in range(len(keys))}
print('contacts:',contacts)
print('name:',contacts['name'])
print(contacts['age'])

# Nesting List Comprehensions
# Given a list of lists (an array):

matrice: list = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# Calculates the transposed array using a nested List Comprehension.
print('normal')
for item in matrice: print(item)
matrice_transposed = [[item[i] for item in matrice] for i in range(len(matrice))]
print('transposed:')
for item in matrice_transposed: print(item)


#Extract Information from a List of Dictionaries
#Given a list of dictionaries representing people:

people = [
{"name": "John", "age": 25, "city": "Madrid"},
{"name": "Ana", "age": 32, "city": "Madrid"},
{"name": "Pedro", "age": 35, "city": "Barcelona"},
{"name": "Laura", "age": 40, "city": "Madrid"}
]
#Extract a list of names of people who live in "Madrid" and are over 30 years old.
filtered_people: list = [item for item in people if (item['city']== 'Madrid' and item['age']>30)]
for item in filtered_people: print(item)


# List Comprehension with an else clause
# Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list by multiplying 
# the even numbers by 2 and leaving the odd numbers as is.
numbers: list = [item for item in range(1,11)]
new_numbers: list = [item*2 if item%2==0 else item for item in numbers  ]
print(new_numbers)