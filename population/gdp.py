"""Plot the nation's GDP to a map."""

import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# Load the population data into a list.
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

    # Build a dictionary of gdp_data.
    cc_gdp = {}
    for gdp_dict in gdp_data:
        if gdp_dict['Year'] == '2010':
            country_name = gdp_dict['Country Name']
            gdp = int(float(gdp_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_gdp[code] = gdp

# Group the countries into 3 gdp levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 1000000000:
        cc_gdp_1[cc] = gdp
    elif gdp < 10000000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp

# Plot and output to file
wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'World GDP in 2010, by Country'

wm.add('0-1bn', cc_gdp_1)
wm.add('1bn-1tr', cc_gdp_2)
wm.add('>1tr', cc_gdp_3)

wm.render_to_file('world_gdp.svg')
