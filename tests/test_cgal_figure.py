from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np

from CGAL.CGAL_Polyhedron_3 import Polyhedron_3, Polyhedron_3_Vertex_iterator
#from CGAL.CGAL_Polyhedron_3 import 
#from CGAL.CGAL_Mesh_3 import Polyhedral_mesh_domain_3
#from CGAL.CGAL_Triangulation_3 import Triangulation_3

# file path
import os
datadir = os.environ.get('DATADIR', './')
datafile = datadir+'triangle.off'

# load input polyhedron
p = Polyhedron_3(datafile)

v = Polyhedron_3_Vertex_iterator();

x = np.zeros(p.size_of_vertices())
y = np.zeros(p.size_of_vertices())
z = np.zeros(p.size_of_vertices())
counter = 0
for v in p.vertices():
    x[counter] = v.point().x()
    y[counter] = v.point().y()
    z[counter] = v.point().z()
    counter += 1

# Plots
#fig = plt.figure(figsize=(10,20))
#ax = fig.add_subplot(211, projection='3d')
#ax.scatter(x, y, z, color='b')
#ax = fig.add_subplot(212, projection='3d')
#ax.plot_trisurf(x, y, z, color='b') # triangulation/normals problem !!
#plt.show()

outer_cst = 0.01
min_coord = min(min(x),min(y),min(z))-outer_cst
max_coord = max(max(x),max(y),max(z))+outer_cst

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
ax.axis("equal")
ax.set_xlim3d(min_coord, max_coord)
ax.set_ylim3d(min_coord, max_coord)
ax.set_zlim3d(min_coord, max_coord)
verts = [zip(x,y,z)]
ax.add_collection3d(Poly3DCollection(verts,facecolors='r'))
plt.show()

#t = Triangulation_3()
# create domain
#domain = Polyhedral_mesh_domain_3(polyhedron)