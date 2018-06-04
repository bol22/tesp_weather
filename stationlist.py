# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:45:48 2018

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
    list_station=[]
    list_id=[]
    for dicts in data['results']:        
        list_station.append(dicts['name'])        
        list_id.append(dicts['id'])
    station_dict=dict(zip(list_id, list_station))
