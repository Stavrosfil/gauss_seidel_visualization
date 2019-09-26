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
x = [0, 0, 0]

# Insert the guesses into the start of the anwers.
vec_x.insert(x[0], 0)
vec_y.insert(x[1], 0)
vec_z.insert(x[2], 0)

n = 4

gauss(A, b, x, n)
solution = solve(A, b)
print('Solution: ', solution)

# This is where the plotting magic happens.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X', fontsize='large', fontweight='bold', labelpad=12)
ax.set_ylabel('Y', fontsize='large', fontweight='bold', labelpad=12)
ax.set_zlabel('Z', fontsize='large', fontweight='bold', labelpad=12)

for i in range(n):

    # Take a step in the x axis
    ax.plot([vec_x[i], vec_x[i + 1]],
            [vec_y[i], vec_y[i]],
            zs=[vec_z[i], vec_z[i]],
            linewidth = 3 / (i + 1))

    # Take a step in the y axis
    ax.plot([vec_x[i + 1], vec_x[i + 1]],
            [vec_y[i], vec_y[i + 1]],
            zs=[vec_z[i], vec_z[i]],
            linewidth = 3 / (i + 1))

    # Take a step in the z axis
    ax.plot([vec_x[i + 1], vec_x[i + 1]],
            [vec_y[i + 1], vec_y[i + 1]],
            zs=[vec_z[i], vec_z[i + 1]],
            linewidth = 3 / (i + 1))

# Show a red circle for the first guess, and a green circle for the answer.
ax.scatter(x[0], x[1], x[2], c='red', marker='o')
ax.scatter(vec_x[-1], vec_y[-1], vec_z[-1], c='yellow', marker='o')
ax.scatter(solution[0], solution[1], solution[2], c='green', marker='o')

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal.
normal = A[0]
d = -1

# create x,y
plane_space_x = np.arange(min(vec_x) - 0.2, max(vec_x) + 0.2, .1)
plane_space_y = np.arange(min(vec_y) - 0.2, max(vec_y) + 0.2, .1)
xx, yy = np.meshgrid(plane_space_x, plane_space_y)

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

# plot the surface
ax.plot_surface(xx, yy, z, alpha=0.2, color='grey')

# rotate the axes and update
# for angle in range(0, 360):
#     ax.view_init(30, angle)
#     plt.draw()
#     plt.pause(.001)

plt.show()
fig.savefig('plot.svg')

#%%
