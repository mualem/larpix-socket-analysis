import pandas as pd
import h5py
import plotly
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import csv
import sys
import numpy as np
from collections import Counter


def selectFile(defaultFile):
	filetypes = (('csv files','*.csv'),('text files','*.txt'),('All files','*.*'))
	filename = fd.askopenfilename(
		title='Serial Number file name',
		initialdir='./data/',
		initialfile=defaultFile,
		filetypes=filetypes,
		multiple=True)
	return filename

# if we get a parameter, assume that is the filename we will use, otherwise we'll pop up the tk dialog
print(sys.argv)
inputCSVfiles=[]
if len(sys.argv) >= 1 : #We got some arguments passed to our python code, it should be the input file
	inputCSVfiles.append(sys.argv[1])
	print("Using input file ",inputCSVfiles[0])
	listlen=1
else:
	from tkinter import filedialog as fd
	inputCSVfiles=selectFile('')
	listlen=len(inputCSVfiles)
	print('listlen=',listlen)
	print('inputCSVfiles=',inputCSVfiles)
	if listlen<1:
		exit("Must enter one or more (with ctrl-click) files to use")


NumASICchannels = 64
ShowPlots = False

netconfigFrame = pd.read_csv(inputCSVfiles[0])

if listlen>1:
	for filename in inputCSVfiles[1:]:
		#print(filename)
		netconfigFrame = netconfigFrame.append(pd.read_csv(filename),ignore_index=True)

print(netconfigFrame)
badchip = netconfigFrame[ (netconfigFrame['init_chip_results']!=64) ]
goodchip = netconfigFrame[ (netconfigFrame['init_chip_results']==0) ]

print(badchip)

badchipSN=badchip['ChipSN']
goodchipSN=goodchip['ChipSN']

GoodSNList=[]

GoodSNList=goodchipSN.drop_duplicates().to_list()

#print('GoodSNList=',GoodSNList)

summaryByChip=[]
for SN in GoodSNList:
    #summaryByChip.append((SN,'Good'))
    testtime=goodchip['TestTime'][(goodchip['ChipSN']==SN)]
    #print(testtime.iat[0])
    summaryByChip.append((SN,testtime.iat[0],'Good'))
BadSNList=[]

for SN in badchipSN.drop_duplicates().to_list() :
    if SN not in goodchipSN.drop_duplicates().to_list() :
        #print(SN)
        BadSNList.append(SN)
        #summaryByChip.append((SN,'Bad'))
        testtime=badchip['TestTime'][(badchip['ChipSN']==SN)]
        #print(testtime.iat[0])
        summaryByChip.append((SN,testtime.iat[0],'Bad'))

print('BadSNList=',BadSNList)
summaryByChip.sort()
#print(summaryByChip)
netsummary=pd.DataFrame(summaryByChip)
#print(netsummary)
summaryfilename=inputCSVfiles[0].replace("netconfig","netsummary")
netsummary.to_csv(summaryfilename,index=False,header=False)
