# 13/12/2021

import numpy as np
import numpy.linalg as la
import pandas as pd
from sympy import *

# 2 ways of viewing a matrix: 1. Collection of rows
                            # 2. collection of column

# hstack- matrix creation
a=np.array([[2],[1],[-1]])
b=np.array([[-3],[4],[-1]])
A= np.hstack((a,b))
print(A)

#Slicing
print(A[0,1])
print(A[1,:2])
print(A[:,1])

# Matrix Operation

# Addition
m1=np.array([[2,4],[1,9]])
m2=np.array([[6,8],[-1,0]])
m3=np.array([[2,4,3,1]])
M=[m1,m2,m3]   # List
for i,j in zip(M,range(len(M))):
    print(f"Shape of {'m'+str(j+1)}:{i.shape}") # we can make it simple by printing 3 times

print(m1+m2)

#Exception handling
try:
    m1+m3
except:
    print("Matrices must be of same dimension")


# (u.T).v = (v.T).u
u= np.array([-1,2,4]).reshape(3,1)
v= np.array([-2,0,5]).reshape(3,1)
pro1= np.dot(u.T,v)
pro2= np.dot(v.T,u)
print(np.equal(pro1,pro2))

# (A.u).v = u.T((A.T).v)
A= np.array([-1,2,4,2,6,2,6,1,7]).reshape(3,3)
A1= np.dot(np.dot(A,u).T,v)
print(A1)
A2= np.dot(u.T, np.dot(A.T,v))
print(A2)

# (A.B).T= (B.T).(A.T)
B = np.random.randint(-10,10,(3,3))
print(B)
AB=np.dot(A,B)
BtAt=np.dot(B.T,A.T)
print(np.equal(AB.T, BtAt))


# identity matrix
print(np.eye(3,k=1))


# Trace - Sum of diagonal elements
m= np.random.randint(1,10,(3,3))
np.trace(m)

# Diagonal Matrix
print(np.diag([1,4,7]))

# Triangular Matrix
m= np.random.randint(1,10,9).reshape(3,3)
print("m:",m)
print(np.triu(m))
x= np.triu(m,k=1) # diagonal shift upward
print(la.det(x))
print(np.tril(m))

#In Triangular matrix, if diagonal elements are 0, it is irreversible, det=0

#Inverse of a matrix

m_inv= np.around(la.inv(m),2)
print(m_inv)

# inverse of upper and lower triangular matrix
# will be upper and lower triangular matrix respectively


# Symmetric matrix
c= np.random.randint(-10,10,(3,3))
d= np.random.randint(-10,10,(3,3))

C= np.triu(c)+ np.triu(c).T
print(C)

D= np.tril(d)+ np.tril(d).T
print(D)

print(np.equal(C.T,C))
print()
print(np.equal(D.T,D))
print()
E=np.add(C,D)     # +/- of symmetric matrices is symmetric matrix
print(np.equal(E.T,E))
print()
#Scalar product of SM is a SM
F=3*E
print(np.equal(F.T,F))


#product of SM is not SM but holds for following case
# A.B = B.A
# (A.B).T= (B.T).(A.T)= BA = AB
G=np.array([[1,2],[2,3]])
H=np.array([[-4,3],[3,-1]])
GH= np.dot(G,H)
HG= np.dot(H,G)
print(GH==HG)
print()
GHt= (np.dot(G,H)).T
HtGt= np.dot(G.T,H.T)
print(GHt==HtGt)
print()
print(GHt==GH)

#If A is reversible SM then A_inverse is also a SM
J = np.array(([-10,-1,3,-1,6,1,3,1,-6])).reshape(3,3)
print(np.around(la.det(J),2))

J_inv= np.around(la.inv(J),2)
print(J_inv)





#INVERSE MATRIX     [ np.linalg.inv() ]

# A.A^-1 = I
x= np.array([1,3,5,2,7,8,4,0,6]).reshape(3,3)
x_inv= np.around(la.inv(x),2)
r1= np.dot(x,x_inv)
print(r1)
# Substitute 1e-10 with 0
np.place(r1,r1<1e-10,0)
print(r1)



# A.b=c
# A^-1.A.b= A^-1.c
# b= A^-1.c

A= np.array([1,1,2,2,4,-3,3,6,-5]).reshape(3,3)
c= np.array([9,1,0]).reshape(3,1)
A_inv=la.inv(A)
re= np.around(np.dot(A_inv,c),2)
print(re)
#or
print(la.solve(A,c))
print()


#Gaussian Jordon elimination method (Reduced row echelon form)

#Example1:
# x + y = 2
# 2x + 4y = -3
# 3x + 6y = 5

a= np.array([[1,1,2],
             [2,4,-3],
             [3,6,5]])
a[1,:]=a[1,:]-2*a[0,:]
a[2,:]=a[2,:]-3*a[0,:]
a[1,:]=a[1,:]/2
a[0,:]=a[0,:]-a[1,:]
a[2,:]=a[2,:]-3*a[1,:]
a[2,:]=a[2,:]/8
a[0,:]=a[0,:]-5*a[2,:]
a[1,:]=a[1,:]+3*a[2,:]
print(a)

#using sympy
a1=Matrix(a)
print(a1)
print(a1.rref())    # returns rref form and number of columns wiith diagonal element 1


#Example 2:

# a+b-c+3d==0
# 3a+b-c-d=0
# 2a-b-2c+d=0

a= np.array([[1,1,-1,3,0],
             [3,1,-1,-1,0],
             [2,-1,-2,1,0]])
a1= Matrix(a)
print(a1.rref())

# Determinant     [ np.linalg.det(a) ]

# Determinant of square matrix A and its transpose matrix is same
a=np.array([1,4,2,5,2,4,6,8,2]).reshape(3,3)
re=np.around([la.det(a), la.det(a.T)],2)
print(re)

# if all the elements in 1 row or column is 0, det= 0
b= np.array([3,1,3,1,4,6,0,0,0]).reshape(3,3)
print(la.det(b))












