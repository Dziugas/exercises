# dict comprehension
dict0 = {x: x.upper() for x in 'abcdefgh'}
print(dict0)

# we can swap keys and values
dict1 = {v:k for k,v in dict0.items()}
print(dict1)