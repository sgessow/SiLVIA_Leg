import sys
from multiprocessing import Process, Queue
import read_serial_data
import measure_pos
import time
import csv


csv_file_out='test_output.csv'
if len(sys.argv)>=2:
    csv_file_out=sys.argv[1]

Data=[]
q=Queue()
duration=5
arduino = Process(target=read_serial_data.read_serial, args=([q,duration]))
dyna = Process(target=measure_pos.read_pos, args=([q,duration]))
arduino.start()
dyna.start()
start_time=time.time()
cur_time=start_time
Last_A=[]
Last_D=[]
new_A=False
new_D=False
while(cur_time-start_time<duration):
    cur_time = time.time()
    if not q.empty():
        line=q.get()
        if line[0]=='A':
            Last_A=line
            new_A=True
        elif line[0]=='D':
            Last_D=line
            new_D=True
    if new_D and new_A:
        if abs(Last_D[1]-Last_A[1]>.1):
            print("Sampling Error!")
        else:
            line_to_append=Last_D[1:2]+Last_A[2:]+Last_D[2:]
            Data.append(line_to_append)
            new_A=False
            new_D=False


arduino.join()
dyna.join()
with open(csv_file_out, 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(Data)

