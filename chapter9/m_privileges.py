class Privileges():

	def __init__(self,first):
		self.first = first
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		"""lists the set of privileges the admin has"""
		if self.first == 'admin':

			for privilege in self.privileges:
				print("the Admin user has the following privileges: " + privilege + ".")