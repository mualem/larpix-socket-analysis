import time
import os,sys

mypid=os.getpid()
os.environ['PRINT_TIME_PID']=str(mypid)

print(mypid)
print('mypid in print_time is ',mypid)


while 1:
  print('printing time every few seconds ',time.strftime("%H:%M:%S"),flush=True)
  time.sleep(3)
  print('printing time every few seconds ',time.strftime("%H:%M:%S"),flush=True)
  time.sleep(3)
  sys.exit(37)  