# pizza toppings 


print('please enter "quit" to exit at any time')
question = "Please enter a pizza topping you would like: "


topping = " "


while topping != 'quit':
	topping = input(question)

	if topping != 'quit':
		
		print(topping.title() + ' has been added to your pizza.')
