#           Python Begineer Boost

#           Polymorphism in Python


class Employee:
    def __init__(self,name,age,eid):
        self.name = name
        self.age = age
        self.eid = eid

    def introduce(self):
        print(f"My name is {self.name} and Id is {self.eid}")


class Student():
    def __init__(self,name,roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def introduce(self):
        print(f"{self.name} says greet")   


e1 = Employee("Shubham",21,'ABC123')
e1.introduce()

s1 = Student("Tom","Xyz121","CS101")
s1.introduce()