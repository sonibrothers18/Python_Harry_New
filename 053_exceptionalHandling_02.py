try:
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    print(a/b)

except ZeroDivisionError: 
    print("Second number can't be zero")

except TypeError: 
    print("Can't do this operation")

except: 
    print("Error in program") # All other exceptions are handled here.