from m_users import User
from m_privileges import Privileges

class Admin(User):
	def __init__(self,first_name,last_name="",location=""):
		super().__init__(first_name,last_name,location)
		# adding the new atrtribute that stores a list of strings
		self.first = first_name
		self.banner_of_priv = Privileges(self.first)