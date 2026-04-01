import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# parameters
# -----------------------------
N = 2000
N2 = N // 2
v0 = 100.0
ITERS = 100
bins = 60
show_iters = [0, 1, 2, 3, 10, 20]

rng = np.random.default_rng()

# -----------------------------
# elastic collision, equal masses, rotation method
# alpha in radians (array of size N2)
# -----------------------------
def collide_equal_masses(v1x, v1y, v2x, v2y, alpha):
    ca = np.cos(alpha)
    sa = np.sin(alpha)

    # rotate to collision frame: v' = R^{-1} v
    v1xp = ca * v1x + sa * v1y
    v1yp = -sa * v1x + ca * v1y

    v2xp = ca * v2x + sa * v2y
    v2yp = -sa * v2x + ca * v2y

    # equal masses, elastic: exchange x' components, keep y'
    u1xp = v2xp
    u1yp = v1yp
    u2xp = v1xp
    u2yp = v2yp

    # rotate back: u = R u'
    u1x = ca * u1xp - sa * u1yp
    u1y = sa * u1xp + ca * u1yp
    u2x = ca * u2xp - sa * u2yp
    u2y = sa * u2xp + ca * u2yp

    return u1x, u1y, u2x, u2y

def plot_vx_hist(v1, v2, k):
    vx = np.concatenate([v1[:, 0], v2[:, 0]])
    plt.figure()
    plt.hist(vx, bins=bins)
    plt.title(f"vx histogram - iteration {k}")
    plt.xlabel("vx")
    plt.ylabel("count")
    plt.grid(True)
    plt.show()

# -----------------------------
# init velocities: two opposite groups in x
# -----------------------------
v1 = np.zeros((N2, 2), dtype=float)
v2 = np.zeros((N2, 2), dtype=float)
v1[:, 0] = +v0
v2[:, 0] = -v0

v1_init = v1.copy()
v2_init = v2.copy()

# histogram at iteration 0
if 0 in show_iters:
    plot_vx_hist(v1, v2, 0)

# store random angles
alphas = np.zeros((ITERS, N2), dtype=float)

# -----------------------------
# forward simulation
# -----------------------------
for k in range(1, ITERS + 1):
    alpha = rng.uniform(0.0, np.pi / 2.0, size=N2)
    alphas[k - 1, :] = alpha

    u1x, u1y, u2x, u2y = collide_equal_masses(
        v1[:, 0], v1[:, 1],
        v2[:, 0], v2[:, 1],
        alpha
    )
    v1[:, 0], v1[:, 1] = u1x, u1y
    v2[:, 0], v2[:, 1] = u2x, u2y

    # ensure different partner next iteration
    v2 = np.roll(v2, shift=1, axis=0)

    if k in show_iters:
        plot_vx_hist(v1, v2, k)

# -----------------------------
# time reversal
# -----------------------------
v1_rev = -v1.copy()
v2_rev = -v2.copy()

for k in range(ITERS - 1, -1, -1):
    # undo forward roll
    v2_rev = np.roll(v2_rev, shift=-1, axis=0)

    alpha = alphas[k, :]

    u1x, u1y, u2x, u2y = collide_equal_masses(
        v1_rev[:, 0], v1_rev[:, 1],
        v2_rev[:, 0], v2_rev[:, 1],
        alpha
    )
    v1_rev[:, 0], v1_rev[:, 1] = u1x, u1y
    v2_rev[:, 0], v2_rev[:, 1] = u2x, u2y

# errors vs initial
err1 = np.max(np.abs(v1_rev - v1_init))
err2 = np.max(np.abs(v2_rev - v2_init))
print(err1)
print(err2)
