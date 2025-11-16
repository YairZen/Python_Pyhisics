import numpy as np

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]


#input
V = float(input('enter V: '))
alp = float(input('enter alpha: '))
qn = int(input('enter question no.: '))
print()

# consts
rho = 1.3  # kg/m^3 (air density)
A = 18     # m^2 (wing area)

# your code

# angle from input (deg -> rad) for questions 1–2
alp_rad = alp * np.pi / 180.0
sin_a = np.sin(alp_rad)
cos_a = np.cos(alp_rad)

# 1. vertical force the air exerts on the plate
Fy = 2 * rho * A * V**2 * (sin_a**2 * cos_a)

# 2. horizontal force the air exerts on the plate
Fx = 2 * rho * A * V**2 * (sin_a**3)

# 3. angle where vertical force is 10 times the horizontal one
# tan(alpha) = 0.1 -> alpha ≈ 5.71°
alpha = 5.71 * np.pi / 180.0  # used only for printing in Q3

# for Q4 use the exact angle from Fy = 10 * Fx
alpha_rad = np.arctan(0.1)

# 4. speed so that vertical force balances weight of 1000 kg
m = 1000.0
g = 10.0
V4 = np.sqrt(m * g / (2 * rho * A * (np.sin(alpha_rad)**2 * np.cos(alpha_rad))))

Answers = [0, Fy, Fx, alpha * 180 / np.pi, V4]
print(f'{Answers[qn]:.5g}')
