#more guests

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