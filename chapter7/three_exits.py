# while loop with a break statement

print('You can enter "quit" at any time to exit')

age = " "

while age:
	age = input('What is your age?: ')
	if age == 'quit':
		break

	else:
		if int(age) < 3:
			print('Your ticket is free.')
		elif int(age) < 13:
			print('Your ticket is $10')
		else: 
			print('Your ticket will cost $15')