# checking usernames

current_users = ['Frank','claudia','matteo','franco','isabel']

new_users = ['frank','paul','ariana','diana','matteo']

for new_user in new_users:
	if new_user in current_users:
		print('You will need to enter a new username since this one is already taken: ' + new_user.lower())
	else:
		print("Username is available:" + new_user.lower())