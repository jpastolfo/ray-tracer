import numpy
import math

from stl import mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d


data = numpy.zeros(2,dtype=mesh.Mesh.dtype)


vertices = numpy.array([\
    [-1,1,0],
    [1,1,0],
    [1,-1,0],
    [-1,-1,0],
    [-1,1,1],
    [1,1,1],
    [1,-1,1],
    [-1,-1,1]])

faces = numpy.array([\
    [0,1,3],
    [1,3,2],
    [5,4,7],
    [5,6,7],
    [1,4,0],
    [1,5,4],
    [1,2,5],
    [2,5,6],
    [2,6,7],
    [2,7,3],
    [3,7,4],
    [3,4,0]])

cube = mesh.Mesh(numpy.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]


ray = mesh.Mesh(data.copy())
meshes = [cube]

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

for m in meshes:
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

scale = numpy.concatenate([m.points for m in meshes]).flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()