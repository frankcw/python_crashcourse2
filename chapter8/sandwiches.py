# sandwiches

def make_sandwich(size,*ingredients):
	"""sumarize the sandwich we are about to make"""
	print ('\nMaking a ' + str(size) +
		'inch sandwich with the following ingredients: ')

	for ingredient in ingredients:
		print('- ' + ingredient.title())

make_sandwich(6,'tomatoe','ham','lettuce')
make_sandwich(12,'bacon','lettuce','tomatoe')
make_sandwich(6,'roast beef')