import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import time
import numpy as np


from src.Quaternions import *

x1 = Quaternion(0, -1, -1, -1)
x2 = Quaternion(0, 1, -1, -1)
x3 = Quaternion(0, 1, 1, -1)
x4 = Quaternion(0, -1, 1, -1)
x5 = Quaternion(0, 0, 0, 1)

r = rotation(0.05, 0, 0, 1)

c = 0
while c < 5000:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    v = np.array([[x1.i, x1.j, x1.k], [x2.i, x2.j, x2.k], [x3.i, x3.j, x3.k], [x4.i, x4.j, x4.k], [x5.i, x5.j, x5.k]])
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-2.5, 2.5)
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
    verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
             [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]
    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    x1 = x1.rotate(r)
    x2 = x2.rotate(r)
    x3 = x3.rotate(r)
    x4 = x4.rotate(r)
    x5 = x5.rotate(r)
    plt.show()
    time.sleep(1/30)
    c = c + 1
