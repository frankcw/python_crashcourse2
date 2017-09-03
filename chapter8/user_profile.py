# user porfile

def build_profile(first,last,**user_info):
	'''build a dictionary containing everythin we know abou a user'''
	profile = {}
	profile['first name'] = first 
	profile['last name'] = last

	for k,v in user_info.items():
		profile[k] = v
	return profile

user_profile = build_profile('frank','cordova',location ='ecuador',work='nasdaq')

print(user_profile)