# city names

def city_country(city,country):
	''' Neatly format the city and country '''
	full_location = city.title() + ', ' + country.title()
	return full_location

location = city_country('guayaquil','ecuador')
print(location)
location = city_country('new york','united states')
print(location)
location = city_country('hawaii','united states')
print(location)