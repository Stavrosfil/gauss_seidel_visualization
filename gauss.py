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
x = [10, 10, 10]

n = 5

gauss(A, b, x, n)
solution = solve(A, b)
print('Solution: ', solution)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([x[0], vec_x[0]],
        [x[1], vec_y[0]],
        zs=[x[2], vec_z[0]],
        linewidth = 1.5)

for i in range(n - 1):
    ax.plot([vec_x[i], vec_x[i + 1]],
            [vec_y[i], vec_y[i + 1]],
            zs=[vec_z[i], vec_z[i + 1]],
            linewidth = 1 / (i + 1))

ax.scatter(x[0], x[1], x[2], c='r', marker='o')
ax.scatter(solution[0], solution[1], solution[2], c='g', marker='o')

fig.savefig('plot.svg')
