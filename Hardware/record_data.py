import sys
from multiprocessing import Process, Queue
import Hardware.measure_pos as measure_pos
import Hardware.read_serial_data as read_serial_data
import Util.interpolation as interp
import Util.make_trajectory as ang
import time
import csv
import matplotlib.pyplot as plt


csv_file_out='test_output.csv'
if len(sys.argv)>=2:
    csv_file_out=sys.argv[1]

start=[0,-20]
end=[0,80]
pts1=interp.interpolate_Bspline(100, start, end, 20,False)
pts2=interp.interpolate_line(100,end, start)
pts=pts1+pts2
angles, coord=ang.calculate_angles(pts)
# print(coord)
# plt.plot([coord[i][1] for i in range(len(coord))],
#          [coord[i][0] for i in  range(len(coord))])
# plt.xlabel("x")
# plt.ylabel("z")
# # plt.xlim([-200, 10])
# # plt.ylim([-200, 200])
# plt.show(block=True)

for a in angles:
     print(a)
Data=[]
q=Queue()
duration=5
arduino = Process(target=read_serial_data.read_serial, args=([q,duration]))
dyna = Process(target=measure_pos.read_pos, args=([q,duration,angles]))
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

