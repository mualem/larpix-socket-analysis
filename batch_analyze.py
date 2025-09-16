import pandas as pd
#import h5py
#import plotly
#import plotly.express as px
#import chart_studio
#import chart_studio.plotly as py
#import plotly.graph_objs as go
import csv
import sys
import numpy as np
#from collections import Counter

NumASICchannels = 64
ShowPlots = False

def selectFile(defaultFile):
	filetypes = (('csv files','*.csv'),('text files','*.txt'),('All files','*.*'))
	filename = fd.askopenfilename(
		title='Select netsummary<batch>.csv file name',
		initialdir='./data/',
		initialfile=defaultFile,
		filetypes=filetypes,
		multiple=False)
	return filename

# if we get a parameter, assume that is the filename we will use, otherwise we'll pop up the tk dialog
print(sys.argv)
if len(sys.argv) >= 1 : #We got some arguments passed to our python code, it should be the input file
	inputCSVfile=sys.argv[1]
	print("Using input file ",inputCSVfile)
	listlen=1
else:
	from tkinter import filedialog as fd
	inputCSVfile=selectFile('')
	listlen=len(inputCSVfile)
	print('listlen=',listlen)
	print('inputCSVfiles=',inputCSVfiles)
	if listlen<1:
		exit("Must enter one or more (with ctrl-click) files to use")


# read in the netconfig results (tuples) with each SN in the batch
netsummaryFrame = pd.read_csv(inputCSVfile,header=None,names=['ChipSN','nettesttime','netresult'])

#print(netsummaryFrame)

# read in the bps-summary csv file
bpsresultsfilename=inputCSVfile.replace("netsummary","bps-results")
bpsresultsFrame=pd.read_csv(bpsresultsfilename,header=None,names=['ChipSN','bpstesttime','bpsresult'])

#print(bpsresultsFrame)

overallresults=pd.merge(netsummaryFrame,bpsresultsFrame,on='ChipSN',how='outer')
print(overallresults)

outfilename=inputCSVfile.replace("netsummary","batchsummary")
overallresults.to_csv(outfilename,index=False)

print('Wrote overall results to ',outfilename)