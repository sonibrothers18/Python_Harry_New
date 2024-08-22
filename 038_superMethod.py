# It is used when we have to call the constructor of base class along with derived class

class Employee():
    def __init__(self):
        print("It is 1")

class Programmer(Employee):
    def __init__(self):
        print("It is 2")
        super().__init__()

a = Programmer()