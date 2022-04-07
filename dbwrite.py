import psycopg2
from sqlalchemy import create_engine
import time
import pandas as pd
import sys

if len(sys.argv) < 2:
	print("Enter file name on command line to add to database")
	exit()
filename = sys.argv[1]
print(" processing file ",filename," now")
#exit()
conn_string = 'postgresql://larpixtester:Lauritsen373@127.0.0.1/larpixtester'
db = create_engine(conn_string)
conn = db.connect()
df = pd.read_csv(filename)
#df = pd.read_csv('bps-summary220110.csv')
#df = pd.read_csv('bps-summary220111.csv')
#df = pd.read_csv('bps-summary220120.csv')
#df = pd.read_csv('bps-summary220121.csv')
#df = pd.read_csv('bps-summary220125.csv')
#df.to_sql('to_sql_test', con=conn, if_exists='replace', index=False)
#df.to_sql('netconfig_test', con=conn, if_exists='append', index=False)
df.to_sql('bps_test', con=conn, if_exists='append', index=False)
