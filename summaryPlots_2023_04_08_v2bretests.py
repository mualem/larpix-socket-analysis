import pandas as pd
import h5py
import plotly
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import csv
import numpy as np
from collections import Counter
from tkinter import filedialog as fd

NumASICchannels = 64
ShowPlots = False

#varlist = []
#for chan in range(0,32): varlist.append('ch{:02d}'.format(chan))

#meandf = pd.read_csv("20200131_all78/means.csv")
#stddf = pd.read_csv("20200131_all78/sdevs.csv")
#nentdf = pd.read_csv("20200131_all78/nents.csv")
#meandf.plot.hist()
#fig = px.histogram(sdev)
#fig = px.histogram(stddf)
#fig.show()
#fig = px.histogram(stddf,x='ch00')
#fig.show()
#fig = px.histogram(meandf,x='ch00')
#fig.show()

#fig4 = go.Figure()
#for graph in varlist: fig4.add_trace(go.Histogram(x=nentdf[graph]))

#fig4.show()

#fig5 = px.scatter(x=meandf[],y=stddf[])
#fig3.update_layout(barmode="stack")
#fig3.update_layout(barmode="overlay")
#for graph in varlist: fig3.add_trace(go.Histogram(x=meandf[graph],xbins=dict(start=0,end=255,size=3)))

#fig3.show()

# reshape separate csvs to single summary.csv

#summaryFrame = pd.DataFrame(columns = ['runtime','Mean','Std','Nent','ChanName','Chan'])
#summaryFrame2 = pd.read_csv("20200204_tray1_summary.csv")
#summaryFrame = pd.read_csv("20200131_all78/summary.csv")
#summaryFrame = pd.read_csv("20200204_tray0_summary.csv")
#summaryFrame = pd.read_csv("20200206_boiling_pixel.csv")

