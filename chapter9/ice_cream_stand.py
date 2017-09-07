# ice cream stand


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
restaurant.open_restaurant()

# new class for the excersise

class IceCreamStand(Restaurant):
	"""Class that inherits from the Restaurant Class, we are also 
	adding an attribute with a list called flavors."""
	def __init__(self,restaurant_name,restaurant_cuisine):
		super().__init__(restaurant_name,restaurant_cuisine)
		self.flavors = ['vanilla','chocolate','pistachio']

	def display_flavor(self):
		"""method that describes flavor"""
		for flavor in self.flavors:
			print("The flavor for your ice cream is: " + flavor + ".")


# create instance of IceCreamStand and call this method
ice_cream = IceCreamStand('baskin robins','ice cream')
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.display_flavor()
	
	
	