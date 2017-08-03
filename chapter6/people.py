# people

people = []

person1 = {'name':'frank','lname':'cordova','age':'27','city':'guayaquil'}
person2 = {'name':'matteo','lname':'cordova','age':'9','city':'south bound brook'}
person3 = {'name':'claudia','lname':'rivadeneira','age':'27','city':'palenque'}

people.append(person1)
people.append(person2)
people.append(person3)

for person in people:
	print( person['name'].title() +  ' ' + person['lname'].title() + 
		', age ' + person['age'] + ' lives in ' + person['city'].title() +
		'.')
