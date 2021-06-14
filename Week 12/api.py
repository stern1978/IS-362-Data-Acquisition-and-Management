import os
import pandas as pd
import requests
import json

apiKey = os.environ.get('NYTimes_API')
link = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=' + apiKey
page = requests.get(link)
json = page.json()
results = page.json()['results']
topLen = list(range(len(results)))
topSites = []
x = 0
for site in topLen:
    topTitle = results[x]['title']
    x+=1
    topSites.append(topTitle)
print(topSites)
