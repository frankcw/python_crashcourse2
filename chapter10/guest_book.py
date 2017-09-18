# guest book

# write a while loop that prompts users for their name
# when they enter their name print a greeting to the screen
# also add a line recording their visit in a file called guest_book.txt
# make sure each eantry appears on a new line in the file


message = "Please enter your name (you can enter 'q' to exit at any time): "
# we need a variable to initialize the loop, it can't be empte/False

name = ' '

filename = 'guest_book.txt'
with open(filename, 'a') as file:
	file.write('Below is a list of guests:\n')


while name != 'q':

	name = input(message)

	if name == 'q':
		break

	print("Hello " + name.title() + ', welcome to the party!')

	with open(filename, 'a') as file:
		file.write(name.title() + "\n")


print("prgram ended")


