# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:52:51 2018

@author: liub725
"""

# linear interpolate for the hourly data to make 5 minutes data.
#csvFile = open("temperature_mean_seattleairport_sim.csv", "r")
#reader = csv.reader(csvFile)
#list1=[]
#for row in reader:
#    list1.append(row)
import pandas as pd
import csv
from datetime import datetime

with open('temperature_mean_seattleairport_sim.csv') as f:
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
# Creat a timeseries data      
ts = pd.Series(temperature, index=timestamp)
# upsample to every 5 minutes
s=ts.resample('300s').interpolate()
# won't work without transfering to float
s=s.astype(float)
s=s.interpolate()
# pandas series to csv
s.to_csv('5min_temp.csv')


## other option transfer from float to 
## s is the 5 minuts pd.series data
## obtain the datetime as a string and write into a new csv file
#dt=s.index.tolist()
#dtstring=[]
#for k in dt:
#    dtstring.append(k.strftime("%Y-%m-%d %H:%M:%S"))
#
#values=s.tolist()
#dt_values=dict(zip(dtstring,values))
#
#
#with open('dict.csv', 'w',newline='') as csv_file:
#    writer = csv.writer(csv_file)
#    for key, value in dt_values.items():
#        writer.writerow([key, value])
##for x in dt_values:
##    row_array=[]
##    for n in x:
##        row_array.append(x[n])
##    newFile.writerow(row_array)







#converted = ts.asfreq('5Min', method='linear')
#converted.head()
#
#df=pd.read_csv('temperature_mean_seattleairport_sim.csv')
#df['time'] = pd.to_datetime(df['time']) 
#df['date_delta'] = (df['date'] - df['date'].min())  / np.timedelta64(1,'D')
#
#interp_time = np.linspace(time[0], time[-1], 10)
#interp_temp = np.interp(interp_time, time, temp)
#data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
#        'battle_deaths': [34, 25, 26, 15, 15, 14, 26, 25, 62, 41]}
#df = pd.DataFrame(data, columns = ['date', 'battle_deaths'])
#print(df)
