# ### --easy--

# # print even numbers from list
# numbers = [1, 2, 3, 4, 5, 6, 0]
# print([n for n in numbers if n % 2 == 0 ])

# # abcabcabc +
# print(3 * 'abc')

# # How would you remove the last item from a list my_list in Python + pop use correct
# numbers.pop()
# print(numbers)

# # Write a simple for loop that prints the numbers 1 to 5
# for i in range(1, 6):
#     print(i)

# # How do you define a function in Python that takes two arguments and returns their sum? + 
# def sum_two(a, b):
#     return a+b
# print(sum_two(1, 2))

# # Given the dictionary my_dict = {'a': 1, 'b': 2, 'c': 3},
# # how would you access the value associated with the key 'b'
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict['b'])


### --medium--

# Write a list comprehension(compilation) that generates a list of squares for the numbers
# 1 through 10, but only for the even numbers.
print([n*n for n in range(1, 11) if n % 2 == 0])

# How would you reverse the string 'Python is fun!' in Python?
input_str = 'Python is fun!'
def reveres_string(input_str):
    return input_str[::-1]
print(reveres_string(input_str))

# Given two dictionaries, dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}, how would
# you merge them into one dictionary, with dict2 values overwriting dict1 in case of conflicts?
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(dict1 | dict2)

# Write a Python script that reads a file named data.txt and prints each line in uppercase.
def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read().upper())
read_file('test.txt')

# Define a class Dog with an attribute name. Add a method bark() that prints "<name> says woof!"
#  where <name> is the dog’s name.
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f'{self.name} says woof!')

dog_1 = Dog('Ko')
dog_1.bark()

print(dict1.keys())
