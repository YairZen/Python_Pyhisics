import numpy as np
import matplotlib.pyplot as plt

# Given parameters
V = 2     #[m/s]
#V = 1
R = 1   #[m]
omg = V/R
#omg = 2

# Time settings
dt = 10**(-3)    #[sec]  10^(-3) sec time steps
t = np.arange(0, 10, dt)

# center
X = V*t
Y = 0

# point P from center
Xcp = R * np.sin(omg*t)
Ycp = R * np.cos(omg*t)

# general point P
Xp = X + Xcp
Yp = Y + Ycp

# Plot
plt.figure()
plt.plot(Xp, Yp)
#plt.axis("equal")
plt.xlabel("Xp")
plt.ylabel("Yp")
plt.title("Trajectory of point P (0 <= t < 10 s)")
plt.grid(True)
plt.show()
