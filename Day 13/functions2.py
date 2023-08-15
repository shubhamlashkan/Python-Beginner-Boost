#           Python Begineer Boost

#           Functions - Part 2

#def greet(lname, age,fname='Unknown'):
 #   print(fname)
 #   print(lname)
 #   print(age)

#greet('lashkan',20)
#greet('shubham ','lashkan',20)


#def greet(*fruits):
 #   print(fruits[2])

#greet('apple','orange','watermelon','lemon')


#def greet(lname, age,fname):
 #  print(fname)
  # print(lname)
 #  print(age)

#greet(fname='Shubham',lname="lashkan",age=31)


#def greet(**personInfo):
#    print(personInfo["fname"])


#greet(fname="shubham",lname='lashkan',age=21,subject="maths")


def average(mylist):
    sum = 0
    for num in mylist:
        sum = sum + num
    return sum
mylist = [1,2,3,4,5]
avg = average(mylist)/len(mylist)
print(avg)


mylist2 = [22,44,66,12,67]
avg = average(mylist2)/len(mylist2)
print(avg)