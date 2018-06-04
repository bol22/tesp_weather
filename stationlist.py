# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:45:48 2018

@author: liub725
"""

import requests

# token is required and can be obtained from https://www.ncdc.noaa.gov/cdo-web/token
myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'

myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=NORMAL_HLY&limit=1000'
head={'token':myToken}
r=requests.get(url=myUrl, headers=head)
data=r.json()
list_station=[]
list_id=[]
for dicts in data['results']:        
    list_station.append(dicts['name'])        
    list_id.append(dicts['id'])
station_dict=dict(zip(list_id, list_station))
