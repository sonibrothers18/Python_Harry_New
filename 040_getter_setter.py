class Employee():
    a = 1

    @property
    def name(self):
        return self.fName, self.lName
        # return f"{self.fName} {self.lName}"
    
    @name.setter
    def name(self, value):
        self.fName = value.split(" ")[0]
        self.lName = value.split(" ")[1]

x = Employee()
print(x.a)

x.name = "mayur soni"
print(x.name)
print(x.fName)
print(x.lName)