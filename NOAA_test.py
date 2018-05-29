myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=COOP:010008&units=metric&startdate=2010-05-01&enddate=2010-08-31&limit=1000'

head={'token':myToken}
import requests
import json
import csv

r=requests.get(url=myUrl, headers=head)
data=r.json()


outputFile = open("Data_temp.csv","w")
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
        