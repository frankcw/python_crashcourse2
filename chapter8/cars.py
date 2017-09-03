# cars

def build_car(man,mod,**car_information):
	'''build a dictionary for a car'''
	profile = {}
	profile['manufacturer'] = man
	profile['model'] = mod
	for k,v in car_information.items():
		profile[k] = v
	return profile

car_profile = build_car('subaru','outback',color='blue',tow_package=True)

print(car_profile)