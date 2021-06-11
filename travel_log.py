travel_log = [
	{
	'country_visited':'France',
	'cities_visited':['Paris','Lille','Dijon'],
	'total_visits': 12
	 },
	{
	'country_visited':'Germany',
	'cities_visited':['Berlin', 'Hamburg','Stuttgart'],
	'total_visits':7
	}
]

def add_new_country(country, cities, visits):
	new_dict = {}
	new_dict['country_visited'] = country
	new_dict['cities_visited'] = cities
	new_dict['total_visits'] = visits
	travel_log.append(new_dict)
	return travel_log


add_new_country(country = "Russia", visits =  2, cities = ["Moscow", "Saint Petersburg"])


print(travel_log)