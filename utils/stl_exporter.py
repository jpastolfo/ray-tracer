import numpy as np
import matplotlib.pyplot as plt

from stl import mesh
from entities.beam import Ray



def create(ray:Ray,n_vertices:int=3,radius:float=1):
    
    print(ray.path)
    print(ray.path.x)
    print(ray.path.y)

    angle = 2*np.pi/n_vertices

    vertices_x = []
    vertices_y = []
    vertices_z = []
    vertices = []
    for i in range(len(ray.path.x)):

        ray_x = ray.path.x[i]
        ray_y = ray.path.y[i]
        dir_x = ray.path.dir_x[i]
        dir_y = ray.path.dir_y[i]

        for j in range(n_vertices):
            
            x = ray_x - dir_y * (radius*np.cos(j*angle))
            y = ray_y + dir_x * (radius*np.cos(j*angle))

            print("3D Vertice:", [x,y,radius*np.sin(j*angle)])
            vertices_x.append(x)
            vertices_y.append(y)
            vertices_z.append(radius*np.sin(j*angle))
            vertices.append([x,y,radius*np.sin(j*angle)])


    faces = []
    for i in range(int((len(vertices))/n_vertices)-1):
        for j in range(n_vertices-1):
            faces.append([i*n_vertices+j,
                          i*n_vertices+n_vertices+j,
                          i*n_vertices+n_vertices+j+1])
            faces.append([i*n_vertices+j,
                          i*n_vertices+j+1,
                          i*n_vertices+n_vertices+j+1])
        faces.append([(i+1)*n_vertices-1,
                      (i+2)*n_vertices-1,
                      (i+1)*n_vertices])
        faces.append([(i+1)*n_vertices-1,
                      i*n_vertices,
                      (i+1)*n_vertices])

    #print(faces)

    faces = np.array(faces)
    vertices = np.array(vertices)
    
    path = mesh.Mesh(np.zeros(faces.shape[0],dtype=mesh.Mesh.dtype))
    for i,f in enumerate(faces):
        #print(f"f={f}")
        for j in range(3):
            #print(path.vectors[i][j])
            #print(vertices[f[j],:])
            path.vectors[i][j] = vertices[f[j],:]

    path.save("path.stl")



    from matplotlib import pyplot
    from mpl_toolkits import mplot3d

    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    # Render the cube
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(path.vectors))

    # Auto scale to the mesh size
    scale = path.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()
