#           Python Begineer Boost

#           Set


#fruits = set(["apple","banana","cherry","apple","banana"])
fruits = {"apple","cherry","apple"}
print(fruits)



fruits.add('watermelon')
print(fruits)

fruits.remove('apple')
print(fruits)

set1 = {1,2,3,4}
print(set1)
set2 = {3,4,5,6}
print(set2)

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

difference = set2.difference(set1)
print(difference)