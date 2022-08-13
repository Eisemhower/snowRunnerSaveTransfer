# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:56:41 2022

@author: gmars
"""
import re


mySavePath = "C:/Program Files (x86)/Steam/userdata/46321573/1465360/remote/CompleteSave.cfg"
outpath = "./CompleteSave.cfg"
field = '"trucksInWarehouse":'


## Open my save and get the list of trucks in the warehouse
file = open(mySavePath, 'r')
mySave = file.read()
file.close()

# Get the truck list, excluding the inwarehouse bit.
exp= '("trucksInWarehouse":\[.+\}],)'
myTrucks  = re.findall(exp, mySave)[0]


# Now read other save.
outfile = open(outpath, 'r')
outSave = outfile.read()
outfile.close()

# Now find the warehouse field and transfer the trucks
exp = '"trucksInWarehouse":[],)'
outSave.replace(exp, myTrucks)

outfile = open(outpath, 'w')
outfile.write(outSave)
outfile.close()

