"""Display the result of die rolls in this script."""
import pygal

from die import Die

# Create a two D6 die.
die1 = Die()
die2 = Die()
# die3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
    result = die1.roll() * die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
min1 = ((die1.num_sides + 1) - die1.num_sides)
min2 = ((die2.num_sides + 1) - die2.num_sides)
# min3 = ((die3.num_sides + 1) - die3.num_sides)
min_result = min1 + min2
max_result = die1.num_sides * die2.num_sides

for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 die 1,000 times."
hist.x_labels = []
for i in range(min_result, max_result+1):
    hist.x_labels.append(i)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 times 2', frequencies)
hist.render_to_file('die_visual.svg')
