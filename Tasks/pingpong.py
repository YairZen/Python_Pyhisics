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
## your code and answers

dt = 1e-4
Tmax = 1.1

def trunc_5sf(x, n=5):
    # truncate to n significant figures (not round)
    if x == 0 or not np.isfinite(x):
        return x
    sign = 1.0
    if x < 0:
        sign = -1.0
        x = -x
    e = np.floor(np.log10(x))
    m = x / (10.0**e)
    s = np.floor(m * (10.0**(n-1)) + 1e-12)
    return sign * s * (10.0**(e-(n-1)))

def calc_range(c_val):
    N = int(Tmax/dt) + 1
    x = 0.0
    y = 0.0
    vx = v0 * np.cos(alpha)
    vy = v0 * np.sin(alpha)
    best_x = 0.0

    for _ in range(N-1):
        v = np.hypot(vx, vy)
        drag = (b + c_val * v) / m
        ax = -drag * vx
        ay = -g - drag * vy

        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        new_x = x + vx * dt
        new_y = y + vy * dt

        if new_y >= 0:
            best_x = new_x
        else:
            break

        vx, vy, x, y = new_vx, new_vy, new_x, new_y

    return best_x

ANS1 = trunc_5sf(calc_range(0.0))  # סעיף 1: בלי גרר kv^2
ANS2 = trunc_5sf(calc_range(c))    # סעיף 2: עם c מהקלט


#ouput
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')
