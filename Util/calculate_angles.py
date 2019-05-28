import sympy as sym
import mpmath as math
def calculate_angles_slow(Input_Cords):
    #Constants
    scalling_const=sym.sqrt(.3)
    f=195*scalling_const
    t=375*scalling_const

    f = f * (10 ^ -3)
    t = t * (10 ^ -3)

    t_1, t_2, x, y = sym.symbols("t_1, t_2,x,y")

    angles = sym.solve([f_x, f_y], [t_1, t_2])

    for coord in Input_Cords:
        X = (200-coord[0])*(10^-3)
        Y = coord[1]*(10^-3)

        # Convert to Meters
        f_x = f * sym.cos(t_1) + t * sym.cos(t_2) + X
        f_y = f * sym.sin(t_1) + t * sym.sin(t_2) + Y
        # Solve for t_1 and t_2 based on x and y

        if angles ==[]:
            print("Failed:" + str(X*(10^3))+', '+str(Y))
        else:
            print(angles[0],angles[1])


def calculate_angles(Input_Cords):
    # Constants
    scalling_const = sym.sqrt(.3)
    f = 195 * scalling_const
    t = 375 * scalling_const

    f = f * (10 ^ -3)
    t = t * (10 ^ -3)

    angle_list=[]

    for coord in Input_Cords:
        X = (200 - coord[0]) * (10 ^ -3)
        Y = coord[1] * (10 ^ -3)
        H=sym.sqrt(math.power(X,2)+math.power(Y,2))
        alpha=sym.acos((math.power(t,2)-math.power(f,2)-math.power(H,2))/(2*f*H))
        beta=sym.atan(Y/X)
        T_1=alpha-beta
        T_2=sym.acos((math.power(H,2)-math.power(f,2)-math.power(t,2))/(2*f*t))
        angles=[T_1,T_2]
        angle_list.append(angles)
    return angle_list