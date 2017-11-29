# addition 

# write a program that prompts for two numbers
# add them together and print the resuilt
# catch the TypeError if either input values is not a number and print a friendly error message

while True:

	# requesting first number to add
	first_number = input('please enter the first number("q" to quit): ')
	if first_number == 'q':
		break


	second_number = input('please enter the second number("q" to quit): ')
	if second_number == 'q':
		break
	try:
		answer = (int(first_number) + int(second_number))
		print (answer)	
	except ValueError:
		print("You didn't place numbers!")