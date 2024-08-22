class Employee:
    name = "mayur"
    salary = 12541

    def getInfo(self):
        print(f"Salary of {self.name} is {self.salary}")

a = Employee()
a.getInfo() #? It means Employee.getInfo(a) that's why we use self