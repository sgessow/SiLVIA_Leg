from robot_player import MotionManager, DxlOptions
import numpy as np
import platform
import time



"""
Test a single chain of DXLs 
IDs: 1,2
USB port is /dev/ttyUSB0
Motors are MX28
"""
def read_pos(Q,duration=5,angles=[-1.18545]):
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

	# todo add support for multiple angle positions
	start_time=time.time()
	cur_time=start_time
	with MotionManager(motor_id, dt=dt, options=dxl_opts) as mm:
		for pos in angles:
			mm.set_goal_position([2], [np.pi - pos[0]])
			mm.set_goal_position([1],pos[1])
			line = []
			cur_time = time.time()
			cur_pos = mm.get_all_present_position()
			cur_pos[:] = [-x + 1 * np.pi for x in cur_pos]
			line.append("D")
			line.append(cur_time)
			line = line + cur_pos
			Q.put(line)
		mm.torque_off([1])
		while cur_time-start_time<duration:
			line=[]
			cur_time=time.time()
			cur_pos=mm.get_all_present_position()
			cur_pos[:] = [-x + 1*np.pi for x in cur_pos]
			line.append("D")
			line.append(cur_time)
			line=line+cur_pos
			Q.put(line)
			# mm.wait(.1)
	return True
