# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator():
    
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"Square of {self.number} is {self.number**2}")

a = Calculator(6)
a.square()