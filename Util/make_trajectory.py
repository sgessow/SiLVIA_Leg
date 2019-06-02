import mpmath as math
import Util.interpolation as interp
import matplotlib.pyplot as plt
import numpy as np


# Takes in coords relative to the foot and converts them to relative the body
def shift_coordinates(Input_Cords, distance_to_wall, vertical_offset):
    output_coord=[]
    for coord in Input_Cords:
        new_x=distance_to_wall-coord[0]
        new_y= coord[1] - vertical_offset
        output_coord.append([new_x,new_y])
    return output_coord


def calculate_angles(Input_Cords):
    # Constants
    scalling_const = np.sqrt(.3)
    f = 195 * scalling_const
    t = 375 * scalling_const

    f = f * (10 ^ -3)
    t = t * (10 ^ -3)

    angle_list=[]
    for coord in Input_Cords:
        X = (coord[0]) * (10 ^ -3)
        Y = (-coord[1]) * (10 ^ -3)
        H = np.sqrt(math.power(X,2)+math.power(Y,2))
        alpha = math.acos((math.power(t,2)-math.power(f,2)-math.power(H,2))/(2*f*H))
        beta = math.atan(Y/X)
        T_1 = alpha-beta+np.pi
        T_2 = math.acos((math.power(H,2)-math.power(f,2)-math.power(t,2))/(2*f*t))+np.pi
        angles=[T_1,T_2]
        angle_list.append(angles)
    return angle_list

def calculate_coordinates(input_angles):
    # Constants
    scalling_const = np.sqrt(.3)
    f = 195 * scalling_const * math.power(10,-3)
    t = 375 * scalling_const * math.power(10,-3)
    coord_list=[]
    for angle in input_angles:
        T_1=angle[0]-np.pi
        T_2=angle[1]-np.pi
        x=float((f*math.cos(T_1)+t*math.cos((T_1-T_2)))*math.power(10,3))
        y=float((f*math.sin(T_1)+t*math.sin((T_1-T_2)))*math.power(10,3))
        coord_list.append([x,y])
    return coord_list

def make_trajectory(current_point, ending_point, state=2, lift_height=30, steps=100):
    # State 0 is only the pull away and place on wall
    # state 1 is only push down
    # state 2 is both

    # starting point and ending point are given relative to the body, need to convert them to be relative to the foot
    current_point_b=current_point
    ending_point_b=ending_point
    x_shift=max([current_point_b[0],ending_point_b[0]])
    min_y=min([current_point[1],ending_point[1]])
    max_y=max([current_point[1],ending_point[1]])
    y_shift=-1*(min_y+max_y)/2
    current_point_l = [x_shift - current_point[0], current_point[1] + y_shift]
    ending_point_l = [x_shift - ending_point[0], ending_point[1] + y_shift]
    pts_l=[]
    if state == 0 or state==2:
        new_pts=interp.interpolate_Bspline(steps,current_point_l,ending_point_l,lift_height,False)
        pts_l=pts_l+new_pts
    #pts_l.reverse()
    if state==1 or state==2:
        new_pts=interp.interpolate_line(steps,ending_point_l,current_point_l)
        pts_l=pts_l+new_pts
    pts_b=shift_coordinates(pts_l,x_shift,y_shift)
    angles=calculate_angles(pts_b)
    return angles, pts_b


def plot_trajectory(pts):
    plt.plot([pts[i][0] for i in range(len(pts))],
             [pts[i][1] for i in range(len(pts))])
    plt.xlabel("x")
    plt.ylabel("z")
    # plt.xlim([-200, 10])
    # plt.ylim([-200, 200])
    plt.show(block=True)