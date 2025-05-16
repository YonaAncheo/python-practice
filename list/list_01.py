# excersices about list and list comprenhension.

numbs: list = [1,2,3,4,5]
print('numbs: ',numbs)
# creation list with list comprenhension
numbers: list = [num for num in range(1,11)]
print('numbers',numbers, sep=': ')
pair_numbers: list = [pairs for pairs in numbers if pairs%2 == 0]
print('pairs',pair_numbers, sep=': ')
odd_numbers: list = [odd for odd in numbers if odd%2 == 1]
print('odd: ',odd_numbers)