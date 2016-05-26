'''Get the top 30 stories from hacker-news by comment and plot to graph'''

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter


def get_api_item(url):
    '''Make an API call and return the response object.'''
    r = requests.get(url)
    return r

# Initial url to use to make api call
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Process information about each submission.
# API call will return a list of IDs
submission_ids = get_api_item(url).json()

# Use the IDs returned above and loop through them
# to make new API calls the will return a dict item for each id (Top 30).
submission_dicts, titles = [], []
for sub_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(sub_id) + '.json'
           )
    # API call will return a dictionay item for each ID
    # in the list being for looped
    response_dict = get_api_item(url).json()

    # Append the dictionary title data to the titles list
    # for the chart x values below
    titles.append(response_dict['title'])

    # Make a new sub dictonary from response_dict containing
    # link and comment info. This will be appended to
    # submission_dict list and used as the data for the graph below
    submission_dict = {
        'xlink': 'http://news.ycombinator.com/item?id=' + str(sub_id),
        'value': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

# Sort everything in the dict list by comments after it is filled up
submission_dicts = sorted(
              submission_dicts,
              key=itemgetter('value'), reverse=True
              )

# Visualization stuff
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# Plot the chart
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Commented Disscussions on Hacker news'
chart.x_labels = titles
chart.add('', submission_dicts)

chart.render_to_file('hacker-news.svg')
