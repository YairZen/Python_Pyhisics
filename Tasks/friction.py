
import numpy as np

#input
F=list(map(float,input().split()))
a=list(map(float,input().split()))
print()

# consts
g=9.8

# your code

F_arr = np.array(F, dtype=float)
a_arr = np.array(a, dtype=float)

# linear fit: a = (1/m)*F - μg
p, pcov = np.polyfit(F_arr, a_arr, 1, cov=True)
slope, intercept = p
sigma_intercept = np.sqrt(pcov[1, 1])

# friction coefficient and its raw uncertainty
mu_raw = -intercept / g
DELTA_mu_raw = sigma_intercept / g

# round uncertainty to 1 significant digit,
# and μ to the same decimal place
if DELTA_mu_raw == 0:
    mu = mu_raw
    DELTA_mu = DELTA_mu_raw
else:
    power = int(np.floor(np.log10(abs(DELTA_mu_raw))))
    decimals = -power
    DELTA_mu = round(DELTA_mu_raw, decimals)
    mu = round(mu_raw, decimals)


## output
print(f'{mu}\n{DELTA_mu}')
