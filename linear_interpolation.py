# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:52:51 2018

@author: liub725
"""

# linear interpolate for the hourly data to make 5 minutes data.
csvFile = open("temperature_mean_seattleairport_sim.csv", "r")
reader = csv.reader(csvFile)
list1=[]
for row in reader:
    list1.append(row)