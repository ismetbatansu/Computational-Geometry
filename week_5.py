from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# In[95]:


def draw_my_line(normal_vector, point_on_line): # other_point adim 2 de eklendi
    a = normal_vector[0]
    b = normal_vector[1]
    c = normal_vector[2]
    
    x_0 = point_on_line[0]
    y_0 = point_on_line[1]
    z_0 = point_on_line[2]
    
    x = []
    y = []
    z = []
    
   
    
    for t in range(-1,10):
        x.append(x_0+t*a)
        y.append(y_0+t*b) 
        z.append(z_0+t*c) 
    return x,y,z
    
    


# In[96]:


def my_scalar_product(a, b ):
    #a = [-1,-2,4]
    #b = [-2,-5,2]
    #a transpoz b 
    a_t_b= a[0]*b[0]+a[1]*b[1]+ a[2]*b[2]
    return a_t_b


# In[97]:


def point_on_line(normal_vector,point_on_line,other_point): #adim 3
    
    a_x = other_point[0] - point_on_line[0]   #otherpoint pointonline ikilisi
    a_y = other_point[1] - point_on_line[1] 
    a_z = other_point[2] - point_on_line[2] 
    
    b = [a_x,a_y,a_z]
    a = normal_vector
    
    c = my_scalar_product(a,b) / my_scalar_product(a,a)
    
    b_x = c*a[0]
    b_y = c*a[1]
    b_z = c*a[2]
    
    nearest_point_on_line = [b_x,b_y,b_z]
    
    return nearest_point_on_line


# In[98]:


# adım 1 : line çizdiriyoruz
#p = (1,2,3)
#n = (4,5,6)
#points = draw_my_line(n,p) adim 1 de kullanılıyor
#%matplotlib notebook
#fig = plt.figure()
####ax = fig.add_subplot(111,projection='3d')
#ax = plt.axes(projection='3d')
#ax.plot3D(points[0],points[1],points[2],'red')
###plt.plot(points[0],points[1],points[2])
#plt.show

#########################
# adım 2 : bir nokta ile line arasındaki en kısa mesafeye denk gelen line üstündeki nokta

#draw_my_line fonksiyonuna other_point parametresi eklendi !

p = (0,0,0)  #hattı tanımlayan iki pakametre
n = (1,1,1)
other_point = (1,2,7)   #bekleme kontrası
points = draw_my_line(n,p)
n_p = point_on_line(n,p,other_point)  #hat üzerindeki bize en yaıkın nokta

get_ipython().run_line_magic('matplotlib', 'notebook')
ax = plt.axes(projection='3d')
ax.plot3D(points[0],points[1],points[2],'red')
ax.scatter(n_p[0],n_p[1],n_p[2],'*')
ax.scatter(other_point[0],other_point[0],other_point[0],'*')
plt.show