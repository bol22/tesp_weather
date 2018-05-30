"""
Created on Mon May 28 11:02:28 2018

@author: liuboming
"""
import requests, json, csv

myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
#myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&stationid=COOP:010008&units=metric&startdate=2014-05-01&enddate=2014-05-10'
# find the stationid which support datasetid=NORMAL_HLY
myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=NORMAL_HLY&limit=1000'

head={'token':myToken}

r=requests.get(url=myUrl, headers=head)
data=r.json()

if data=={}:
    print('Wrong url, no data avaliable')
else :
    outputFile = open("stations_support_hourly_data.csv","w")
    outputWriter = csv.writer(outputFile)
    # obtain keys in the dict
    keys=list(data['results'][0].keys()) 
# write keys in the first line
    outputWriter.writerow(keys)

    for location in data['results']:
        row_array=[]
        for attribute in location:
            row_array.append(location[attribute])
        outputWriter.writerow(row_array)
#outputFile.close()
        