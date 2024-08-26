# else block will run if there is no error in try block

try:
    a = int(input("Enter your number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")