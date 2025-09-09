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
#from show_in_browser import show_df, show_plt_plot, show_px_plot

NumASICchannels = 64
ShowPlots = False

def selectFile(defaultFile):
	filetypes = (('hdf5 files','*.h5'),('csv files','*.csv'),('text files','*.txt'),('All files','*.*'))
	filename = fd.askopenfilename(
		title='File Name',
		initialdir='./data/',
		initialfile=defaultFile,
		filetypes=filetypes,
		multiple=True)
	return filename

inputH5files=selectFile('')
listlen=len(inputH5files)
if listlen<1:
	exit("Must enter one or more (with ctrl-click) files to use")
d = h5py.File(inputH5files[0],mode='r')
date = list(d['_header'].attrs.values())[0]   
d = d['packets']
print("read ",inputH5files[0]," with ",len(d)," packets")
h5asdf = pd.DataFrame(d[0:len(d)])
#h5datapackets=h5asdf[h5asdf['packet_type']==1] # select only data packets 1 for v3, 0 for <v3

h5asdf.to_csv('fulldf.csv')

