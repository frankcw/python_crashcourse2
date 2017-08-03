# polling

favorite_fruits = {'frank':'banana','matteo':'apple','claudia':'strawberry','syedur':'peanut'}

new_list = ['frank','matteo','paul','franco']

for k in sorted(favorite_fruits):
	if k in new_list:
		print(k.title() + ' has already taken the survey!')
	else:
		print(k.title() + ' has not yet taken the survey, please complete.')