"""data visualization stuff"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get date, high and low temoeratures from file.
filename = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'

# Death Valley expansion
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)



# Stika Expansion
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)

    dates2, highs2, lows2 = [], [], []
    for row2 in reader2:
        try:
            current_date2 = datetime.strptime(row2[0], "%Y-%m-%d")
            high2 = int(row2[1])
            low2 = int(row2[3])
        except ValueError:
            print(current_date2, 'missing data')
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)


# Plot data: Death Valley.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates2, highs2, c='yellow', alpha=0.5)
plt.plot(dates2, lows2, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='green', alpha=0.1)


# Format plot.
title = "Daily high and low temperatures - Death Valley vs Sitka 2014"
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
