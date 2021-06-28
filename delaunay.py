import numpy as np
from scipy.spatial import Delaunay


def delaunay(points):
    points = np.array(points)
    tri = Delaunay(points)

    return tri
