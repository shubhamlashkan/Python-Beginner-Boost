#           Python Begineer Boost

#           Dictionary Data Structure

student = {
    "name":"Shubham Lashkan",
    "age":27
}
print(student)
print(student["name"])
student["age"] = 28
print(student)
#print(student["major"])
student["major"] = "Computer Science"
print(student)
print(student["major"])

del student["age"]
print(student)


if "majo" in student:
    print(student["major"])
else:
    print("major information not available")