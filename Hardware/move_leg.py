from robot_player import MotionManager, DxlOptions
import numpy as np
import platform
import Util.make_trajectory as trajectory


current_point=[200,-70]
end_point=[200,-30]
angles, point=trajectory.make_trajectory(current_point,end_point,2)
trajectory.plot_trajectory(point)


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

with MotionManager(motor_id, dt=dt, options=dxl_opts) as mm:
    mm.torque_on([1])
    mm.torque_on([2])
    for pos in angles:
        mm.set_goal_position([2], [pos[0] + np.pi])
        mm.set_goal_position([1], [pos[1] + np.pi])
        mm.wait(0.01)