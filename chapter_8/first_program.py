# create student class that takes name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average.

class Student:
    def __init__(self , name , phy , chem , math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    def calculate_average(self):
        avg =  (self.phy + self.chem + self.math) / 3
        print("the average marks of" , self.name , "is:" , avg)

s1 = Student("sweety", 1, 2, 3)
s1.calculate_average()

s2 = Student("monu", 5, 6, 4)
s2.calculate_average()