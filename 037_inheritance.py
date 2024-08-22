class Employee():
    company = "Microsoft"
    def getDetail(self):
        print(f"Company is {self.company}")

class Programmer(Employee):
    def __init__(self, language):
        self.language = language
    
    def allInfo(self):
        print(f"Language is {self.language} and company is {self.company}")
    
a = Programmer("Python")
x = Employee()
a.allInfo()
print(a.company)
print(x.company)