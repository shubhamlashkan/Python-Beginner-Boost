#           Python Begineer Boost

#           Data Structure List

fruits = ["apple","banana","cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)
fruits.append("watermelon")
print(fruits)
print(len(fruits))

vegetable = ["Potato","Tomato"]
print(vegetable)

combined_list = fruits + vegetable
print(combined_list)

combined_list.remove("Potato")
print(combined_list)
print(len(combined_list))

#Syntax : new_list = combined_list[start:end:step]

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
new_list = numbers[-7:-1:1]
print(new_list)