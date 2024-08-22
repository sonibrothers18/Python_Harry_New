class Employee:
    name = "mayur" # class attribute

a = Employee()
a.salary = 12450 # ! Instance(object) attribute
a.name = "Alex" #? Instance attributes, take preference over class attributes during assignment & retrieval.
print(a.name, a.salary)