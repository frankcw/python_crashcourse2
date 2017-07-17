# buffet

foods = ('beef','pork','fish','chinese','vegetables')

for food in foods:
	print(food.title())

# python will reject this, because the list is a tuple.
# food[0] = 'meat'

# the only way to modify a tuple is by replacing it.

foods = ('eggs','soups','salads','vegan','drinks')
print("\nThis is the modified Tuple:")
for food in foods:
	print(food.title())
