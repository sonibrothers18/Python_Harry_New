# Write a program to filter a list of numbers which are divisible by 5.

numbers = [4,5,55852,458,56952,84]

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

s = list(filter(divisible5, numbers))
print(s)