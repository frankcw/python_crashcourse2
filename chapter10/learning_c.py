# learning C

# read each line from the file you created and replace the work Python with 
# another language, like C

filename = 'learning_python.txt'

with open(filename) as file_object:
	content = file_object.read()
	content = content.replace('Python','C')
	
print(content.rstrip())