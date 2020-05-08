# 1.1 Simple
# range
list0 = [x for x in range(20)]
print(list0)

# conditions
list1 = [x for x in range(20) if 3 < x < 15]
print(list1)

# methods on objects
list2 = [x.upper() for x in 'abcdef']
print(list2)

# functions
list3 = [abs(x) for x in (1, 2, -3, -5, -8)]
print(list3)

# 1.2 Nested
# there is no limit to nesting list comprehensions
nested = [(x, y) for x in range(5) for y in range(10, 15)]
print(nested)

# the above is equivalent to
res = []
for x in range(5):
    for y in range(10, 15):
        res.append((x,y))
print(res)
print(res == nested)

# three levels deep
deeply_nested = [x*y*z for x in range(10) for y in range(10) for z in range(10)]
print(deeply_nested)

# the above is equivalent to
res = []
for x in range(10):
    for y in range(10):
        for z in range (10):
            res.append(x*y*z)
print(res)
print(deeply_nested == res)