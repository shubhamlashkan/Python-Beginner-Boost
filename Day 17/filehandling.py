#           Python Begineer Boost

#           File Handling

#The open() function takes two parameters; filename, and mode.


"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

#file = open("example.txt",'x')

print("Reading complete file")
file = open("example.txt",'r')
print(file.read())
file.close()


print("Reading 5 character")
file = open("example.txt",'r')
print(file.read(5))
file.close()

print("Reading one line")
file = open("example.txt",'r')
print(file.readline())
print(file.readline())
file.close()


print("Reading using loop")
file = open("example.txt",'r')
for line in file:
    print(line)
file.close()



file = open("example.txt",'a')
file.write("Some content added using append mode.")
file.close()

file = open("example.txt",'r')
print(file.read())
file.close()



file = open("example.txt",'w')
file.write("Some content added using append mode.")
file.close()

file = open("example.txt",'r')
print(file.read())
file.close()