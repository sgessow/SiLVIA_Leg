import sys
from multiprocessing import Process, Array, Value, Lock
import Hardware.record_pos as measure_pos
import Hardware.read_serial_data as read_serial_data
import Util.make_trajectory as trajectory
import time
import csv

# Things to change
current_point=[200,-70]
end_point=[200,-30]
csv_file_out='Data/1006_No_Spring_3.csv'
duration=6
turn_on_time=2

# Set up the csv file
if len(sys.argv)>=2:
    csv_file_out=sys.argv[1]

# Make the path for the leg
angles, point=trajectory.make_trajectory(current_point,end_point,2,27)
#trajectory.plot_trajectory(point)

Data=[]
val_arduino=Array('d', 6)
val_dyna=Array('d', 5)
new_val=Value('i',1)
lock=Lock()
lock1=Lock()

measure_pos.turn_on_motors(turn_on_time)
arduino = Process(target=read_serial_data.read_serial, args=([val_arduino,duration]))
dyna = Process(target=measure_pos.read_pos, args=([val_dyna,new_val,angles,duration]))
arduino.start()
dyna.start()


start_time=time.time()
cur_time=start_time
while(cur_time-start_time<duration):
    cur_time = time.time()
    with lock:
        if new_val.value:
            new_val.value = False
            line=[]
            arduino_data= [val_arduino[i] for i in range(6)]
            dyna_data=[val_dyna[i] for i in range(5)]
            angles_meas=[dyna_data[2],dyna_data[1]]
            angles_goal=dyna_data[3:]
            position=trajectory.calculate_coordinates([angles_meas,angles_goal])
            dyna_data=dyna_data[:3]+position[0]+position[1]
            line=arduino_data+dyna_data
            Data.append(line)


arduino.join()
dyna.join()
Data=Data[0:]
#Write to the CSV File
with open(csv_file_out, 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(Data)

