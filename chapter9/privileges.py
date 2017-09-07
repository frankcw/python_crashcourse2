# privileges

# write a separate Privileges class
# Class should have one attribute, privileges, that stores a list of strings
# move the show_privileges() method to this class
# make a Privileges instance as an attribute in the Admin Class
# Create a new instance of Admin and user your method to show its privileges.

# This is the User Class
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


information = User('frank','cordova','new jersey')
information.describe_user()
information.greet_user()

# this is where I star the Admin class
class Admin(User):
	def __init__(self,first_name,last_name="",location=""):
		super().__init__(first_name,last_name,location)
		# adding the new atrtribute that stores a list of strings
		self.banner_of_priv = Privileges()


class Privileges():

	def __init__(self,privileges):
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		"""lists the set of privileges the admin has"""
		for privilege in self.privileges:
			print("the Admin user has the following privileges: " + privilege + ".")


admin_call = Admin('admin')
admin_call.describe_user()
admin_call.greet_user()
admin_call.show_privileges()