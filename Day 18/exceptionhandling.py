#           Python Begineer Boost

#           Exception Handling

try:
    x = 10
    print(x)
except ZeroDivisionError:
    print("Divison by zero not possible")
except NameError:
    print("Variable x not defined")
else:
    print("Some code will execute if exception doesn't occur")
finally:
    print("This will always execute")
print("Hello World")


age = -1 
try:
    if age<0:
        raise ValueError("Age can't be negative")
except ValueError as error:
    print(error)