import pandas as pd

airportsOriginal = pd.read_csv('airports.csv')
airports = airportsOriginal.copy()

northernmost = airports.sort_values(by = 'lat', ascending = False)
filterednorth = northernmost[(northernmost['lat'] > 0) &
                             (northernmost['lon'] < 0) &
                             (northernmost['tz'] <= -5) &
                             (northernmost['tz'] >= -10)]
print(filterednorth.head())

easternmost = airports.sort_values(by = 'lon', ascending = False)
filteredeast = easternmost[(easternmost['lat'] > 0) &
                           (easternmost['lon'] < 0) &
                           (easternmost['tz'] <= -5) &
                           (easternmost['tz'] >= -10)]
print(filteredeast.head(5))

weatherOriginal = pd.read_csv('weather.csv')
wind = weatherOriginal.copy()
wind = wind.sort_values(by = 'wind_speed', ascending = False)
wind[(wind['month'] == 2) & 
     (wind['day'] == 12) & 
     (wind['year'] == 2013) &
     (wind['wind_speed'] < 231)].head(1)
print(wind)
