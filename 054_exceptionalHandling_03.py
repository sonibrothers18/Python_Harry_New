# custom exceptions using the ‘raise’ keyword

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"Division of a/b is {a/b}")