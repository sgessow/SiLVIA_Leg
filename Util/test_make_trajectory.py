import Util.make_trajectory as trajectory

current_pos=[200,-30]
end_pos=[200,10]
angles, points=trajectory.make_trajectory(current_pos,end_pos,2)
new_points=trajectory.calculate_coordinates(angles)
trajectory.plot_trajectory(points)
trajectory.plot_trajectory(new_points)