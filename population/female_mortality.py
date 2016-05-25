"""Female mortality rates chart."""

import csv
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# Open file and extract data
filename = "life_female.csv"

with open(filename) as f:
    lifedata = csv.reader(f)

    # Get to the proper column line on the csv
    for n in range(1, 6):
        next(lifedata)

    # Make a new dictionary. Translate the country names
    # to country_codes, and put them in as keys and the
    # life expectancy data as values (taken from the 2014 data set)
    lrates = {}
    for rowdata in list(lifedata):
        ccode = get_country_code(rowdata[0])
        try:
            lrates[ccode] = float(rowdata[58])
        except ValueError:
            continue

# Plot new graph and output to file
wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Female Life Expectancy in 2014, by Country'

wm.add('Years', lrates)

wm.render_to_file('female_mortality.svg')
