# imported admin

# store the classes User, Privileges, and Admin in one module
# make and Admin instance and call show_privileges() to show that everything is working correctly.

from privileges import User, Admin, Privileges

admin_call = Admin('admin')
admin_call.banner_of_priv.show_privileges()