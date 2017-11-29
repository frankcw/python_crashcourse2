# cats and dogs

# write a program that tries to read these files and print the contents of the file to the screen
# wrap the code in a try-escept block to cath the FileNotFound error and print a message
# move one of the files to a different location and make sure the except block works


filename = 'cats.txt'
print('Below is a list of cat names: ')
# trying to open the file cats.txt, if the file doesn't exist you get a message.
try:
	with open(filename,'r') as file_object:
		contents = file_object.read()
		print (contents.strip())
except FileNotFoundError:
	print('The file ' + filename + " is not found, please check the name.") 

filename = 'dogs.txt'
print("Below is a list dog names: ")
# trying to open the file dogs.txt, if the file doesn't exist it will fail silently.
try:
	with open(filename,'r') as file_object:
		contents = file_object.read()
		print (contents.strip())
except FileNotFoundError:
	pass