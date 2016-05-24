"""Need this to work out what the missing countries are fpr world pop.py."""

import json

from pygal.maps.world import COUNTRIES

# Open pop file
filename = 'population_data.json'
with open(filename) as f:
    pop = json.load(f)

# Build a dictionary of population data.
cc_pop = {}
for dict in pop:
    if dict['Year'] == '2010':
        country_name = dict['Country Name']
        population = int(float(dict['Value']))
        cc_pop[country_name] = population

# See if the country name for COUNTRIES is in cc_pop dictionary
# If not then output the COUNTRIES key/value pair to a new dictonary
# That will determine what is missing from the world graph
missing_countries = {}
for k, v in COUNTRIES.items():
    try:
        cc_pop[v]
    except KeyError:
        missing_countries[k] = v

# Out put the missing countries from COUNTRIES. These will have to be manually
# put into country codes
print(sorted(missing_countries.items()))
