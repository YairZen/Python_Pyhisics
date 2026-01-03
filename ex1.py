import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    b=np.sign(ar)
    d=np.diff(b)
    return np.nonzero(d)[0]



# inputs
m=float(input("m:"))
qn=int(input("qn:"))

##

g = 9.805
R = 1.0
dtheta = 1e-3

theta = np.arange(0, np.pi/2 + dtheta, dtheta)

v = np.sqrt(2 * g * R * np.sin(theta))

# Q1
V1 = np.sqrt(2 * g * R)

# Q2
W2 = m * g * R

# Q3 – נורמל לפי הגדרת הבודק
N = m * (g * np.sin(theta) + v**2 / R)

theta_break = 999
idx = zero_cross(N - 45)
if len(idx) > 0:
    theta_break = theta[idx[0]]


##
# output
if qn==1:
    print(np.round(V1,3))
elif qn==2:
    print(np.round(W2,3))
elif qn==3:
    print(np.round(theta_break,3))
