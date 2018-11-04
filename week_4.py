# coding: utf-8

# In[13]:

point_test = np.array([1,-1,1])
normal_test = np.array([1,-2,1])
sum(point_test*normal_test)


# In[36]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[47]:

point1=np.array([0,0,0])
normal1=np.array([1,-2,1])

point2=np.array([0,-4,0])
normal2=np.array([0,2,-8])
point3=np.array([0,0,1])
normal3=np.array([-4,5,9])


# In[48]:

d1=-np.sum(point1*normal1) #
d2=-np.sum(point2*normal2) #
d3=-np.sum(point3*normal3) #
d1,d3,d2


# In[49]:

xx, yy = np.meshgrid(range(30),range(30))


# In[50]:

z1=(-normal1[0]*xx-normal1[1]*yy-d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d=plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color='yellow')


# In[55]:

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')

n=1000
theta_max = 8*np.pi
theta = np.linspace(0, theta_max, n)

x = np.sin(theta)
y = np.cos(theta)
z = theta

ax.plot(x,y,z, 'b', lw=2)


# In[ ]:
