class Employee():
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

x = Employee()
x.a = 15

print(x.a)
x.show()