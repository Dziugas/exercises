# 1. Use a list comprehension to convert a list of numbers from 10 to 50 into their squares if the numbers
# are even.

list0 = [i for i in range(10, 50)]
print(list0)

result_list0 = [i**2 for i in list0 if i % 2 == 0]
print(result_list0)

# 2. Write a nested list comprehension that iterates through the lists x, y and z each holding floats that
# represent coordinates. The comprehension should return a list with tuples of this three coordinates
# one from x, one from y, and one form z for all values of x that are within given limits you provide
import random
x = [random.uniform(0, 100) for i in range(0, 9)]
print(x)
y = [random.uniform(0, 100) for i in range(0, 9)]
print(y)
z = [random.uniform(0, 100) for i in range(0, 9)]
print(z)

result_list1 = [(item0, item1, item2) for item0 in x if 70 < item0 < 100 for item1 in y for item2 in z]
print(result_list1)

# 3. Write a dictionary comprehension (Python >= 2.7) or a generator expression that is converted into a
# dictionary (Python < 2.7) that goes through a list of numbers and uses the square of the number as
# key and the number itself as value.
list1 = [i for i in range(1, 11)]
print(list1)

result_dict0 = {i**2:i for i in list1}
print(result_dict0)
# change keys with values
result_dict1 = {v:k for k, v in result_dict0.items()}
print(result_dict1)

# 4. Write either (a) a set comprehension for Python >= 2.7 or (b) a generator expression that is converted
# into a set for Python < 2.7 that creates a set from a list of numbers turning negative numbers (that
# should be in the list) into positive numbers.

list2 = [i for i in range(-10, 0)]
print(list2)
set0 = {abs(z) for z in list2}
print(set0)


