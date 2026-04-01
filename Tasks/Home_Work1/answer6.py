import numpy as np

# parameters
V = 2
#V = 1
R = 1
omg = V/R
#omg = 2

dt = 1e-3
t = np.arange(0, 10, dt)

# contact equation: f(t) = Rcos(omg*t) + R = 0
f = R*np.cos(omg*t) + R

# numerical derivative of f
df = np.gradient(f)/dt

# solve f(t)=0 numerically by locating local minima of f
idx = []
for i in range(1, len(df)-1):
    if df[i-1] < 0 and df[i] > 0:   # minimum of f(t)
        idx.append(i)

# contact times
t_touch = t[idx]

print("Touch times (s):")
print(t_touch)
