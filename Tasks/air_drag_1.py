#imports and def
import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    sign_ar=np.sign(ar)
    sign_change_ar=np.abs(sign_ar[:-1]-sign_ar[1:])
    return np.nonzero(sign_change_ar)[0]

#input
sn=int(input())
v0=float(input())
m=float(input())
b=float(input())

#your code
#your code
dt = 1e-3
g = 9.8
Tmax = 3.0

N = int(Tmax/dt) + 1

v = np.zeros(N)
y = np.zeros(N)
t = np.zeros(N)

v[0] = v0
y[0] = 0.0
t[0] = 0.0

for i in range(N-1):
    a = -g - (b/m)*v[i]
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i]*dt
    t[i+1] = t[i] + dt

# זמן לשיא גובה (מתי מהירות משנה סימן)
idx_v0 = zero_cross(v)[0]
t1 = t[idx_v0]

# זמן חזרה לקרקע (גובה 0) אחרי השיא → רק החציות לאחר idx_v0
idx_y_all = zero_cross(y)
idx_y0 = [k for k in idx_y_all if k > idx_v0][0]
t2 = t[idx_y0] - t[idx_v0]

#output
if sn==1:
    print(t1)
if sn==2:
    print(t2)