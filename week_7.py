
#define a vectorel function
#define its derivate
#comment them
#draw the derivate for a point in thar curve
#sint, cost
#t=10


# In[9]:

theta_current = 4 * np.pi
x_1=math.cos(theta_current)
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current)
y_2=math.cos(theta_current)
z_2=theta_current

x_s=[x_1,x_2]
y_s=[y_1,y_2]
z_s=[z_1,z_2]
ax.plot(x_s,y_s,z_s)
plt.show()


# In[1]:

get_ipython().magic('matplotlib notebook')
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x =  np.sin(theta)
y =  np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)


theta_current = 3 * np.pi/2
x_1=math.cos(theta_current)
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current)
y_2=math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]
ax.plot(x_s,y_s,z_s)


plt.show()


# In[ ]:

# x=acost y=bsint z=t olarak tanımlanmış eğrinin, t=3pi/2 deki teğet doğrusunu çiziniz
# x=6t y=3t^2 z=t olan eğrinin t=10 daki teğetini çiziniz.


# In[5]:

get_ipython().magic('matplotlib notebook')
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
a=5
b=7
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x =  a*np.sin(theta)
y =  b*np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)


theta_current = 3 * np.pi/2
x_1=a*math.cos(theta_current)
y_1=b*math.sin(theta_current)
z_1=1

x_2=a*math.sin(theta_current)
y_2=b*math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]
ax.plot(x_s,y_s,z_s)


plt.show()


# In[8]:

get_ipython().magic('matplotlib notebook')
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# x=6t y=3t^2 z=t olan eğrinin t=10 daki teğetini çiziniz.

n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis

theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x =  6*theta
y =  3*(theta**2)
ax.plot(x, y, z, 'b', lw=2)


theta_current = 10
x_1=6
y_1=3*theta_current
z_1=1

x_2=0
y_2=6
z_2=0

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]
ax.plot(x_s,y_s,z_s)


plt.show()


# In[ ]:



