# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:46:58 2018

@author: liub725
"""
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:06:01 2018

@author: liuboming
"""
import pandas as pd
import csv, requests
from datetime import datetime
#station id :GHCND:USW00024233
def downloadweather_NOAA(stationid, startdate, enddate):
# token is required and can be obtained from https://www.ncdc.noaa.gov/cdo-web/token
    myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
    # an example url to fetch hourly temperature at a given station (seattle airport)
    myUrl_1='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-TEMP-NORMAL&stationid='+stationid+'&startdate='+startdate+'&enddate='+enddate+'&limit=1000'
    myUrl_2='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_HLY&datatypeid=HLY-WIND-AVGSPD&stationid='+stationid+'&startdate='+startdate+'&enddate='+enddate+'&limit=1000'
    head={'token':myToken}
    r1=requests.get(url=myUrl_1, headers=head)
    r2=requests.get(url=myUrl_2, headers=head)
    data1=r1.json()
    data2=r2.json()
    if data1=={} or data2=={}:
        print('no data avaliable for one of the url')
    else:
               
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
  
    with open("temperature_mean__sim.csv") as f1:
         reader_1 = csv.reader(f1)
         timestamp=[]
         temperature=[]
         for row in reader_1:
             #skip frist row
             if reader_1.line_num == 1:
                 continue
             #read the timestamp after transfer the data type
             timestamp.append(datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
             temperature.append(row[1])        
    f1.close()
    
    with open("windspeed_mean__sim.csv") as f2:
         reader_2 = csv.reader(f2)
         #timestamp=[]
         windspeed=[]
         for row in reader_2:
             #skip frist row
             if reader_2.line_num == 1:
                 continue
             #read the timestamp after transfer the data type
             #timestamp.append(datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
             windspeed.append(row[1])     
    f2.close()
   
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
    s1=s1.interpolate(method='quadratic')
    s2=s2.interpolate(method='quadratic')
    dt=pd.DataFrame(data={'temperature':list(s1.values), 'windspeed':list(s2.values)}, index=s1.index)
    # pandas series to csv
    dt.to_csv('5min_temp_wind.csv')
    print('weather data in csv')

def _tests():
    # fetch the IDs of all the states 
	downloadweather_NOAA('GHCND:USW00024233','2010-05-01','2010-06-01')

if __name__ == '__main__':
	_tests()
