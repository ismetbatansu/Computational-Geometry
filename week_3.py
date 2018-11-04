
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def point_on_line(normal_vector,point_on_line,other_point):
    a_x= other_point[0]-point_on_line[0]
    a_y= other_point[1]-point_on_line[1]
    a_z= other_point[2]-point_on_line[2]
    
    b=[a_x,a_y,a_z]
    a=normal_vector
    
    c=transpose(a,b)/transpose(a,a)
    
    b_x=c*a[0]
    b_y=c*a[1]
    b_z=c*a[2]
    
    nearest_point_on_line=(b_x,b_y,b_z)
    
    return nearest_point_on_line

def draw_my_line(normal_vector,point_on_line):
    a=normal_vector[0]
    b=normal_vector[1]
    c=normal_vector[2]
    x_0=point_on_line[0]
    y_0=point_on_line[1]
    z_0=point_on_line[2]
    x=[]
    y=[]
    z=[]
    
    for t in range(-100,100):
        x.append(x_0+t*a)
        y.append(y_0+t*b)
        z.append(z_0+t*c)
    return (x,y,z)

def transpose(a,b):
    return (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    
p=(0,0,0) #hattı tanımla
n=(1,1,1)  
get_ipython().run_line_magic('matplotlib', 'notebook')
other_point=[1,1,100] #bekleme noktası
n_p=point_on_line(n,p,other_point) #hat üzerindeki en yakın nokta
points=draw_my_line(n,p)


get_ipython().run_line_magic('matplotlib', 'notebook')
fig = plt.figure()
ax=plt.axes(projection='3d')
ax.plot3D(points[0],points[1],points[2],'red')
ax.scatter(other_point[0],other_point[1],other_point[2],'*')
ax.scatter(n_p[0],n_p[1],n_p[2],'*')
plt.show()
