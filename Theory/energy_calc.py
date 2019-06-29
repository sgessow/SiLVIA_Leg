import matplotlib.pyplot as plt
import numpy as np
from numpy import array, cos, sin, pi

t_1=np.pi/3
t_2=np.pi/4
scalling_const = np.sqrt(.3)
f = 195 * scalling_const
t = 375 * scalling_const

f =np.float( f * (10 ^ -3))
t =np.float(t * (10 ^ -3))

J=np.array([[-f*sin(t_1)-t*sin(t_1-t_2), t*sin(t_1-t_2)], [f*cos(t_1)-t*cos(t_1-t_2), t*cos(t_1-t_2)]])
print(J)