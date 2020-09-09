countries = {
    'mexico': 126,
    'chile': 18,
    'colombia': 49,
    'argentina': 44
}

country = input('Type a country: ')
try:
    value = countries[country.lower()]
except KeyError:
    print('There is not information about', country)
else:
    print('The total population of {} is {} million'.format(country, value))