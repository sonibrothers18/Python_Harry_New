# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex():
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def showComplex(self):
        print(f"{self.r} + {self.i}i")

    def __add__(self, two):
        return f"{self.r + two.r} + {self.i + two.i}i" #! String can also be returned
    # todo str will used if return complex number itself
    
    # def __mul__(self, two):
    #     return f"(a + ib) (c + id) = (ac - bd) + i(ad + bc)"
    #     return f"{(self.r * two.r)}"


a = Complex(5, 8)
b = Complex(5, 2)
a.showComplex()
print(a + b)