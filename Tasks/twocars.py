import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

#input
T1=float(input('enter T_one: '))
T2=float(input('enter T_two: '))
qn=int(input('enter question no.: '))

# your code
R = 40.0
w1 = 2*np.pi / T1
w2 = 2*np.pi / T2

# time used in Q1-Q3
t1 = T1 / 6.0
th1 = w1 * t1
th2 = w2 * t1

# Q1: position of car 1 at t = T1/6
X1 = R * np.cos(th1)
Y1 = R * np.sin(th1)

# Q2: straight-line (chord) distance between cars at t1
d = 2 * R * np.abs(np.sin(0.5 * (th2 - th1)))

# Q3: shortest arc distance along the circle at t1
dtheta = th2 - th1
# wrap to [-pi, pi] -> minimal angular separation
dtheta_min = ((dtheta + np.pi) % (2*np.pi)) - np.pi
s = R * np.abs(dtheta_min)

# Q4: first meeting time (numeric) on a fixed 0.01s grid,
#     pick the FIRST hit after t=0 where (Δθ mod 2π) ~ 0
dt = 0.01
t_grid = np.arange(0.0, 10*T2, dt)
dtheta_mod = ((w2*t_grid - w1*t_grid) % (2*np.pi))   # in [0, 2π)
eps = 1e-3
idx = np.where(dtheta_mod < eps)[0]
idx = idx[idx > 0]                 # exclude t=0
T3_numeric = t_grid[idx[0]] if idx.size > 0 else np.nan

# Q5: analytic meeting time (kept as before)
T3_analytic = (T1 * T2) / (T2 - T1)


#output
if qn==1:
    print(f'{X1:.5g},{Y1:.5g} m')
if qn==2:
    print(f'{d:.5g} m')
if qn==3:
    print(f'{s:.5g} m')
if qn==4:
    print(f'{T3_numeric:.5g}')
if qn==5:
    print(f

    {T3_analytic:.5g}')