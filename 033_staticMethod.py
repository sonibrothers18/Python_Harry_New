# Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
# We did not need to pass the whole object

class Employee():

    @staticmethod
    def greet():
        print("Hello user")

a = Employee()
a.greet()