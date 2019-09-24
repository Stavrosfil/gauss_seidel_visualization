# %%
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt


def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(str(i).zfill(3))
        print(x)
    return x


A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]

n = 5

print(gauss(A, b, x, n))
print(solve(A, b))

# %%
VecStart_x = [0, 1, 3, 5]
VecStart_y = [2, 2, 5, 5]
VecStart_z = [0, 1, 1, 5]
VecEnd_x = [1, 2, -1, 6]
VecEnd_y = [3, 1, -2, 7]
VecEnd_z = [1, 0, 4, 9]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(4):
    ax.plot([VecStart_x[i], VecEnd_x[i]],
            [VecStart_y[i], VecEnd_y[i]],
            zs=[VecStart_z[i], VecEnd_z[i]])


# %%
