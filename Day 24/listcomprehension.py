#           Python Begineer Boost

#           List Comprehension in Python


numbers = [1,2,3,4,5]
square_number = []
for num in numbers:
    square_number.append(num**2)

sq_number  = [ num**2 for num in numbers]  
even_numbers = [num for num in numbers if num%2==0]

print(numbers)
print(sq_number)
print(even_numbers)

Names = ["Alice","Bob","charlie","David"]
name_length = [len(name) for name in Names]
print(name_length)