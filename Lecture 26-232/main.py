# LIST COMPREHENSION

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Nuray"
letters_list = [letter for letter in name]
print(letters_list)

# Python sequences:
# list
# range
# string
# tuple

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# CONDITIONAL LIST COMPREHENSION

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)
print(long_names)