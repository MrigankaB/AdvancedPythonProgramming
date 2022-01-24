# 15/12/2021(wed)

#Practice

import numpy as np
import numpy.linalg as la

"""
x= np.array([[1,2,3],[1,1,2],[1,3,1]])
y= np.array([[1,2,2],[3,1,1],[1,1,1]])

# dot product
xy= np.dot(x.T,y)
print(xy)

# Attributes
print("dimension ", xy.ndim)
print("Shape ", xy.shape)
print("Size ", xy.size)
print("itemsize ", xy.itemsize)
print("dtype ", xy.dtype)



# Calculating the inverse of the matrix
invx= la.inv(x)
print("Inverse of x is :")
print(invx)


#creating zero matrix
a=np.zeros((4,5))
print(a)


#crreating one matrix
b=np.ones((4,5))
print(b)


c= np.arange(6,dtype="float")
print(c)
d= np.reshape(c,(3,2))
print(d)


e= np.linspace(1,9,9)   #endpoint="False/True"
print(e)
f= np.resize(e,(4,3))
print(f)



#Row matrix & Coloumn matrix
g=np.arange(3)
h=np.arange(4)[:,np.newaxis]
print(g)
print(h)


identity= np.eye(3,4,1)
print(identity)
identity1= np.eye(3,3)
j= np.fill_diagonal(identity1,4)
print(j)


k= np.full((2,2),4)
print(k)


#Choose
a=np.array( [[2,0,1],[2,1,2]])
print(np.choose(a,[-1,0,1]))

"""

""" 
u= np.array([[0],[2]])
v= np.array([[2],[0]])
inner= np.dot(u.T,v)
print(inner)
#inner1= la.norm(u)*la.norm(v)*np.cos(rad,0)
if(inner == 0):
    print("u and v are orthogonal vectors")
else:
    print("u and v are not orthogonal")
"""

"""
#Angle between two vectors

a=np.array([1,2,1])
b=np.array([[1],[1],[1]])
x=np.dot(a,b)
print(x)

anorm= la.norm(a)
bnorm= la.norm(b)
print(anorm)
print(bnorm)

cos=x/(anorm*bnorm)
print(cos)

rad= np.arccos(cos)
print(rad)

deg= np.rad2deg(rad)
print(deg)

"""

"""
# Cauchy Schwarz inequality proof

u= np.array([[-1],[2]])
v= np.array([[4],[-2]])
inner=abs(np.dot(u.T,v))
print(inner)
normProd= round(la.norm(u)*la.norm(v),3)
print(normProd)

if( inner!= normProd):
    print("Cauchy Schwarz inequality proved")
else:
    print("Something went wrong")
"""

"""
# Triangular inequality proof

u= np.array([[-1],[2]])
v= np.array([[4],[-2]])

uv_norm1= la.norm(u+v)
print(uv_norm1)

uv_norm2= round(la.norm(u)+ la.norm(v), 3)
print(uv_norm2)

if( uv_norm1 != uv_norm2):
    print("triangular inequality proved")
else:
    print("Something went wrong")
"""

"""
#Projection

u= np.array([[1],[0]])
v= np.array([[2],[1]])
inner= np.dot(u.T,v)
unorm= (la.norm(u))**2
vproj= (inner*u)/unorm
print(vproj)

"""




