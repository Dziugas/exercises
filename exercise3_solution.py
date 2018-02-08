a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(input("Please, enter a number: "))

def c(a):
    return [n for n in a if n<b]

print ("These are all the lower numbers than your number {}:\n{}\n"
       "that come from this list: {}".format(b, c(a), a))

