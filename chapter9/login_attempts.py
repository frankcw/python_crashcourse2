# login attempts


class User():
	"""Creating a class to store user information"""
	def __init__(self,first_name,last_name,location):
		self.first = first_name
		self.last = last_name
		self.loc = location
		self.log_attempts = 0

	def describe_user(self):
		# prints a summary of the user's information
		print(self.first.title() + ' ' + self.last.title() + 
			' lives in ' + self.loc.title() + '.')


	def greet_user(self):
		# prints a personalized greeting to the user
		print('Hello ' + self.first.title() + ', welcome to this page.')

	# login attempt methods
	def increment_login_attempts(self):
		# increases the attempts by 1
		self.log_attempts = self.log_attempts + 1

	def reset_login_attempts(self):
		self.log_attempts = 0



information = User('frank','cordova','new jersey')
information.describe_user()
information.greet_user()

information = User('claudia','rivadeneira','hawaii')
information.describe_user()
information.greet_user()

# login attempt instances
information.increment_login_attempts()
information.increment_login_attempts()
information.increment_login_attempts()
information.increment_login_attempts()
print("You have tried login a total of: " + str(information.log_attempts))

# reseting the amount of attempts
print("We are not going to reset the attempts.")
information.reset_login_attempts()
print("You have tried login a total of: " + str(information.log_attempts))
