class Employee():
    name = "mayur"
    salary = 1000

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        print("I am done")

a = Employee("alex", 9999, 24)
print(a.name, a.salary, a.age)