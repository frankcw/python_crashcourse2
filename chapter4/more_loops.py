#loops

pizzas = ['pepperoni','ham','cheese']

friend_pizzas = pizzas[:]

pizzas.append('salami')
friend_pizzas.append('pine apple')

print("My favorite pizzas are : ")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas[-3:]:
