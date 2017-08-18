# no pastrami

sandwich_orders = ['pastrami','turkey','pastrami','ham','roast beef','tuna','chicken','pastrami']
finished_sandwiches = []


print("The Deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

#print(sandwich_orders)

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('Your ' + sandwich + ' sandwich is being made!')

	finished_sandwiches.append(sandwich)

print('\nThe below sandwiches have been completed:\n')
for sandwich in finished_sandwiches:
	print(sandwich.title())	