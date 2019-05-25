from robot_player import MotionManager, DxlOptions
import numpy as np
import platform
import time
import csv


"""
Test a single chain of DXLs 
IDs: 1,2
USB port is /dev/ttyUSB0
Motors are MX28
"""

motor_id = [1,2]
dt = .005

if platform.system() == 'Windows':
    ports = ['COM15']
else:
    ports = ['/dev/ttyUSB0']

dxl_str = "MX28"

dxl_opts = DxlOptions([motor_id],
            motor_types=[dxl_str],
            ports=ports,
            baudrate=3000000,
            protocol_version=2
           )
goal_pos=-1.18545
start_time=time.time()
cur_time=start_time
duration=10
Data=[]
with MotionManager(motor_id, dt=dt, options=dxl_opts) as mm:
	di=mm.device
	mm.torque_off([1])
	mm.set_goal_position([2],[np.pi-goal_pos])
	while cur_time-start_time<duration:
		cur_time=time.time()
		cur_pos=mm.get_all_present_position()
		#print(cur_time-start_time)
		#cur_vel=mm.get_all_present_velocity()
		Data.append(cur_pos)
		mm.wait(.1)
with open('test.csv', mode='w') as csv_file:
	writer=csv.writer(csv_file)
	for row in Data:
		writer.writerow(row)
csv_file.close()
    
   
    #assert(np.allclose(mm.get_all_present_position(), np.array([0, 0]), atol=.1))
    #print(mm.get_all_present_position())
