"""portland rainfall."""
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'portland05.csv'

# open and extract the data
with open(filename) as f:
    r = csv.reader(f)
    # Move the dial up from the headers
    headers = next(r)
    # Append dates and rainfall values to a list
    dates, percip = [], []
    for row in r:
        try:
            thedate = datetime.strptime(row[0], "%m/%d/%Y")
            p = float(row[19])
        except ValueError:
            print(thedate, 'missing data')
        else:
            dates.append(thedate)
            percip.append(p)

# Plot rainfall
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, percip, c='red', alpha=0.5)

# Format plot.
title = "Rainfall Portland"
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Inches", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
