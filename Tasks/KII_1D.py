import numpy as np
from MyFunc import zero_cross


v0=float(input("vo: "))
gamma=float(input("gamma: "))
qn=int(input("q#:"))

t=np.arange(0,7, 0.01)
v=v0 * np.exp((-gamma)*t)*np.cos(10*gamma*t)
a=np.gradient(v, 0.01)   #dt = 0.01
x=np.cumsum(v)*0.01
t3rd_stop=t[zero_cross(v)[2]]

Answers=[0,t[:10],v[:10],a[:10],x[:10],t3rd_stop]
print(Answers[qn])
