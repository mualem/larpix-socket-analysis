from subprocess import Popen, PIPE, CalledProcessError
import time, os, signal

cmd=['python print_time.py']
#cmd=["ls -al "]

start_time=time.time()

with Popen(cmd, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    FirstLine=True
    for line in p.stdout:
        if FirstLine :
          mypid=line # first line should just be the PID from the subprocess
          FirstLine=False
        print(line, end='') # process line here
        #pid=p.pid
        #print('PID=',pid)
        dt=time.time()-start_time
        print('dt=',dt)
        #if dt > 15 : p.kill()
        if dt > 15 : 
          # Get PID of process (set in print_time.py)
          #mypid=os.getenv('PRINT_TIME_PID')
          print('mypid in run_my_job is ',mypid)
          #p.terminate()
          #p.send_signal(9)
          #pid=p.pid
          #print('PID=',pid)
          #os.kill(pid) # this seems to kill the shell, not the process running
          os.kill(int(mypid),signal.SIGKILL)

print('p.returncode= ',p.returncode)
#if p.returncode != 0:
#    raise CalledProcessError(p.returncode, p.args)

print('I was still running')