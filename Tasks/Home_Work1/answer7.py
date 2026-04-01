import numpy as np
import matplotlib.pyplot as plt

# parameters
V = 2
R = 1
omg = V/R

# time
dt = 1e-3
t = np.arange(dt, 10 + dt, dt)

# position of point P
Xp = V*t + R*np.sin(omg*t)
Yp = R*np.cos(omg*t)

# numerical differentiation (velocity components)
V_Xp = np.gradient(Xp)/dt
V_Yp = np.gradient(Yp)/dt

# speed magnitude
Vp = (V_Xp**2 + V_Yp**2)**0.5

# plot |v(t)|
plt.plot(t, Vp)
plt.xlabel('t [s]')
plt.ylabel('|v| [m/s]')
plt.title('Speed magnitude of point P vs time')
plt.grid()
plt.show()
