# global is used to modify the value of global variable

a = 100
print(a)

def fun():
    global a
    a = 50
    print(a)

fun()
print(a)