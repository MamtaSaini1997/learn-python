# define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
# create an Engineer class that inherit properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def ShowDetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, dept, salary):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age
    
    def show_det(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)

e1 = Engineer("sweety", 27, "employee", "coding", 50000)
e1.show_det()