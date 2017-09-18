# reading file

# print contents once by reading the entire file
# print contents once by looping over the file object
# print contents once by storing the lines in a list and working with them outside the with block

# reading the entire file
filename = 'learning_python.txt'

print("\nthe entire file")
with open(filename) as file_object:
	content = file_object.read()
	print(content.rstrip())
	
# reading the file by looping through each line

print('\nfile via loops')
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# reading the entire file storing the lines in a list

print('\nthe file via a list')
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())