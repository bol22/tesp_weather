# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:17:35 2018

@author: liub725
"""
import requests, json, csv

# token is required and can be obtained from https://www.ncdc.noaa.gov/cdo-web/token
myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
# an example url to fetch hourly temperature at a given station (seattle airport)
#myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-TEMP-NORMAL&stationid=GHCND:USW00024233&startdate=2010-05-01&enddate=2010-06-01&limit=1000'
# find the stationid which support datasetid=NORMAL_HLY
myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=NORMAL_HLY&limit=1000'

head={'token':myToken}
r=requests.get(url=myUrl, headers=head)
data=r.json()

if data=={}:
    print('Wrong url, no data avaliable')
else :
    outputFile = open("stationid_with_houly_data.csv","w",newline='')
    outputWriter = csv.writer(outputFile)
    keys=['time','value'] 
    outputWriter.writerow(keys)
    for location in data['results']:
        row_array=[]
        for attribute in location:
            row_array.append(location[attribute])
        outputWriter.writerow(row_array)
    outputFile.close()
        

