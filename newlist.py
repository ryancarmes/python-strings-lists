x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort() # default sorts list from lowest value to highest
half = x[0:5]
x.insert(5, half)
for counter in range(0, 5):
    x.pop(0)
print x





