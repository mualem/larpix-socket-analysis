
import psycopg2
from sqlalchemy import create_engine
import time
import pandas as pd
import sys
import h5py
import plotly
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import csv
import numpy as np
from collections import Counter

NumASICchannels = 64
ShowPlots = False

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

	limitsdf=limitsdf.append({'versionname':'LArPix-v2b','Mean':MedMeanbyChan[chan],'maxMean':MaxMeanbyChan[chan],'minMean':MinMeanbyChan[chan],
	'Std':MedStdbyChan[chan],'maxStd':MaxStdbyChan[chan],'minStd':MinStdbyChan[chan],
	'ChanName':textchan,'Chan':chan},ignore_index=True)

# END Loading limits dataFrame
print(limitsdf)
#exit()

conn_string = 'postgresql://larpixtester:Lauritsen373@127.0.0.1/larpixtester'
db = create_engine(conn_string)
conn = db.connect()
limitsdf.to_sql('asic_bps_summary_thresh', con=conn, if_exists='append', index=False)

exit()

#print(limitsdf)
#fig1.show()
#plotly.offline.plot(fig5,filename="LimitsStdvsMean.html",auto_open=False )

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
		badChan =summaryFrame[ (summaryFrame['Chan']==chan) & ( ( (summaryFrame['Std']>MaxStd) | (summaryFrame['Std']<MinStd) )
				| ( (summaryFrame['Mean']<MinMean) | (summaryFrame['Mean']>MaxMean) ) ) ] # | (summaryFrame['Nent']==0) ) ]
		# This doesn't work because I loop over channels.  I need to do it all at once but can't figure out the syntax.
		#summaryFrame['badChan']=(summaryFrame['Chan']==chan) & ( ( (summaryFrame['Std']>MaxStd) | (summaryFrame['Std']<MinStd) )
		#		| ( (summaryFrame['Mean']<MinMean) | (summaryFrame['Mean']>MaxMean) ) )  # | (summaryFrame['Nent']==0) ) ]
		#print('badchancount=',summaryFrame[summaryFrame['badChan']==True].count())
		#print(badChan)
		#AllbadChan.append(badChan,ignore_index=True)
		AllbadChan=pd.concat([AllbadChan,badChan],ignore_index=True)

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

for chan in range(NumASICchannels):
	MaxMean = round(limitsdf['maxMean'][(limitsdf['Chan']==chan)].values[0],2)
	MinMean = round(limitsdf['minMean'][(limitsdf['Chan']==chan)].values[0],2)
	MaxStd = round(limitsdf['maxStd'][(limitsdf['Chan']==chan)].values[0],2)
	MinStd = round(limitsdf['minStd'][(limitsdf['Chan']==chan)].values[0],2)
	print('Range for chan ',chan,' Mean and Std= [',MinMean,',',MaxMean,'][',MinStd,',',MaxStd,']')
	goodChan =summaryFrame[ (summaryFrame['Chan']==chan) & ( ( (summaryFrame['Std']<=MaxStd) & (summaryFrame['Std']>=MinStd) )
				& ( (summaryFrame['Mean']>=MinMean) & (summaryFrame['Mean']<=MaxMean) ) ) ]
	AllGoodChan=pd.concat([AllGoodChan,goodChan],ignore_index=True)

