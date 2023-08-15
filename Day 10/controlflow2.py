#           Python Begineer Boost

#           Control Flow Statements 

#           Loops - while, for

#           Loop control statement

#while condition:
    # code if condition is true

#normal execution continues if condition evaluates to false


count = 0

while count<5:
    print('Subscribe to my channel')
    count = count + 1
    print(count)
print("Loop execution completed. Normal execution")


#for item in sequence:
    #code block to execute for each item in the sequence

#Out of the loop normal execution will begin

fruits = ["apple","banana","cherry","watermelon"]

for fruit in fruits:
    print(fruit)


# range(start,stop,step)
# 1, 5, 9, 13,
for num in range(1,22,4):
    print(num)


word = "Shubham Lashkan"

for char in word:
    print(char)