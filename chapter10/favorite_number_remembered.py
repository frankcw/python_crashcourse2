# favorite number remembered

# combine two programs from 10-11 into one file. 
# If the number is already stored, report the favorite number to the user.
# if not, prompt for the user's favorite number and store it ina  file
# run the program twice to see that it works.

import json


filename = 'numbers.json'

try:
	with open(filename) as file_obj:
		favorite_number = json.load(file_obj)
		
except FileNotFoundError:
	# delete the file so that this can be tested.
	favorite_number = input("What is your favorite number?: ")
	with open(filename,'w') as file_obj:
		json.dump(favorite_number,file_obj)
	print("We will remmeber your favorite number next time you are back.")
else:
	print("I know your favorite number! It's " + favorite_number)	