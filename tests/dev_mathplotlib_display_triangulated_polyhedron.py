from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np

from CGAL import CGAL_Convex_hull_3
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from CGAL.CGAL_Triangulation_3 import Delaunay_triangulation_3


def insert_polyhedron(dt, polyhedron):
    """
    Updates a triangulation objects with a set of polyhedron points
    
    Inputs:
        dt          Delaunay triangulation object
        polyhedron  Polyhedron_3
    Outputs:
        none (update dt object)
    """
    if not polyhedron:
        return
    for polypt in polyhedron.points():
        dt.insert(polypt)

def plot_triangulated_polyhedron(ax, dt):
    """
    Plots a polyhedron based on triangle facet data using mathplotlib/mplot3d
    Also updates figure axes range for the polyhedron to display
    
    Inputs:
        ax      graphics current axis (fig.gca), has to support 3d projection
        dt      Delaunay triangulation of the considered polyhedron
    Outputs:
        none (updated figure)
    """
    def plot_facet(ax, facet, *args):
        facet_tri = dt.triangle(facet)
        xs = np.zeros(3)
        ys = np.zeros(3)
        zs = np.zeros(3)
        for ind_point in range(0,3):
            p = facet_tri.vertex(ind_point)
            xs[ind_point] = p.x()
            ys[ind_point] = p.y()
            zs[ind_point] = p.z()
        verts = [zip(xs,ys,zs)]
        ax.add_collection3d(Poly3DCollection(verts,facecolors='grey',edgecolors='k'))
        
        # update axis limits for the points to appear
        ax_xlim = ax.get_xlim()
        ax_ylim = ax.get_ylim()
        ax_zlim = ax.get_zlim()
        
        ax_xmin= min(min(xs),ax_xlim[0])
        ax_ymin= min(min(ys),ax_ylim[0])
        ax_zmin= min(min(zs),ax_zlim[0])
        ax_xmax= max(max(xs),ax_xlim[1])
        ax_ymax= max(max(ys),ax_ylim[1])
        ax_zmax= max(max(zs),ax_zlim[1])
        
        ax.set_xlim(ax_xmin,ax_xmax)
        ax.set_ylim(ax_ymin,ax_ymax)
        ax.set_zlim(ax_zmin,ax_zmax)
        
    for facet in dt.finite_facets():        
        # plot facet
        plot_facet(ax, facet)
    
    plt.show()

# main
import os
datadir = os.environ.get('DATADIR', './')
datafile = datadir+'sphere.off' #'cube.off'

# load input polyhedron
my_poly = Polyhedron_3(datafile)

# form convex hull
# can only properly plot convex hull ?
# subtract to original polyhedron ?
res = Polyhedron_3()
CGAL_Convex_hull_3.convex_hull_3(my_poly.points(), res)

# insert polyhedron points in triangulation
#hdl_del_tri = Delaunay_triangulation_3()
#insert_polyhedron(hdl_del_tri,my_poly)
hdl_del_tri = Delaunay_triangulation_3(res.points())
#hdl_del_tri = Delaunay_triangulation_3(my_poly.points())

# plot triangulated polyhedron
fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
plot_triangulated_polyhedron(ax,hdl_del_tri)
    