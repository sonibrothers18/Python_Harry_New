error1 = "fail"
error2 = "ugly in class"
error3 = "bad boy"

statement = input("Enter your statement: ")

if((error1 in statement) or (error2 in statement) or (error3 in statement)):
    print("game over")
else:
    print("pass")