# multiple modules

from m_users import *
from m_admin import *
from m_privileges import *


call_admin = Admin('admin')
call_admin.banner_of_priv.show_privileges()