# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:11:17 2018

@author: liub725
"""
import pandas as pd
import csv, requests
from datetime import datetime

stationid='GHCND:USW00024233'
startdate='2010-05-01'
enddate='2010-06-01'

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
        
