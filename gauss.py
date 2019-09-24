# %%
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

vec_x = []
vec_y = []
vec_z = []

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        # print(str(i).zfill(3))
        # print(x)
        vec_x.append(x[0])
        vec_y.append(x[1])
        vec_z.append(x[2])
    return x


A = np.array([[4.0, -2.0, 1.0],
              [1.0, -3.0, 2.0],
              [-1.0, 2.0, 6.0]])

b = [1.0, 2.0, 3.0]
x = [1, 1, 1]

n = 10

gauss(A, b, x, n)
print('Solution: ', solve(A, b))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(n - 1):
    ax.plot([vec_x[i], vec_x[i + 1]],
            [vec_y[i], vec_y[i + 1]],
            zs=[vec_z[i], vec_z[i + 1]])

fig.savefig('plot.svg')