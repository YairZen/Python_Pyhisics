import numpy as np
#import matplotlib.pyplot as plt


m1=float(input())
m2=float(input())
F0=float(input())
v0=float(input())

qn=int(input())

### your code

# ציר הזמן
dt = 0.01
t = np.arange(0.0, 10.0, dt)

# כוח האינטראקציה המוגדר: F(t)=F0*sin(2t)
F = F0*np.sin(2*t)

# תנאי התחלה
p10 = m1*v0
p20 = 0.0

# אינטגרציה בסכום שמאלי: dp/dt = F  (מוסיפים אפס בתחילה)
imp = dt*np.cumsum(np.r_[0.0, F[:-1]])

# על גוף 1 פועל -F, ועל גוף 2 +F
p1 = p10 - imp
p2 = p20 + imp
P  = p1 + p2

ANS4 = 'no'   # אין שימור אנרגיה קינטית כללית באינטראקציה כללית
ANS5 = 'yes'  # dP/dt = סכום הכוחות החיצוניים (כאן אפס) — נשמר
ANS6 = 'yes'  # שימור התנע הכולל מתקיים


## output
if qn==1: print(p1[:10])
if qn==2: print(p2[:10])
if qn==3: print(P[:10])
if qn==4: print(ANS4)
if qn==5: print(ANS5)
if qn==6: print(ANS6)