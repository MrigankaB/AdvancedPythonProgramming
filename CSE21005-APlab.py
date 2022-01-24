# 30/12/2021

import numpy as np
import numpy.linalg as la
import pandas as pd
from sympy import *

# Q1
x= np.array([[1],[2],[3]])
print("x=",x,"\n")

y= np.array([[-1],[-1],[0]])
print("y=",y,"\n")


# (1)Commutitive  x + Y = Y + X
a= np.add(x,y)
b= np.add(y,x)
print(np.equal(a,b))

# (2)Identity law   x + 0 = x
z= np.zeros(3)
a= np.add(x,z)
print(np.equal(a,x))
b= np.add(y,z)
print(np.equal(b,y))




# (ii) Distance between x and y

point= np.array([[1,-1],[2,-1],[3,0]])
print(point)

d=[(point[I,0]**2+point[I,1]**2)**0.5 for I in range(3)]
re= np.c_[point,d]
re1=pd.DataFrame(re)
re1.coloums=['x','y','distance']
re1.index=['b','g','r']
print(re1)

# (ii)Angle between x and y
r=np.dot(x.T,y)
xnorm= la.norm(x)
ynorm= la.norm(y)
cos=r/(xnorm*ynorm)
rad= np.arccos(cos)
deg= np.rad2deg(rad)
print("Angle between x and y: ",deg)



# (iii) Check whether x and y are orthogonal to each other
inner= np.dot(x.T,y)
print(inner)
if(inner == 0):
    print("x and y are orthogonal vectors")
else:
    print("x and y are not orthogonal")




# (iv) Triangular inequality proof
xy_norm1= la.norm(x+y)
print(xy_norm1)

xy_norm2= round(la.norm(x)+ la.norm(y), 3)
print(xy_norm2)

if( xy_norm1 != xy_norm2):
    print("triangular inequality proved")
else:
    print("Something went wrong")






# Q2.Gauss-Jordan elimination
A = np.array([[1,0,2,0],
              [1,1,0,0],
              [1,2,0,1],
              [1,1,1,1]])

I = np.eye(4)
A[1,:] = A[1,:] - A[0,:]
A[2,:] = A[2,:] - A[0,:]
A[3,:] = A[3,:] - A[0,:]
A[2,:] = A[2,:] - 2*A[1,:]
A[3,:] = A[3,:] - A[1,:]
A[0,:] = A[0,:] - A[2,:]
A[1,:] = A[1,:] + A[2,:]
A[2,:] = A[2,:] - A[3,:]
A[3,:] = A[3,:] - A[2,:]
A[0,:] = A[0,:] + A[3,:]
A[1,:] = A[1,:] - A[3,:]
print(A)
#Using above operations on I4
I[1,:] = I[1,:] - I[0,:]
I[2,:] = I[2,:] - I[0,:]
I[3,:] = I[3,:] - I[0,:]
I[2,:] = I[2,:] - 2*I[1,:]
I[3,:] = I[3,:] - I[1,:]
I[0,:] = I[0,:] - I[2,:]
I[1,:] = I[1,:] + I[2,:]
I[2,:] = I[2,:] - I[3,:]
I[3,:] = I[3,:] - I[2,:]
I[0,:] = I[0,:] + I[3,:]
I[1,:] = I[1,:] - I[3,:]
print(I)
#print(la.inv(A))     ??


#Using sympy
a = np.array([[1,0,2,0,1,0,0,0],
              [1,1,0,0,0,1,0,0],
              [1,2,0,1,0,0,1,0],
              [1,1,1,1,0,0,0,1]])
a1=Matrix(a)
print(a1)
print(a1.rref())
print()

#A_inv=la.inv(A)
#print(A_inv)

