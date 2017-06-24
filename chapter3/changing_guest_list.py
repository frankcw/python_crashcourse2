#changing guest list

guest_list = ['claudia','matteo','cira','franco','isabel','frank','pedro']

for name in guest_list:
	message = name.title() + " is invited to my house for a party!"
	print(message)

#removing an item from a list and using it in another statement
unavailable_guests = guest_list.pop(2)
print('\n' + unavailable_guests.title() + ' will not be able to assist')

#appending a new item to the list
guest_list.append('paul')

#printing out the new list with a message
for name in guest_list:
	message = name.title() + " is invited to my house for a party! This is the second list"
	print(message)