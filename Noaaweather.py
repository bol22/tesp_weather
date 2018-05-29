# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:02:28 2018

@author: liuboming
"""
import requests, csv

def weatherNOAA(endpoints):
# base url and token
    myToken='GlQbxfsaOUPCWrtJylfRwRuXwAZJnyVK'
    myUrl='https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    head={'token':myToken}
    #json response from url
    r=requests.get(url='https://www.ncdc.noaa.gov/cdo-web/api/v2/' + endpoints, headers=head)
    data=r.json()
#write into csv
    outputFile = open("weather.csv","w")
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

def _tests():
    # fetch the IDs of all the states 
	weatherNOAA('locations?locationcategoryid=ST&limit=52')

if __name__ == '__main__':
	_tests()

