
#imports
import numpy as np

def zero_cross(ar_of_a_sampled_f):
    #your code
    H1t = np.sign(ar_of_a_sampled_f)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]

# input
v0=float(input())
# const
g=9.8 # m/s^2
t=np.arange(0,5,0.01)
y=-0.3+v0*t-0.5*g*t**2

## your code

z_idx = zero_cross(y)
time_of_flight= t[z_idx[1]] - t[z_idx[0]]

#output
print(f'time of flight: {time_of_flight:.5g} s')