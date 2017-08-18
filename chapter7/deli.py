# deli 

sandwich_orders = ['turkey','ham','roast beef','tuna','chicken']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('Your ' + sandwich + ' sandwich is being made!')

	finished_sandwiches.append(sandwich)

print('\nThe below sandwiches have been completed:\n')
for sandwich in finished_sandwiches:
	print(sandwich.title())


