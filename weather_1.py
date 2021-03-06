# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:06:01 2018

@author: liuboming
"""
import pandas as pd
import csv, requests
from datetime import datetime

# token is required and can be obtained from https://www.ncdc.noaa.gov/cdo-web/token
myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
# an example url to fetch hourly temperature at a given station (seattle airport)
myUrl_1='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-TEMP-NORMAL&stationid=GHCND:USW00024233&startdate=2010-01-01&enddate=2010-02-01&limit=1000'
myUrl_2='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-WIND-AVGSPD&stationid=GHCND:USW00024233&startdate=2010-01-01&enddate=2010-02-01&limit=1000'
head={'token':myToken}
r1=requests.get(url=myUrl_1, headers=head)
r2=requests.get(url=myUrl_2, headers=head)
data1=r1.json()
data2=r2.json()
if data1=={} or data2=={}:
    print('no data avaliable for one of the url')
else :
    outputFile_1 = open("temperature_mean__sim.csv","w",newline='')
    outputWriter_1 = csv.writer(outputFile_1)
    keys=['time','value'] 
    outputWriter_1.writerow(keys)
    for dicts in data1['results']:
        row_arrayt=[]
        #remove the 'T' between date and time
        timestamp=dicts['date']
        timestampfixed=timestamp.replace("T", " ")
        row_arrayt.append(timestampfixed)
        row_arrayt.append(dicts['value'])
        outputWriter_1.writerow(row_arrayt)
    outputFile_1.close()
    
    outputFile_2 = open("windspeed_mean__sim.csv","w",newline='')
    outputWriter_2 = csv.writer(outputFile_2)
    keys=['time','value'] 
    outputWriter_2.writerow(keys)
    for dicts in data2['results']:
        row_arrayw=[]
        #remove the 'T' between date and time
        timestamp=dicts['date']
        timestampfixed=timestamp.replace("T", " ")
        row_arrayw.append(timestampfixed)
        row_arrayw.append(dicts['value'])
        outputWriter_2.writerow(row_arrayw)
    outputFile_2.close()


# linear interpolation
with open("temperature_mean__sim.csv") as f:
     reader = csv.reader(f)
     timestamp=[]
     temperature=[]
     for row in reader:
         #skip frist row
         if reader.line_num == 1:
             continue
         #read the timestamp after transfer the data type
         timestamp.append(datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
         temperature.append(row[1])        

with open("windspeed_mean__sim.csv") as f:
     reader = csv.reader(f)
     #timestamp=[]
     windspeed=[]
     for row in reader:
         #skip frist row
         if reader.line_num == 1:
             continue
         #read the timestamp after transfer the data type
         #timestamp.append(datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
         windspeed.append(row[1])     


# Creat a timeseries data      
dti=pd.to_datetime(timestamp)
ts1 = pd.Series(temperature, index=dti)
ts2 = pd.Series(windspeed, index=dti)
# upsample to every 5 minutes
s1=ts1.resample('300s').interpolate()
s2=ts2.resample('300s').interpolate()
# won't work without transfering to float
s1=s1.astype(float)
s2=s2.astype(float)
s1=s1.interpolate()
s2=s2.interpolate()
dt=pd.DataFrame(data={'temperature':list(s1.values), 'windspeed':list(s2.values)}, index=s1.index)
# pandas series to csv
dt.to_csv('5min_temp_wind.csv')
print('weather data in csv')