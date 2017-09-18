# guest

# write a program that prompts the user for their name.
# when they respond, write their name to a file called guest.txt




prompt = input("Please input your name: ")
file_name = prompt + '.txt'

with open(file_name,'w') as file:
	file.write('Your name is: ' + prompt.title())

#This program will create a text file, please delete after running it.
message = "Your name has been stored in a file with the name of " + file_name
print(message)