#           Python Begineer Boost

#           Object Oriented Programming Part -2 

class Student:
    def __init__(self,name,age,roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.attendance = 0

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}, Attendance:{self.attendance}")

    def update_attendance(self,attended_classes):
        print("Update attendance is called")
        self.attendance = self.attendance + attended_classes

    def get_attendance_percentage(self,total_classes):
        if total_classes==0:
            return 0
        return (self.attendance/total_classes)*100

    def is_eligible_for_exam(self,percentage_criteria):
        return self.get_attendance_percentage(60)>percentage_criteria

student1 = Student('John Doe',20,"A123")
print("Student 1 Detail")
student1.display_info()
student1.update_attendance(40) #attendance = 15
student1.display_info()
attendance_percentage = student1.get_attendance_percentage(60)
print("Attendance Percentage: ",attendance_percentage)
print(student1.is_eligible_for_exam(60))



"""
attendance_percentage = student1.get_attendance_percentage(0)
print("Attendance Percentage:" ,attendance_percentage)
attendance_percentage = student1.get_attendance_percentage(30)
print("Attendance Percentage:" ,attendance_percentage)
"""





"""
student2 = Student('Jane Smith',21,"B123")
print("Student 2 Detail")
student2.display_info()
student2.attendance = 1
student2.display_info()"""