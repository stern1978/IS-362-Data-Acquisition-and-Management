import pandas as pd
from random import randrange


avgMPH = 16 #found on internet
totalMiles = 1519 #from Google Maps
timeBiking = 8
distPerDay = avgMPH * timeBiking
daysNeeded = round(totalMiles / distPerDay)
days = list(range(1, daysNeeded + 1))
miles = []
sumMiles = []

for mile in days:
    rand = (randrange(round(distPerDay/1.1), round(distPerDay*1.1)))
    miles.append(rand)
    sumMile = sum(miles)
    sumMiles.append(sumMile)

pdSeries = pd.Series(sumMiles, index=days)
totalDistance = pd.DataFrame({'Day' : days, 'Odometer Reading' : pdSeries})
print(totalDistance)


dayMiles = []
x = 0
y = 0
pdlist = pdSeries.tolist()

try:
    for dist in pdlist:
        if pdlist[x] - pdlist[0] == 0:
            dd = pdlist[0]
            dayMiles.append(dd)
            x += 1
        else:
            dd = pdlist[x] - pdlist[y]
            dayMiles.append(dd)
            x += 1
            y += 1
except:
    pass

pdsMPD = pd.Series(dayMiles, index=days)

df = pd.DataFrame({'Day' : days, 'Miles per Day' : pdsMPD})
print(df)



