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

import numpy as np
from matplotlib.dates import strpdate2num

time, temp = np.loadtxt('temperature_mean_seattleairport_sim.csv', skiprows=1,
        converters={2:strpdate2num('%H:%M:%S')}, unpack=True)


interp_time = np.linspace(time[0], time[-1], 100)
interp_temp = np.interp(interp_time, time, temp)
