"""
Created on Mon May 28 11:02:28 2018

@author: liuboming
"""
import requests, json, csv

myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
# an example url to fetch hourly wind speed at a given station (seattle airport)
#myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-WIND-VCTSPD&stationid=GHCND:USW00024233&startdate=2010-05-01&enddate=2010-05-31&limit=1000'

# find the stationid which support datasetid=NORMAL_HLY
#myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=NORMAL_HLY&limit=1000'

# fetch all the data types
# myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?limit=1000'

# an example url to fetch hourly temperature at a given station (seattle airport)
myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-TEMP-NORMAL&stationid=GHCND:USW00024233&unit=metric&startdate=2010-05-01&enddate=2010-05-31&limit=1000'

head={'token':myToken}
r=requests.get(url=myUrl, headers=head)
data=r.json()

if data=={}:
    print('Wrong url, no data avaliable')
else :
    outputFile = open("temperature_mean_seattleairport.csv","w",newline='')
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
        