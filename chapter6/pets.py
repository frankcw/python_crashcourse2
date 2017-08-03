# pets 

pets = []

billy = {'type':'dog','owner':'frank','color':'brown'}
laica = {'type':'dog','owner':'paul','color':'black'}
pony = {'type':'horse','owner':'claudia','color':'white'}

pets.append(billy)
pets.append(laica)
pets.append(pony)

for pet in pets:
	print('The ' + pet['type'] + ' belongs to ' + pet['owner'].title() + 
		' and its color is ' + pet['color'] + ".")