# BATCH 1
BATCH1=False
#BATCH1=True
if BATCH1:
	summaryFrame = pd.read_csv("20200826_v2First38.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("20200829_2540-2629.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200830_2450-2539.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200828_2630-2719.csv"),ignore_index=True)

# BATCH 2
BATCH2=False
#BATCH2=True
if BATCH2:
	summaryFrame = summaryFrame.append(pd.read_csv("20200922_2449-2258.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200925_2257-2090.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200925_2089-1987.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200926_1986-1940.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20200928_1939-1843.csv"),ignore_index=True)
BATCH2Part2=False
#BATCH2Part2=True
if BATCH2Part2:
	summaryFrame = summaryFrame.append(pd.read_csv("20201002_1843-1820.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201003_1819-1730.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201004_1729-1640.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201007_1639-1548.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201015_1547-1440.csv"),ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201015_1439-1335.csv"),ignore_index=True)	
	summaryFrame = summaryFrame.append(pd.read_csv("20201016_1334-1266.csv"),ignore_index=True)	
	summaryFrame = summaryFrame.append(pd.read_csv("20201018_1265-1190.csv"),ignore_index=True)	
	summaryFrame = summaryFrame.append(pd.read_csv("20201018_1189-1134.csv"),ignore_index=True)	
	summaryFrame = summaryFrame.append(pd.read_csv("20201019_1133-1100.csv"),ignore_index=True)

# Compare brd3 vs brd4
brd3vbrd4=False
if brd3vbrd4:
	summaryFrame = pd.read_csv("20201002_brd3_brd4.csv") # insertion on each test

# Compare brd3 vs brd4
brdl3vbrdp5=False
if brdl3vbrdp5:
	summaryFrame = pd.read_csv("20201013_brdl3-brdp5.csv") # insertion on each test

BATCH3Part2=False
#BATCH3Part2=True
if BATCH3Part2:
	#summaryFrame = pd.read_csv("20201022_1099-1010.csv",dtype={'ChipSN':'string'})
	summaryFrame = summaryFrame.append(pd.read_csv("20201022_1099-1010.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201022_1009-0921.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201026_0919-0854.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201027_0853-0728.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201028_0727-0668.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201029_0667-0578.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201030_0577-0434.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201031_0433-0337.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201101_0336-0258.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20201101_0257-0200.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)

# Pkg BATCH 2
PkgBATCH2=False
if PkgBATCH2:
	summaryFrame = pd.read_csv("20210401_3089-3000.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("20210406_3198-3090.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210408_3406-3199.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210414_3490-3407.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210414_3629-3491.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210414_3767-3630.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210414_3899-3768.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)
	summaryFrame = summaryFrame.append(pd.read_csv("20210414_3989-3900.csv",dtype={'ChipSN':'string'})
			,ignore_index=True)


# v2b initial
v2bInitial=False
#v2bInitial=True
if v2bInitial:
	#summaryFrame = pd.read_csv("First180_chiphandlerWGroundfoot_2021_11_22.csv")
	#summaryFrame = pd.read_csv("First180_chiphandlerWGroundfoot_2021_11_23.csv")
	#summaryFrame = pd.read_csv("First360_chiphandlerWGroundfoot_2021_11_23.csv")
	summaryFrame = pd.read_csv("First540_20211209.csv") # used to set the limits
	#summaryFrame = pd.read_csv("Full540_2021_12_10.csv") # had some extra noise on 16 and 18 at some periods.


v2bModule2=False
if v2bModule2:
	summaryFrame = pd.read_csv("bps-v2b.csv")
	#summaryFrame = pd.read_csv("bps_summary_361-720.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps_summary_361-720.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220125.csv")
	#summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220125.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220315.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220315.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220316.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220316.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220321.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220321.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220322.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220322.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220324.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220324.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220325.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220325.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220328.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220328.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("bps-summary220329.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("bps-summary220329.csv"),ignore_index=True)


v2bModule2retest=False
if v2bModule2retest:
	summaryFrame = pd.read_csv("data/bps-summary220405.csv")
	#summaryFrame = pd.read_csv("data/bps-summary220406.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220406.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220407.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220407.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220408.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220408.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220411.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220411.csv"),ignore_index=True)

v2bModule2part2=False
if v2bModule2part2:
	summaryFrame = pd.read_csv("data/bps-summary220512.csv")
	#summaryFrame = pd.read_csv("data/bps-summary220512.csv")
	summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220513.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220513.csv")
	#summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220518.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220518.csv")
	#summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220408.csv"),ignore_index=True)
	#summaryFrame = pd.read_csv("data/bps-summary220411.csv")
	#summaryFrame = summaryFrame.append(pd.read_csv("data/bps-summary220411.csv"),ignore_index=True)

def selectFile(defaultFile):
	filetypes = (('csv files','*.csv'),('text files','*.txt'),('All files','*.*'))
	filename = fd.askopenfilename(
		title='Serial Number file name',
		initialdir='./data/',
		initialfile=defaultFile,
		filetypes=filetypes,
		multiple=True)
	return filename

inputCSVfiles=selectFile('')
listlen=len(inputCSVfiles)
if listlen<1:
	exit("Must enter one or more (with ctrl-click) files to use")
summaryFrame = pd.read_csv(inputCSVfiles[0])
if listlen>1:
	for filename in inputCSVfiles[1:]:
		#print(filename)
		summaryFrame = summaryFrame.append(pd.read_csv(filename),ignore_index=True)
# exit()

#tempFrm=summaryFrame[summaryFrame['Chan']==0].to_csv("concat_data.csv",mode='w')

# try to get ShortSN from the sequence
summaryFrame['ShortSN']=summaryFrame['ChipSN'].str[2:] # should get from 2 to the end, skip 0 and 1 item

MedMeanbyChan=[]
MaxMeanbyChan=[]
MinMeanbyChan=[]
MedStdbyChan=[]
MaxStdbyChan=[]
MinStdbyChan=[]


# standards from first 38, used for first 307 for module 0
#MeanMeanbyChan = [14.16, 14.23, 14.34, 14.44, 15.03, 15.83, -999., -999., -999., -999., 42.28, 22.95, 18.71, 14.53, 13.69, 14.06, 13.11, 14.02, 13.97, 15.42, 15.29, 16.25, -999., -999., -999., -999., 11.38, 11.91, 10.03, 9.92, 12.54, 11.96, 11.84, 14.35, 15.0, 14.16, 18.39, 21.74, -999., -999., -999., 9.03, 11.3, 11.37, 9.08, 11.57, 11.44, 8.96, 11.83, 11.7, 9.76, 11.25, 12.06, 11.47, -999., -999., -999., -999., 12.24, 12.7, 13.19, 12.44, 13.47, 13.59]
#StdMeanbyChan = [1.39, 1.44, 1.49, 1.8, 2.05, 5.58, -999., -999., -999., -999., 3.74, 2.7, 2.34, 2.19, 2.21, 2.29, 2.52, 2.68, 3.22, 4.1, 5.13, 8.02, -999., -999., -999., -999., 2.27, 2.06, 2.14, 2.04, 1.66, 1.91, 1.86, 1.64, 2.02, 2.19, 2.43, 3.78, -999., -999., -999., 3.73, 2.52, 1.74, 1.85, 1.47, 1.41, 1.58, 1.49, 1.43, 1.69, 1.74, 2.29, 2.73, -999., -999., -999., -999., 1.55, 1.42, 1.49, 1.34, 1.35, 1.36]
#MeanStdbyChan = [1.68, 1.28, 1.91, 1.85, 1.6, 2.61, -999., -999., -999., -999., 2.54, 1.79, 1.71, 1.81, 1.82, 1.92, 1.77, 1.44, 1.97, 1.77, 1.62, 1.9, -999., -999., -999., -999., 1.96, 1.25, 1.51, 1.6, 1.72, 1.67, 1.61, 1.51, 2.06, 1.49, 1.53, 2.17, -999., -999., -999., 1.46, 1.58, 1.13, 1.88, 1.94, 2.04, 1.13, 1.64, 1.71, 1.84, 1.63, 1.88, 2.94, -999., -999., -999., -999., 1.78, 1.97, 2.02, 1.82, 1.69, 1.39]
#StdStdbyChan = [0.06, 0.05, 0.09, 0.95, 0.44, 1.69, -999., -999., -999., -999., 0.2, 0.11, 0.11, 0.13, 0.12, 0.18, 0.25, 0.28, 0.34, 0.53, 0.69, 1.3, -999., -999., -999., -999., 0.36, 0.19, 0.17, 0.3, 0.1, 0.11, 0.09, 0.08, 0.08, 0.09, 0.11, 0.16, -999., -999., -999., 0.14, 0.11, 0.07, 0.95, 0.07, 0.06, 0.09, 0.5, 0.14, 0.4, 0.96, 3.62, 4.14, -999., -999., -999., -999., 1.07, 0.35, 0.74, 0.06, 0.06, 0.05]

# Load limits dataFrame Should do this from a file, or database at some point.

# standards used for first 307 for module 0 and 1

#MeanMeanbyChan=[14.07, 14.2, 14.27, 14.6, 15.34, 15.54, -999.0, -999.0, -999.0, -999.0, 42.58, 23.44, 19.02, 14.67, 14.19, 14.11, 13.18, 14.08, 14.2, 15.68, 15.45, 16.52, -999.0, -999.0, -999.0, -999.0, 11.48, 12.02, 10.47, 10.51, 13.3, 12.35, 12.34, 14.77, 15.06, 14.7, 18.25, 21.93, -999.0, -999.0, -999.0, 9.6, 11.35, 11.72, 9.15, 11.74, 11.8, 9.56, 12.02, 11.94, 9.9, 11.82, 11.92, 11.35, -999.0, -999.0, -999.0, -999.0, 12.2, 12.88, 12.98, 13.31, 13.55, 13.64]
#StdMeanbyChan=[1.69, 1.87, 1.98, 11.15, 1.96, 2.21, -999.0, -999.0, -999.0, -999.0, 2.59, 2.6, 2.14, 1.88, 1.79, 1.75, 1.79, 1.82, 1.78, 2.06, 8.48, 2.53, -999.0, -999.0, -999.0, -999.0, 1.7, 1.8, 1.68, 1.83, 1.76, 1.89, 1.59, 1.84, 1.77, 1.62, 1.54, 1.92, -999.0, -999.0, -999.0, 1.69, 1.65, 1.69, 1.79, 1.68, 1.7, 1.65, 1.65, 1.7, 1.66, 1.82, 1.72, 1.85, -999.0, -999.0, -999.0, -999.0, 7.76, 2.06, 1.8, 1.89, 1.65, 1.94]
#MeanStdbyChan=[1.36, 1.4, 1.46, 1.58, 1.9, 5.14, -999.0, -999.0, -999.0, -999.0, 3.71, 2.68, 2.31, 2.16, 2.18, 2.28, 2.45, 2.71, 3.16, 3.92, 4.86, 7.96, -999.0, -999.0, -999.0, -999.0, 2.26, 2.03, 2.11, 1.95, 1.65, 1.87, 1.83, 1.64, 1.99, 2.18, 2.39, 3.75, -999.0, -999.0, -999.0, 3.72, 2.47, 1.72, 1.64, 1.44, 1.37, 1.53, 1.37, 1.39, 1.61, 1.55, 1.65, 1.99, -999.0, -999.0, -999.0, -999.0, 1.37, 1.35, 1.35, 1.33, 1.32, 1.34]
#StdStdbyChan=[1.46, 4.34, 2.88, 2.83, 2.49, 2.45, -999.0, -999.0, -999.0, -999.0, 1.71, 4.55, 3.47, 2.85, 3.21, 3.17, 2.87, 3.44, 3.85, 3.71, 3.26, 4.39, -999.0, -999.0, -999.0, -999.0, 1.74, 1.88, 2.98, 2.74, 1.7, 2.6, 2.61, 1.66, 2.61, 2.77, 1.56, 1.43, -999.0, -999.0, -999.0, 1.87, 1.69, 1.6, 2.6, 1.49, 1.47, 2.77, 1.52, 1.88, 2.72, 1.38, 1.74, 2.19, -999.0, -999.0, -999.0, -999.0, 1.79, 1.65, 1.49, 1.86, 2.81, 4.21]

# standards measured from 540 v2b on the socket board.

MeanMeanbyChan=[16.68, 16.34, 16.62, 16.26, 16.78, 16.76, 16.81, 16.64, 11.97, 11.91, 12.68, 14.4, 14.79, 15.73, 15.93, 16.76, 16.96, 17.6, 17.47, 18.15, 17.86, 18.34, 18.23, 18.26, 17.3, 18.44, 18.19, 18.23, 17.74, 18.05, 17.38, 17.4, 17.13, 17.26, 16.98, 17.2, 16.76, 17.26, 17.03, 17.13, 18.6, 17.5, 17.18, 16.51, 16.68, 16.38, 17.01, 16.85, 17.03, 16.19, 16.48, 16.27, 16.49, 16.21, 16.94, 16.46, 16.81, 16.29, 16.61, 16.4, 16.54, 16.43, 16.64, 16.43]
StdMeanbyChan=[2.23, 2.35, 2.27, 2.29, 2.24, 2.36, 2.08, 2.19, 2.17, 2.05, 2.11, 2.27, 2.19, 2.21, 2.23, 2.11, 2.28, 2.3, 2.26, 2.15, 2.35, 2.29, 2.45, 2.42, 2.1, 2.18, 2.15, 2.12, 2.15, 2.2, 2.23, 2.09, 2.28, 2.1, 2.16, 2.18, 2.12, 2.1, 2.14, 2.19, 2.48, 2.22, 2.5, 2.29, 2.31, 2.27, 2.58, 2.47, 2.68, 2.26, 2.04, 2.22, 2.15, 2.19, 2.04, 2.14, 2.23, 2.28, 2.31, 2.38, 2.17, 2.17, 2.3, 2.28]
MeanStdbyChan=[1.08, 1.57, 1.45, 1.25, 1.42, 1.37, 1.15, 1.25, 1.75, 1.35, 1.14, 1.16, 1.39, 1.94, 1.21, 1.41, 1.01, 1.58, 1.16, 1.08, 1.38, 1.27, 1.26, 1.5, 1.35, 1.19, 1.16, 1.44, 1.37, 1.41, 1.34, 1.38, 1.31, 1.46, 1.7, 1.49, 1.3, 1.46, 1.59, 1.3, 1.95, 1.09, 1.14, 1.22, 1.04, 1.27, 1.3, 1.43, 1.32, 1.21, 1.1, 1.14, 1.17, 1.23, 1.13, 1.17, 1.2, 1.28, 1.3, 1.21, 1.25, 1.49, 1.21, 1.18]
StdStdbyChan=[0.2, 0.68, 0.57, 0.38, 0.55, 0.47, 0.27, 0.32, 0.85, 0.47, 0.27, 0.27, 0.52, 1.07, 0.35, 0.55, 0.16, 0.65, 0.3, 0.23, 0.49, 0.38, 0.38, 0.58, 0.36, 0.29, 0.28, 0.57, 0.49, 0.54, 0.46, 0.5, 0.43, 0.55, 0.75, 0.6, 0.42, 0.56, 0.65, 0.33, 0.27, 0.13, 0.24, 0.34, 0.18, 0.4, 0.45, 0.57, 0.46, 0.35, 0.25, 0.27, 0.28, 0.35, 0.24, 0.27, 0.18, 0.4, 0.43, 0.34, 0.39, 0.6, 0.35, 0.34]

MaxMeanbyChan=[18.91, 18.68, 18.89, 18.56, 19.02, 19.12, 18.89, 18.83, 14.14, 13.96, 14.79, 16.66, 16.98, 17.94, 18.16, 18.87, 19.24, 19.9, 19.73, 20.3, 20.21, 20.63, 20.67, 20.68, 19.4, 20.62, 20.34, 20.34, 19.89, 20.25, 19.6, 19.49, 19.41, 19.37, 19.14, 19.39, 18.88, 19.36, 19.17, 19.33, 21.07, 19.73, 19.68, 18.8, 18.99, 18.64, 19.59, 19.32, 19.71, 18.45, 18.52, 18.49, 18.63, 18.39, 18.98, 18.6, 19.05, 18.58, 18.92, 18.79, 18.7, 18.59, 18.94, 18.71]
MedMeanbyChan=[16.74, 16.36, 16.76, 16.34, 16.77, 16.85, 16.86, 16.55, 11.9, 11.94, 12.91, 14.25, 14.85, 15.75, 16.01, 16.72, 17.08, 17.5, 17.41, 17.99, 17.96, 18.34, 18.15, 18.38, 17.41, 18.45, 18.24, 18.28, 17.81, 17.96, 17.26, 17.39, 17.08, 17.23, 16.95, 17.15, 16.87, 17.28, 17.07, 17.14, 18.67, 17.45, 17.11, 16.48, 16.86, 16.37, 16.84, 16.47, 16.59, 16.31, 16.54, 16.31, 16.49, 16.21, 16.95, 16.54, 17.14, 16.32, 16.69, 16.43, 16.54, 16.33, 16.66, 16.46]
MinMeanbyChan=[14.45, 13.99, 14.35, 13.97, 14.54, 14.41, 14.74, 14.46, 9.81, 9.86, 10.58, 12.13, 12.59, 13.52, 13.71, 14.66, 14.69, 15.3, 15.21, 16.0, 15.51, 16.05, 15.78, 15.85, 15.21, 16.27, 16.04, 16.11, 15.59, 15.86, 15.15, 15.31, 14.85, 15.16, 14.83, 15.02, 14.63, 15.17, 14.9, 14.94, 16.12, 15.28, 14.69, 14.22, 14.37, 14.11, 14.43, 14.39, 14.34, 13.93, 14.44, 14.05, 14.34, 14.02, 14.91, 14.32, 14.58, 14.01, 14.3, 14.02, 14.37, 14.26, 14.34, 14.14]
MaxStdbyChan=[1.28, 2.24, 2.02, 1.64, 1.98, 1.85, 1.42, 1.56, 2.61, 1.82, 1.41, 1.43, 1.92, 3.0, 1.55, 1.96, 1.18, 2.23, 1.47, 1.31, 1.87, 1.66, 1.64, 2.08, 1.71, 1.48, 1.44, 2.01, 1.86, 1.94, 1.8, 1.88, 1.74, 2.01, 2.45, 2.08, 1.72, 2.03, 2.24, 1.63, 2.22, 1.22, 1.38, 1.57, 1.23, 1.67, 1.74, 2.01, 1.77, 1.57, 1.35, 1.42, 1.45, 1.58, 1.36, 1.43, 1.38, 1.68, 1.74, 1.55, 1.64, 2.09, 1.56, 1.52]
MedStdbyChan=[0.97, 1.17, 1.14, 1.02, 1.06, 1.09, 0.98, 1.03, 1.08, 1.02, 0.98, 0.99, 0.98, 1.06, 0.97, 1.05, 0.94, 1.23, 1.0, 0.92, 1.1, 1.0, 1.0, 1.27, 1.16, 1.01, 0.98, 1.0, 1.01, 1.0, 1.04, 1.04, 1.07, 1.11, 1.2, 1.03, 1.05, 1.07, 1.18, 1.1, 1.89, 1.03, 0.98, 0.99, 0.93, 0.98, 0.94, 0.99, 0.95, 0.94, 0.96, 0.97, 1.0, 0.98, 0.98, 0.96, 1.1, 0.98, 1.0, 1.01, 1.01, 1.11, 0.96, 0.97]
MinStdbyChan=[0.87, 0.89, 0.88, 0.87, 0.87, 0.9, 0.88, 0.93, 0.9, 0.88, 0.87, 0.88, 0.87, 0.87, 0.86, 0.86, 0.85, 0.93, 0.86, 0.85, 0.89, 0.89, 0.88, 0.92, 0.99, 0.9, 0.88, 0.87, 0.88, 0.87, 0.89, 0.88, 0.88, 0.91, 0.95, 0.89, 0.89, 0.9, 0.94, 0.97, 1.69, 0.96, 0.9, 0.88, 0.86, 0.87, 0.85, 0.86, 0.86, 0.86, 0.86, 0.87, 0.89, 0.88, 0.89, 0.9, 1.02, 0.88, 0.87, 0.87, 0.86, 0.89, 0.86, 0.85]

limitsdf=pd.DataFrame(columns=['Mean','maxMean','minMean','Std','maxStd','minStd','ChanName','Chan'])

for chan in range(NumASICchannels):
	#if MeanMeanbyChan[chan]!=-999.:
	textchan = 'ch{:02d}'.format(chan)
	#original 38 used these
	#errMean=3 * max(StdMeanbyChan[chan],4.0)
	#errStd=5 * max(StdStdbyChan[chan],0.7)
	#Module 0 and 1 used these:
	#errMean=1.0 * max(StdMeanbyChan[chan],10.0)
	#errStd=1.0 * max(StdStdbyChan[chan],3.0)

	windowminus=3.0
	windowplus=6.0
	MaxMeanbyChan[chan]=MedMeanbyChan[chan]+windowplus*(MaxMeanbyChan[chan]-MedMeanbyChan[chan])
	MinMeanbyChan[chan]=MedMeanbyChan[chan]-windowminus*(MedMeanbyChan[chan]-MinMeanbyChan[chan])
	MaxStdbyChan[chan]=MedStdbyChan[chan]+windowplus*(MaxStdbyChan[chan]-MedStdbyChan[chan])
	MinStdbyChan[chan]=MedStdbyChan[chan]-windowminus*(MedStdbyChan[chan]-MinStdbyChan[chan])
	# Hardcoded values had 417/530 pass, most failures, ~40 on channel 47
	#MaxMeanbyChan[chan]=30.0
	#MinMeanbyChan[chan]=7.0
	#MaxStdbyChan[chan]=9.0
	#MinStdbyChan[chan]=0.5
	# Try new fixed values for v2b second group
	MaxMeanbyChan[chan]=25.0
	MinMeanbyChan[chan]=5.0
	MaxStdbyChan[chan]=4.0
	MinStdbyChan[chan]=0.7

	limitsdf=limitsdf.append({'Mean':MedMeanbyChan[chan],'maxMean':MaxMeanbyChan[chan],'minMean':MinMeanbyChan[chan],
	'Std':MedStdbyChan[chan],'maxStd':MaxStdbyChan[chan],'minStd':MinStdbyChan[chan],
	'ChanName':textchan,'Chan':chan},ignore_index=True)

# END Loading limits dataFrame

#print(limitsdf)
#fig1.show()
#plotly.offline.plot(fig5,filename="LimitsStdvsMean.html",auto_open=False )

#exit()

CalculateNewMeansAndStd=0
if CalculateNewMeansAndStd:
	MedMeanbyChan=[]
	MaxMeanbyChan=[]
	MinMeanbyChan=[]
	MedStdbyChan=[]
	MaxStdbyChan=[]
	MinStdbyChan=[]
	# Clean the data
	summaryFrame=summaryFrame[(summaryFrame['Mean']<250) & (summaryFrame['Std']>0.1)]
	print('summaryFrame has',len(summaryFrame) ,' entries')
	for chan in range(NumASICchannels):

		MedMeanbyChan.append(round(summaryFrame['Mean'][summaryFrame['Chan']==chan].median(),2))
		MedStdbyChan.append(round(summaryFrame['Std'][summaryFrame['Chan']==chan].median(),2))

		MeanQtile=summaryFrame['Mean'][summaryFrame['Chan']==chan].quantile(q=[0.1,0.9])
		StdQtile=summaryFrame['Std'][summaryFrame['Chan']==chan].quantile(q=[0.1,0.9])

		MaxMeanbyChan.append(round(MeanQtile[0.9],2))
		MinMeanbyChan.append(round(MeanQtile[0.1],2))
		MaxStdbyChan.append(round(StdQtile[0.9],2))
		MinStdbyChan.append(round(StdQtile[0.1],2))

		print('{Max,Med,Min}Mean for Chan:',chan,'[',MaxMeanbyChan[chan],',',MedMeanbyChan[chan],',',MinMeanbyChan[chan],']')
		print('{Max,Med,Min}Std for Chan:',chan,'[',MaxStdbyChan[chan],',',MedStdbyChan[chan],',',MinStdbyChan[chan],']')

	print('{Max,Med,Min}Mean,{Max,Med,Min}Std')
	print(MaxMeanbyChan)
	print(MedMeanbyChan)
	print(MinMeanbyChan)
	print(MaxStdbyChan)
	print(MedStdbyChan)
	print(MinStdbyChan)

	exit()

fig2 = px.histogram(x=summaryFrame['Mean'],color=summaryFrame['ChanName'])
fig2.update_layout(barmode="stack",xaxis_title="Baseline Mean (ADC)")
if ShowPlots: fig2.show()
plotly.offline.plot(fig2,filename="Meanstack_bp.html",auto_open=False )

fig3 = px.histogram(x=summaryFrame['Std'],color=summaryFrame['ChanName'])
fig3.update_layout(barmode="stack",xaxis_title="Std Deviation (ADC)")
if ShowPlots: fig3.show()
plotly.offline.plot(fig3,filename="Stdstack_bp.html",auto_open=False )

fig5 = px.scatter(x=summaryFrame['Mean'],y=summaryFrame['Std'],color=summaryFrame['ChanName'])
fig5.update_layout(xaxis_title="Baseline Mean (ADC)",yaxis_title="Std Dev (ADC)")
if ShowPlots: fig5.show()
plotly.offline.plot(fig5,filename="StdvsMean_bp.html",auto_open=False )

fig1 = go.Figure()

for chan in range(NumASICchannels): #[0,1,2]:
	chanlimits=limitsdf[limitsdf['Chan']==chan]
	chanlimits.reset_index(drop=True)
	chanFrame=summaryFrame[summaryFrame['Chan']==chan]
	chanFrame.reset_index(drop=True)
	#print(chanlimits['Mean'])
	if MedMeanbyChan[chan]>0.:
		errYplus=chanlimits['maxStd']-chanlimits['Std']
		#print(errYplus)
		errYminus=chanlimits['Std']-chanlimits['minStd']
		errXplus=chanlimits['maxMean']-chanlimits['Mean']
		errXminus=chanlimits['Mean']-chanlimits['minMean']
		#fig1 = px.line(x=limitsdf['Mean'],y=limitsdf['Std'],error_x=limitsdf['errMean'],error_y=limitsdf['errStd'],color=limitsdf['ChanName'])
		#fig1.add_trace(go.scatter.Line(x=limitsdf['Mean'],y=limitsdf['Std'],error_x=limitsdf['errMean'],error_y=limitsdf['errStd'])) #,color=limitsdf['ChanName']))
		#fig1.add_trace(go.Scatter(name='ch{:02d}'.format(chan),mode='lines',
		#					x=chanlimits['Mean'],error_x=dict(type='data',symmetric=False,array=errXplus,arrayminus=errXminus,visible=True),
		#					y=chanlimits['Std'],error_y=dict(type='data',symmetric=False,array=errYplus,arrayminus=errYminus,visible=True),
		#						marker_color=px.colors.qualitative.Plotly[chan%10])) #,color=limitsdf['ChanName']))
		#fig1.update_layout(xaxis_title="Baseline Mean (ADC)",yaxis_title="Std Dev (ADC)")
		fig1.add_trace(go.Scatter(name='samp{:02d}'.format(chan),x=chanFrame['Mean'],y=chanFrame['Std'],mode='markers',
			marker_color=px.colors.qualitative.Plotly[chan%10])) #,color=summaryFrame['ChanName']))
		#print('Drawing box with x0 x1 y0 y1',chanlimits.at[chan,'minMean'],chanlimits['maxMean'],chanlimits['minStd'],chanlimits['maxStd'])
		# plot boxes doesn't get added to legend
		#fig1.add_shape(name='ch{:02d}box'.format(chan),type="rect",x0=chanlimits.at[chan,'minMean'], y0=chanlimits.at[chan,'minStd'], x1=chanlimits.at[chan,'maxMean'], y1=chanlimits.at[chan,'maxStd'],line=dict(color=px.colors.qualitative.Plotly[chan%10]),)
		# plot as scatter instead
		x0=chanlimits.at[chan,'minMean']
		x1=chanlimits.at[chan,'maxMean']
		y0=chanlimits.at[chan,'minStd']
		y1=chanlimits.at[chan,'maxStd']
		fig1.add_trace(go.Scatter(name='ch{:02d}box'.format(chan),x=[x0,x0,x1,x1,x0],y=[y0,y1,y1,y0,y0],mode='lines',
								line=dict(color=px.colors.qualitative.Plotly[chan%10])))
		#if chan==63: fig1.add_shape(type="rect",x0=15.0, y0=0.9, x1=18.0, y1=1.4,line=dict(color=px.colors.qualitative.Plotly[chan%10]),)

fig1.update_layout(xaxis_title="Baseline Mean (ADC)",yaxis_title="Std Dev (ADC)")
#fig1.update_shapes(dict(xref='x',yref='y'))
if ShowPlots: fig1.show()
plotly.offline.plot(fig1,filename="StdvsMean_bp_limits.html",auto_open=False )

fig6 = px.scatter(x=summaryFrame['runtime']-summaryFrame['runtime'][0],y=summaryFrame['Std'],color=summaryFrame['ChanName'])
fig6.update_layout(xaxis_title="Run Time(s)",yaxis_title="Std Dev (ADC)")
if ShowPlots: fig6.show()
plotly.offline.plot(fig6,filename="StdvsRuntime.html",auto_open=False )

fig7 = px.scatter(x=summaryFrame['runtime']-summaryFrame['runtime'][0],y=summaryFrame['Mean'],color=summaryFrame['ChanName'])
fig7.update_layout(xaxis_title="Run Time(s)",yaxis_title="Baseline Mean (ADC)")
if ShowPlots: fig7.show()
plotly.offline.plot(fig7,filename="MeanvsRuntime.html",auto_open=False )

#badChan = summaryFrame[(summaryFrame['Std']<1) | (summaryFrame['Mean']>240)]
#badChan.reset_index(drop=True)
badChan = summaryFrame[ (summaryFrame['Chan']==64) ]
AllbadChan = summaryFrame[ (summaryFrame['Chan']==64) ]
#print('badChan\n',badChan)

#pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)],ignore_index=True)
for chan in range(NumASICchannels):
	if MeanMeanbyChan[chan]!=-999:
		#	badChan = badChan + summaryFrame[ (summaryFrame['Chan']==chan) & ((summaryFrame['Std']<1) | (summaryFrame['Mean']>240)) ]
		#first versions, based on the 38
		#MaxMean = round(MeanMeanbyChan[chan] + 3 * max(StdMeanbyChan[chan],4.0),2)
		#MinMean = round(MeanMeanbyChan[chan] - 3 * max(StdMeanbyChan[chan],4.0),2)
		#MaxStd = round(MeanStdbyChan[chan] + 5 * max(StdStdbyChan[chan],0.7),2)
		#MinStd = round(MeanStdbyChan[chan] - 5 * max(StdStdbyChan[chan],0.7),2)
		#theMean=limitsdf['Mean'][(limitsdf['Chan']==chan)].values[0]
		#theStd=limitsdf['Std'][(limitsdf['Chan']==chan)].values[0]
		#theErrMean=limitsdf['errMean'][(limitsdf['Chan']==chan)].values[0]
		#theErrStd=limitsdf['errStd'][(limitsdf['Chan']==chan)].values[0]
		# This definition was used for the first 2x2 modules, 0 and 1
		#MaxMean = round(theMean + 2.0 * max(theErrMean,0.0),2)
		#MinMean = round(theMean - 2.0 * max(theErrMean,0.0),2)
		#MaxStd = round(theStd + 2.0 * max(theErrStd,0.0),2)
		#MinStd = round(theStd - 2.0 * max(theErrStd,0.0),2)
		# These were used for v2b ASICs with limits based on percentile 0.9
		#MaxMean = round(theMean + 1.0 * max(theErrMean,0.0),2)
		#MinMean = round(theMean - 1.0 * max(theErrMean,0.0),2)
		#MaxStd = round(theStd + 1.0 * max(theErrStd,0.0),2)
		#MinStd = round(theStd - 1.0 * max(theErrStd,0.0),2)
		MaxMean = round(limitsdf['maxMean'][(limitsdf['Chan']==chan)].values[0],2)
		MinMean = round(limitsdf['minMean'][(limitsdf['Chan']==chan)].values[0],2)
		MaxStd = round(limitsdf['maxStd'][(limitsdf['Chan']==chan)].values[0],2)
		MinStd = round(limitsdf['minStd'][(limitsdf['Chan']==chan)].values[0],2)
		print('Range for chan ',chan,' Mean and Std= [',MinMean,',',MaxMean,'][',MinStd,',',MaxStd,']')
		#badChan =summaryFrame[ (summaryFrame['Chan']==chan) & ((summaryFrame['Std']<1) | (summaryFrame['Mean']>240)) ]
		badChan =summaryFrame[ (summaryFrame['Chan']==chan) & ( (summaryFrame['Nent']==0) | ( (summaryFrame['Std']>MaxStd) | (summaryFrame['Std']<MinStd) )
				| ( (summaryFrame['Mean']<MinMean) | (summaryFrame['Mean']>MaxMean) ) ) ] # | (summaryFrame['Nent']==0) ) ]
		# This doesn't work because I loop over channels.  I need to do it all at once but can't figure out the syntax.
		#summaryFrame['badChan']=(summaryFrame['Chan']==chan) & ( ( (summaryFrame['Std']>MaxStd) | (summaryFrame['Std']<MinStd) )
		#		| ( (summaryFrame['Mean']<MinMean) | (summaryFrame['Mean']>MaxMean) ) )  # | (summaryFrame['Nent']==0) ) ]
		#print('badchancount=',summaryFrame[summaryFrame['badChan']==True].count())
		print(badChan)
		#AllbadChan.append(badChan,ignore_index=True)
		AllbadChan=pd.concat([AllbadChan,badChan],ignore_index=True)

#print('badchancount=',summaryFrame[summaryFrame['badChan']==True].count())

#summaryFrame['goodChan']= limitsdf['maxMean']['Chan'==summaryFrame['Chan']]
#print('summaryFrame\n',summaryFrame)
#(summaryFrame['Std']<=limitsdf[MaxStd][limitsdf['Chan'].values[0]==summaryFrame['Chan'].values[0]])
#	& (summaryFrame['Std']>=limitsdf[MinStd][summaryFrame['Chan']==limitsdf['Chan']]) )
#	& ( (summaryFrame['Mean']>=limitsdf[MinMean][summaryFrame['Chan']==limitsdf['Chan']]) 
#	& (summaryFrame['Mean']<=limitsdf[MaxMean][summaryFrame['Chan']==limitsdf['Chan']]) 

EmptyChan = summaryFrame[ (summaryFrame['Nent']==0) ] # Added this selection to badChan selection above
summaryFrame['emptyChan']=(summaryFrame['Nent']==0)
#print('EmptyChan\n',EmptyChan)

#AllbadChan=pd.concat([AllbadChan,EmptyChan],ignore_index=True)

#print('AllbadChan\n',AllbadChan)
t=AllbadChan.groupby(['ChipSN','runtime']).count()
#print(AllbadChan.groupby(['ChipSN','runtime']).count())
#print(t.shape)
#print(AllbadChan.groupby(['ChipSN','runtime']).size())

fig11 = go.Figure()

for chan in range(NumASICchannels): #[0,1,2]:
	chanlimits=limitsdf[limitsdf['Chan']==chan]
	chanlimits.reset_index(drop=True)
	chanFrame=AllbadChan[AllbadChan['Chan']==chan]
	chanFrame.reset_index(drop=True)
	#print(chanlimits['Mean'])
	if MedMeanbyChan[chan]>0.:
		errYplus=chanlimits['maxStd']-chanlimits['Std']
		errYminus=chanlimits['Std']-chanlimits['minStd']
		errXplus=chanlimits['maxMean']-chanlimits['Mean']
		errXminus=chanlimits['Mean']-chanlimits['minMean']
		#fig11.add_trace(go.Scatter(name='ch{:02d}'.format(chan),mode='lines',
		#					x=chanlimits['Mean'],error_x=dict(type='data',symmetric=False,array=errXplus,arrayminus=errXminus,visible=True),
		#					y=chanlimits['Std'],error_y=dict(type='data',symmetric=False,array=errYplus,arrayminus=errYminus,visible=True),
		#						marker_color=px.colors.qualitative.Plotly[chan%10])) #,color=limitsdf['ChanName']))
		fig11.add_trace(go.Scatter(name='samp{:02d}'.format(chan),x=chanFrame['Mean'],y=chanFrame['Std'],mode='markers',
			marker_color=px.colors.qualitative.Plotly[chan%10])) 
		# plot boxes doesn't get added to legend
		# plot as scatter instead
		x0=chanlimits.at[chan,'minMean']
		x1=chanlimits.at[chan,'maxMean']
		y0=chanlimits.at[chan,'minStd']
		y1=chanlimits.at[chan,'maxStd']
		fig11.add_trace(go.Scatter(name='ch{:02d}box'.format(chan),x=[x0,x0,x1,x1,x0],y=[y0,y1,y1,y0,y0],mode='lines',
								line=dict(color=px.colors.qualitative.Plotly[chan%10])))

fig11.update_layout(xaxis_title="Baseline Mean (ADC)",yaxis_title="Std Dev (ADC)")
if ShowPlots: fig11.show()
plotly.offline.plot(fig11,filename="MeanvsStd_bp_notbox.html",auto_open=False )


#fig8 = go.Figure()
#fig8.add_trace(go.Histogram(x=AllbadChan['ShortSN'],xbins=dict(size=1)))
#fig8.update_layout(xaxis_title="ChipSN",yaxis_title="Number Bad Channels")
#fig8.show()
#plotly.offline.plot(fig8,filename="BadChanvsChip_bp.html",auto_open=False )

#fig8 = px.histogram(x=pd.to_numeric(AllbadChan['ShortSN']),nbins=350,color=AllbadChan['ChanName'])
fig8 = px.histogram(x=AllbadChan['ShortSN'],nbins=350,color=AllbadChan['ChanName']).update_xaxes(categoryorder="category ascending")
fig8.update_layout(barmode="stack",xaxis_title="Chip SN",yaxis_title="Bad Channels")
if ShowPlots: fig8.show()
plotly.offline.plot(fig8,filename="BadChanvsChip_bp.html",auto_open=False )

fig81 = px.histogram(x=AllbadChan['Chan'],nbins=64)
fig81.update_layout(barmode="stack",xaxis_title="Channel",yaxis_title="Bad Channels")
if ShowPlots: fig81.show()
plotly.offline.plot(fig81,filename="BadChanvsChannel_bp.html",auto_open=False )

fig9 = px.scatter(x=summaryFrame['ShortSN'],y=summaryFrame['Std'],color=summaryFrame['ChanName']).update_xaxes(categoryorder="category ascending")
#fig9 = px.line(x=summaryFrame['ShortSN'],y=summaryFrame['Std'],color=summaryFrame['ChanName'])
fig9.update_layout(xaxis_title="ChipSN",yaxis_title="Std Dev (ADC)")
if ShowPlots: fig9.show()
plotly.offline.plot(fig9,filename="StdvsChip_bp.html",auto_open=False )

fig10 = px.scatter(x=summaryFrame['ShortSN'],y=summaryFrame['Mean'],color=summaryFrame['ChanName']).update_xaxes(categoryorder="category ascending")
#fig10 = px.line(x=summaryFrame['ShortSN'],y=summaryFrame['Mean'],color=summaryFrame['ChanName'])
fig10.update_layout(xaxis_title="ChipSN",yaxis_title="Baseline Mean (ADC)")
if ShowPlots: fig10.show()
plotly.offline.plot(fig10,filename="MeanvsChip_bp.html",auto_open=False )

goodChan = summaryFrame[ (summaryFrame['Chan']==64) ]
AllGoodChan = summaryFrame[ (summaryFrame['Chan']==64) ]
#print('goodChan\n',goodChan)

for chan in range(NumASICchannels):
	MaxMean = round(limitsdf['maxMean'][(limitsdf['Chan']==chan)].values[0],2)
	MinMean = round(limitsdf['minMean'][(limitsdf['Chan']==chan)].values[0],2)
	MaxStd = round(limitsdf['maxStd'][(limitsdf['Chan']==chan)].values[0],2)
	MinStd = round(limitsdf['minStd'][(limitsdf['Chan']==chan)].values[0],2)
	print('Range for chan ',chan,' Mean and Std= [',MinMean,',',MaxMean,'][',MinStd,',',MaxStd,']')
	goodChan =summaryFrame[ (summaryFrame['Chan']==chan) & ( ( (summaryFrame['Std']<=MaxStd) & (summaryFrame['Std']>=MinStd) )
				& ( (summaryFrame['Mean']>=MinMean) & (summaryFrame['Mean']<=MaxMean) ) ) ]
	AllGoodChan=pd.concat([AllGoodChan,goodChan],ignore_index=True)
print(AllGoodChan)
t2=AllGoodChan.groupby(['ChipSN','runtime']).count()
#print(AllGoodChan.groupby(['ChipSN','runtime']).count())
#print(t2.shape)

t2=t2[t2['Mean']==64]
#print (t2.shape)
#print(t2)

print('Number of Channels reported: ',summaryFrame.shape[0])
tt=summaryFrame.groupby('ChipSN').count()
print('Number of Chips tested: ',tt.shape[0])
tt=summaryFrame.groupby('runtime').count()
print('Number of Tests done: ',tt.shape[0])
#Number of Chips
#Number of channels
#Number of tests for chips
print('Number of Good Channels reported: ',AllGoodChan.shape[0])
tt=t2.groupby('ChipSN').count()
#print('tt\n',tt)
print('Number of Good Chips tested: ',tt.shape[0])
ttt=AllGoodChan.groupby(['runtime']).count()
ttt=ttt[ttt['Mean']==64]
#print('ttt\n',ttt)
print('Number of Good Tests done: ',ttt.shape[0])

print('Number of Bad Channels reported: ',AllbadChan.shape[0])
print('Number of Empty test channels: ',EmptyChan.shape[0])
t3=AllbadChan.groupby('ChipSN').count()
print('Number of Chips with a bad test: ',t3.shape[0])
t4=AllGoodChan.groupby(['ChipSN','runtime']).count()
print('Number of Bad Tests done: ',t4[t4['Mean']!=64].shape[0])

#print(tt['ChipSN'])

#print('AllbadChan\n',AllbadChan[AllbadChan.groupby('ChipSN') not in tt.index])
#print(tt.index)

badChiptot=0
for chip in t3.index: 
	if chip not in tt.index: 
		badChiptot=badChiptot+1
		#print('bad chip=',chip)

print('Number of bad chips: ',badChiptot)

EmptyChip=EmptyChan.groupby('ChipSN').count()
emptyChiptot=0
for chip in EmptyChip.index: 
	if chip not in tt.index: # tt.index is list of chips with a good test
		emptyChiptot=emptyChiptot+1
		#print('bad chip=',chip)

print('Number of Empty and bad chips: ',emptyChiptot)

print('\n\n\n List of ASICs with ALL good channels \n\n')
element=0
for SN in tt.index :
	element=element+1
	if element % 6  : print(SN,end=',')
	else : print(SN)

print('\n\n\n List of ASICs with only bad or empty channels \n\n')
badorempty = t3 + EmptyChip
for chip in badorempty.index:
	if chip not in tt.index :
		print(chip)

GoodResults=t2.groupby(['ChipSN','runtime']).count()
EmptyResults=EmptyChan.groupby(['ChipSN','runtime']).count()
BadOnlyResults=AllbadChan[ (AllbadChan['Nent']>0) ].groupby(['ChipSN','runtime']).count()

print('GoodResults',GoodResults)
print('EmptyResults',EmptyResults)
print('BadOnlyResults',BadOnlyResults)
