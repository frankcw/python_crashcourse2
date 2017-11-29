# favorite number

# write a program that prompts for the user's favorite number
# use json.dump() to store this number in a file.
# write a separate program that reads in this value and prints the message:
# "I know your favorite number! It's ________"

import json

favorite_number = input("What is your favorite number?: ")

filename = 'numbers.json'

with open(filename,'w') as file_obj:
	json.dump(favorite_number,file_obj)

with open(filename) as file_obj:
	number_read = json.load(file_obj)
	print("I know your favorite number! It's " + number_read)	