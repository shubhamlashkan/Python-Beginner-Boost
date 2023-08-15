#           Python Begineer Boost

#           Lambda Expression
"""
number = [1,3,5,7,9,10,12,6,8,23]

def square(num):
    return num*num

mylist = list(map(square,number))
print(mylist)

def checkEven(num):
    return num%2==0

evenNumbers = list(filter(checkEven,number))
print(evenNumbers)


# lambda argument:expression
"""
#def square(num):
#    return num*num

square = lambda num:num*num

print(square(2))

number = [1,2,3,4,5]

mylist = list(map(lambda num:num*num,number))
print(mylist)

#def checkEven(num):
 #   return num%2==0

evenNumbers = list(filter(lambda num:num%2==0,number))
print(evenNumbers)