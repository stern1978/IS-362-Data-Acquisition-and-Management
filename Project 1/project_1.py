import pandas as pd

airline = pd.read_csv('project_1.csv')
#print(airline)

airlineCopy = airline.copy()

airlineCopy['Total'] = airlineCopy.sum(axis=1)
airlineCopy['AvgDelay'] = airlineCopy['delayed']/airlineCopy['Total']*100
airlineCopy['AvgOnTime'] = airlineCopy['on time']/airlineCopy['Total']*100
#airlineCopy.loc[-1] = ['Total']
#print(airlineCopy)

airlineCopy.groupby(['Airline', 'City']).sum().sort_values(by=['Airline'])
print(airlineCopy)
