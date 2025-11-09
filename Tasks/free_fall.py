import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]
#inputs
V0x=float(input('enter V_ox: '))
V0y=float(input('enter V_oy: '))
qn=int(input('enter qn: '))
print()

#your code


# קבועים ורשת זמן (3000 נק׳ ללא נקודת קצה)
g = 9.8
t = np.linspace(0.0, 2.5*V0y/g, 3000, endpoint=False)
dt = t[1] - t[0]

# מיקום אנליטי לאורך הזמן
y = V0y*t - 0.5*g*t**2

# חציית הקרקע: סוף הצעד שבו y מחליף סימן
k = zero_cross(y)[-1]
t_end = (k + 1) * dt

# תשובות
Ans1 = t_end                 # זמן מעוף נומרי (בדגימה סופית)
Ans2 = V0x * t_end           # טווח נומרי (בדגימה סופית)
Ans3 = 2*V0y/g               # זמן מעוף אנליטי
Ans4 = V0x * Ans3            # טווח אנליטי


Answers=[0,Ans1,Ans2,Ans3,Ans4]
#output
print(f'{Answers[qn]:.5g}')