import sympy as sym

#Constants
g=9.81 #m/s^2
scalling_const=sym.sqrt(.3)
scalling_const_force=sym.sqrt(.3)
mass_robot=10.3; #kg
mu=.5
f=195*scalling_const
t=375*scalling_const
SAFTEY_FACTOR=1.25

# Inputs
# The distance from the center of the robot to the wall
X=200 #mm
# The distance the body is from the point of contact
Y=-30 #mm

# Convert to Meters
X=X*(10^3)
f=f*(10^-3)
t=t*(10^-3)
Y=Y*(10^-3)


# Solve for t_1 and t_2 based on x and y
t_1, t_2,x,y= sym.symbols("t_1, t_2, x, y", real=True)


f_x=f*sym.cos(t_1)+t*sym.cos(t_2)-X
f_y=f*sym.sin(t_1)-t*sym.sin(t_2)-Y

Angles=sym.nonlinsolve([f_x,f_y],[t_1,t_2])

print(Angles)
print(Angles[t_1])