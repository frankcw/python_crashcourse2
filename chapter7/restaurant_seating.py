# restaurant seating

question = input('How many people are in the dinner group?: ')

if int(question) >= 8:
	print('You will have to wait to be seated.')
else:
	print("We are ready to seat you.")