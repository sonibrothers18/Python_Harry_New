# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [151,2,481,54,6,28,56,4]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))