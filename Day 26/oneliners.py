#           Python Begineer Boost

#           Python One Liners

# Swapping
a = 10
b = 15

print(a)
print(b)

a,b = b,a
print(a)
print(b)


# Reverse a String
name = "Shubham Lashkan"
print("Original ",name)
print("Reverse ",name[::-1])

# Sum List Elements
mylist = [10,12,24,27,28]
print(sum(mylist))

# Filter elements using list comprehension
scores = [60,80,86,96,100,25]
passing_scores = [score for score in scores if score>80]
print(passing_scores)

# Join List Element into String
mylist1 = ["subscribe","to","my","channel"]
message = ' - '.join(mylist1)
print(message)