age = int(input("Enter your age: "))

if(age < 0):
    print("Invalid age")
elif(age >= 18):
    print("You can drive")
else:
    print("You can not drive")