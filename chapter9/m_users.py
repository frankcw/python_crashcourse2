class User():
	"""Creating a class to store user information"""
	def __init__(self,first_name,last_name,location):
		self.first = first_name
		self.last = last_name
		self.loc = location

	def describe_user(self):
		# prints a summary of the user's information
		if self.first == 'admin':
			print('Hello Admin!, welcome back')
		else:
			print(self.first.title() + ' ' + self.last.title() + 
				' lives in ' + self.loc.title() + '.')

	def greet_user(self):
		# prints a personalized greeting to the user
		print('Hello ' + self.first.title() + ', welcome to this page.')