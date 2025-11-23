import numpy as np
#import matplotlib.pyplot as plt


def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

c=float(input("enter c: "))
qn=int(input("enter qn: "))

b=7e-5
m=2.7/1000
g=9.8
v0=10
alpha=15*np.pi/180

## your code and answers

dt = 1e-4
Tmax = 1.1

def calc_range(c_val):
    N = int(Tmax/dt) + 1
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)

    vx[0] = v0 * np.cos(alpha)
    vy[0] = v0 * np.sin(alpha)

    for i in range(N-1):
        v = np.hypot(vx[i], vy[i])
        drag_coeff = (b + c_val * v) / m
        ax = -drag_coeff * vx[i]
        ay = -g - drag_coeff * vy[i]
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt

    zc = zero_cross(y)
    if len(zc) >= 2:
        j = zc[1]
        x1, x2 = x[j], x[j+1]
        y1, y2 = y[j], y[j+1]
        if y1 == y2:
            return x1
        frac = y1 / (y1 - y2)      # לינארית ל-y=0
        return x1 + frac * (x2 - x1)
    else:
        return x[-1]

ANS1 = calc_range(0.0)   # סעיף 1: c=0
ANS2 = calc_range(c)     # סעיף 2: c מהקלט


#ouput
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')
