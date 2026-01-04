import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    b=np.sign(ar)
    d=np.diff(b)
    return np.nonzero(d)[0]

# inputs
m=float(input("m:"))
qn=int(input("qn:"))

# Constants
R = 1.0  # radius in meters
g = 9.8  # gravity in m/s²
dtheta = 1e-3  # angle increment in radians

# Create angle array from 0 to π/2
n_steps = int(np.pi/2 / dtheta) + 1
theta = np.linspace(0, np.pi/2, n_steps)
dtheta_actual = theta[1] - theta[0]

# Calculate work increments using right-Riemann (use ending angle of each interval)
dW_array = m * g * R * np.sin(theta[1:]) * dtheta_actual

# Cumulative work (kinetic energy) - prepend 0 for initial condition
K = np.zeros(len(theta))
K[1:] = np.cumsum(dW_array)

# Velocity from kinetic energy
v = np.sqrt(2 * K / m)

# Question 1: velocity at bottom
V1 = v[-1]

# Question 2: total work done by gravity (equals final kinetic energy)
W2 = K[-1]

# Question 3: angle where normal force exceeds 45 N
# Using the formula: N = 3mg cos(θ)
N = 3 * m * g * np.cos(theta)

# Find where N crosses 45 (going down from above)
# N starts at 3mg and decreases as theta increases
# We want to find where N drops below or equals 45
crosses_45 = N <= 45
if np.any(crosses_45):
    # Find first index where N <= 45
    theta_break = theta[np.where(crosses_45)[0][0]]
else:
    theta_break = 999

# output
if qn==1:
    print(np.round(V1,3))
elif qn==2:
    print(np.round(W2,3))
elif qn==3:
    print(np.round(theta_break,3))
