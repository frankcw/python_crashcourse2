# great magicians

def show_magicians(magicians_name):
	''' print the message for each item in the list'''
	for magician in magicians_name:
		print("Your magician's name is " + magician.title() + '.')

def make_great(magicians,newMagicians):
	''' move the items from the old list to the new one
	with the additional string'''
	while magicians:
		conversion = 'the Great ' + magicians.pop()
		newMagicians.append(conversion)


# specify the old list and the new list
name_list = ['carlos','juan','pedro']
final_name_list = []

# function to make them great
make_great(name_list,final_name_list)

# function to actually print the message
show_magicians(final_name_list)

# test to prove that the original list is now empty and got modified
# this list will be empty
#print(name_list)