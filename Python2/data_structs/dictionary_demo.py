""" add following to existing dictionary

Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')


asia_countries = dict()
asia_countries['India'] = ['Bangalore']
locations['Asia'] = asia_countries

africa_countries = dict();
africa_countries['Egypt'] = ['Cairo']
locations['Africa'] = africa_countries

asia_countries['China']=['Shanghai']

print locations

print 1
usa_cities = []
for country in locations['North America']:
    for city in locations['North America'][country]:
        usa_cities.append(city)

for city in sorted(usa_cities):
    print city

print 2
asia_cities = []
for country in locations['Asia']:
    for city in sorted(locations['Asia'][country]):
        asia_cities.append(city + " - "+ country)

for city in sorted(asia_cities):
    print city
