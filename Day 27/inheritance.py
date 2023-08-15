#           Python Begineer Boost

#           Inheritance in Python

class Person:
    def __init__(self,name,age):
        print("Parent init is called")
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and age is {self.age}")




class Student(Person):
    def __init__(self,name,age,student_id,course):
        print('child init is called')
        super().__init__(name,age)
        self.student_id = student_id
        self.course = course

    def display_student_info(self):
        print(f"Student id: {self.student_id}")
        print(f"Course : {self.course}")
        print(f"Name: {self.name}")
    
    

p1 = Person("shubham lashkan",27)
p1.introduce()

s1 = Student("Tom cruise",67,'abx123','cs101')
s1.introduce()
s1.display_student_info()