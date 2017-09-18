# programming poll

# write a loop that asks people why they like programming
# each time someone enters a reason, add their reason the a file that stores all responses

print("You can enter 'q' to quit")
prompt = "why do you like programming?: "
answer = ' '

while answer != 'q':
	
	answer = input(prompt)
	if answer == "q":
		break

	with open('responses.txt','a') as file:
		file.write(answer.rstrip() + '\n')