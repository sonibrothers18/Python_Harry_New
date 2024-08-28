l = [1,2,3,4,5]

# map example
square = lambda x: x*x
sqList = map(square, l)
print(list(sqList))

# filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# reduce example
from functools import reduce
def sum(a, b):
    return a+b
print(reduce(sum, l))