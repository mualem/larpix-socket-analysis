import psycopg2
#from sqlalchemy import create_engine
import time
#import pandas as pd
import sys,os,re

#if len(sys.argv) < 2:
#	print("Enter file name on command line to add to database")
#	exit()
#filename = sys.argv[1]
#print(" processing file ",filename," now")
#exit()

#if filename[-4:] != 'html' :
#	exit('File must end in .html')
#ASICsn = re.split('\_|\.',filename)[-2] # Not sure why it is index -2 
#print('Running with ASICsn:',ASICsn)
#filedata = open(filename, 'rb').read()
#filedate = os.path.getctime(filename)
#filesize = os.path.getsize(filename)
#if filesize<1000 : exit('EXITING: File only ',filesize,' bytes')

#conn_string = 'postgresql://larpixtester:Lauritsen373@127.0.0.1/larpixtester'
#db = create_engine(conn_string)
#conn = db.connect()
#df = pd.read_csv(filename)
#df = pd.read_csv('bps-summary220110.csv')
#df = pd.read_csv('bps-summary220111.csv')
#df = pd.read_csv('bps-summary220120.csv')
#df = pd.read_csv('bps-summary220121.csv')
#df = pd.read_csv('bps-summary220125.csv')
#df.to_sql('to_sql_test', con=conn, if_exists='replace', index=False)
#df.to_sql('to_sql_test', con=conn, if_exists='append', index=False)

conn = psycopg2.connect(dbname="larpixtester",user="larpixtester",password="Lauritsen373",host="127.0.0.1")
try:
	cur = conn.cursor()
	cur.execute(""" SELECT plottime,\"ASICsn\",plotdata FROM bps_plots WHERE \"ASICsn\" = %s LIMIT 1 """,("0Z0180",))
	inblob=cur.fetchone()
	outfilename = "plot_" + inblob[1] + ".html"
	print("Writing ",outfilename)
	open(outfilename,'wb').write(inblob[2])
	#cur.execute("INSERT INTO bps_plots(plottime,\"ASICsn\",plotdata) " +
	#	"VALUES(%s,%s,%s)",
	#	(filedate, ASICsn, psycopg2.Binary(filedata)))
	conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
finally:
	cur.close()
	conn.close()

def write_blob(ASICsn, filename):
    """ insert a BLOB into a table """
    #conn = None
    try:
        # read data from a picture
        #drawing = open(path_to_file, 'rb').read()
        # read database configuration
        #params = config()
        # connect to the PostgresQL database
        #conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO part_drawings(part_id,file_extension,drawing_data) " +
                    "VALUES(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()