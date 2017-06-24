#shrinking guests lists using pop


guest_list = ['claudia','matteo','cira','franco','isabel','frank','pedro']
#original print statement
for name in guest_list:
	message = name.title() + " is invited to my house for a party!"
	print(message)

#new print statement
print("\nI have found a bigger table so there will be more guests.")

#additional guests inserted and appended
guest_list.insert(0,'carlos')
guest_list.insert(3,'david')
guest_list.append('jose')

#new list being printed
print("\nThis is the new list of guests:")
for name in guest_list:
	message = name.title() + " is invited to my house for a party!"
	print(message)

print("\nTHERE IS NOW AN ERROR IN THE RESERVATION\n I can only invite 2 people!\n")

#printing uninvitations
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message)
uninvited_guest = guest_list.pop()
message = uninvited_guest.title() + " is no longer invited, sorry."
print (message + "\n")

#list of people still invited

invited_guest = guest_list.pop()
message = invited_guest.title() + ' is invited to the party, congratulations!'
print(message)
invited_guest = guest_list.pop()
message = invited_guest.title() + ' is invited to the party, congratulations!'
print(message)

#printing empty list
print(guest_list)



