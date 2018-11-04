import matplotlib.pyplot as plt

def draw_a_vector_from_origin(v):
    # from origin to v
    x=(0,v[0])
    y=(0,v[1])
    plt.plot(x,y)
    
def draw_a_vector(v,w):
    # from origin to v
    x=(v[0],w[0])
    y=(v[1],w[1])
    plt.plot(x,y)
    
def distance(v,w):
    return (((v[0]-w[0])**2)+((v[1]-w[1])**2))**.5
    
def scalar_product(a,b):
    return (a[0]*b[0]+a[1]*b[1])

def vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]

def vector_substract(v,w):
    return [v[0]-w[0],v[1]-w[1]]

def vector_multiply_scalar(c,v):
    return [v[0]*c,v[1]*c]

get_ipython().run_line_magic('matplotlib', 'inline')

a=[3,0]
b=[0,4]
#draw_a_vector_from_origin(x)
#draw_a_vector_from_origin(y)
draw_a_vector([5,5],[10,12])
draw_a_vector_from_origin([-7,5])
#vector_add(a,b)
#vector_substract(a,b)
#vector_multiply_scalar(3,a)
distance(a,b)