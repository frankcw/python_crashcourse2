# Hello Admin

users = ('fracor','syerah','britam','vaskri','admin')

for user in users:
	if user == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
		print('Hello ' + user.lower() + ", thank you for loggin in again.")