import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def find_orthogonal_vector(A):
    min_index = np.argmin(np.abs(A))
    B = np.zeros_like(A)
    other_indices = [i for i in range(len(A)) if i != min_index]
    B[other_indices[0]], B[other_indices[1]] = -A[other_indices[1]], A[other_indices[0]]
    return B

A = np.array([1, 2, 3])
B = find_orthogonal_vector(A)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ベクトルAの描画
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='black')

# ベクトルBの描画
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='r')

ax.set_xlim([min(0, B[0], A[0]), max(0, B[0], A[0])])
ax.set_ylim([min(0, B[1], A[1]), max(0, B[1], A[1])])
ax.set_zlim([min(0, B[2], A[2]), max(0, B[2], A[2])])

plt.show()
