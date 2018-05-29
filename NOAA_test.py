"""
Created on Mon May 28 11:02:28 2018

@author: liuboming
"""
myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?datacategoryid=TEMP'

head={'token':myToken}
import requests, json, csv

r=requests.get(url=myUrl, headers=head)
data=r.json()

outputFile = open("Datasetsfottemp.csv","w")
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
        