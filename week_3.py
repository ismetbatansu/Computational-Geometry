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
    
    for t in range(-1,10):
        x.append(x_0+t*a)
        y.append(y_0+t*b)
        z.append(z_0+t*c)
    return (x,y,z)

def my_scalar_product(a,b): #transpoze
    return (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])

def point_on_line(normal_vector,point_on_line,other_point):
    a_x= other_point[0]-point_on_line[0] #otherPoint pointOn-line
    a_y= other_point[1]-point_on_line[1]
    a_z= other_point[2]-point_on_line[2]
    
    a=[a_x,a_y,a_z]
    b=normal_vector
    
    c=my_scalar_product(a,b)
    
    b_x=c*b[0]
    b_y=c*b[1]
    b_z=c*b[2]
    
    nearest_point_on_line=(b_x,b_y,b_z)
    
    return nearest_point_on_line

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook 

p=(1,2,3) #hattı tanımlayan 2 parametre
n=(4,5,6)  
other_point=[1,2,5] #bekleme noktası
n_p=point_on_line(n,p,other_point) #hat üzerindeki en yakın nokta
points=draw_my_line(n,p)


ax=plt.axes(projection='3d')
ax.plot3D(points[0],points[1],points[2],'red')
ax.scatter(other_point[0],other_point[1],other_point[2],'*')
ax.scatter(n_p[0],n_p[1],n_p[2],'*')
plt.show()