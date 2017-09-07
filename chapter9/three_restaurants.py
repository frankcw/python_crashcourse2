# three restaurants

class Restaurant():
	''' simple Class to call restaurant'''
	def __init__(self, restaurant_name, restaurant_cuisine):
		self.name = restaurant_name
		self.cuisine = restaurant_cuisine

	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + 
			" and we do " + self.cuisine + " food.")

	def open_restaurant(self):
		print("The " + self.name.title() + ' restaurant is now open.')

# instance to call Class
restaurant = Restaurant("little italy",'italian')
restaurant.describe_restaurant()

restaurant = Restaurant("shalimar",'indian')
restaurant.describe_restaurant()

restaurant = Restaurant("burger king",'burger')
restaurant.describe_restaurant()
