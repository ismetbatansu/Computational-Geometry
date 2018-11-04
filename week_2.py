
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1 = np.array([0,0,0]) #originden geçen x=1 y=-2 z=1 olan bir normal var, meshgrid yapısı oluşturucaz.
normal1 = np.array([1,-2,1])

point2 = np.array([0,-4,0])
normal2 = np.array([1,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])

d1 = -np.sum(point1*normal1)
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3)

xx, yy = np.meshgrid(range(5), range(5)) #5,5 büyüklüğünde bir meshgrid oluştur.

z1 = (-normal1[0]*xx - normal1[1]*yy -d1)*1./normal1[2]
get_ipython().run_line_magic('matplotlib', 'inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')