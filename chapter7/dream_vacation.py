# dream vacation

places = {}

print('please type "q" to quit the program at any given time')

# we create a flag for the while loop
polling = True

while polling:

	name = input("what is your name?:")
	response = input("where would you go in the world: ")
	places[name] = response

# we change the flag so that the whil loop breaks when the user has input "no"
	repeat = input('Would you like to input another person?(yes/no): ')
	if repeat == 'no':
		polling = False


print(places)