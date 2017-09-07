# number served

class Restaurant():
	''' simple Class to call restaurant with its information'''
	def __init__(self, restaurant_name, restaurant_cuisine):
		self.name = restaurant_name
		self.cuisine = restaurant_cuisine
		# new attribute to specify how many customers have been served.
		self.number_served = 0

	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + 
			" and we do " + self.cuisine + " food.")

	def open_restaurant(self):
		print("The " + self.name.title() + ' restaurant is now open.')

	def set_number_served(self,customers):
		# let me set the number of customer that have been served.
		self.number_served = customers

	def increment_number_served(self,customers_increment):
		# add the amount of customers that have come in.
		self.number_served += customers_increment

# instance to call Class
restaurant = Restaurant("little italy",'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# THESE ARE THE NEW ADDITIONS TO USE THE NEW METHODS
# new instances calling the number of customers that have been served
print("The restaurant has " + str(restaurant.number_served) + ' customers at the moment')
print("3 customers have just oredered something!")
restaurant.number_served = 3
print("The restaurant has " + str(restaurant.number_served) + ' customers at the moment')

# changing the number of customers by calling a method
restaurant.set_number_served(5)
print("The restaurant now has " + str(restaurant.number_served) + " customers.")

# incrementing the number of customers, to represent how many have come in through out the day
restaurant.increment_number_served(25)
print("The restaurant has ahd a total of " + str(restaurant.number_served) + " customers in the day!")
