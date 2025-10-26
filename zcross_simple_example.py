#imports
import numpy as np

def zero_cross(ar_of_a_sampled_f):

    signs = np.sign(ar_of_a_sampled_f)


    sign_changes = np.diff(signs)
    ar_of_sign_change_indxs = np.nonzero(sign_changes)[0]
    return ar_of_sign_change_indxs

# input
v0=float(input())
# const
g=9.8 # m/s^2
t=np.arange(0,5,0.01)
y=-0.3+v0*t-0.5*g*t**2
## your code

t0, t1 = zero_cross(y)

time_of_flight= np.abs(t1-t0)

#output
print(f'time of flight: {time_of_flight:.5g} s')