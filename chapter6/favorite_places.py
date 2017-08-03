# favorite places

favorite_places = {'frank':['paris','london','hawaii'],'claudia':['guayaquil','new york'],'matteo':['barcelona']}

for k,v in sorted(favorite_places.items()):
	if len(v) > 1:		
		print('\n' + k.title() + "'s favorite places are: " )
		for place in v:
			print(place.title())
	else:
		print('\n' + k.title() + "'s favorite place is: ")
		for p in v:
			print(p.title())
