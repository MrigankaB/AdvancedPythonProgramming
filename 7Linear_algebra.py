#LAB 29/11/2021

# Calculating Scalar and Vector Distance
# Unit Vector
# Vector Properties

import numpy as np
import pandas as pd

"""
#Scalar Distance
ab=(5**2+3**2)**0.5
print(round(ab,3))




#Vector Distance
point= np.array([[5,3],[3,-4],[-2,-4],[-3,5]])
print(point)

d=[(point[I,0]**2+point[I,1]**2)**0.5 for I in range(4)]
re= np.c_[point,d]
re1=pd.DataFrame(re)
re1.coloums=['x','y','distance']
re1.index=['b','g','r','k']
print(re1)




#Dimension and Axis
arr=np.array([[5,3,-2,-3],[3,-4,-4,5]])
print(arr)
print(arr.reshape(-1,2))

"""



"""
#norms and Unit vectors

#Unit vector- size or norm is 1

import numpy.linalg as la

la.norm([[5,0],[3,0]])


a= np.array([[2],[7]])
a_norm=la.norm(a)
a_unit=a/a_norm
print(a_unit)

print(la.norm(a_unit))
"""





# Vector Properties
a= np.array([10,15])
b= np.array([8,2])
c= np.array([1,2,3])


"""
#addition
l1= print(a+b)
l2= print(b+a)
if l1 == l2:
    print("a+b = b+a is true")
else:
    print("a+b = b+a is false")
"""


"""
n1=a+b
x=n1+c
l1= print(x)

n2=b+c
y= a+n2
l2= print(y)
if l1 == l2:
    print("(a+b)+c = a+(b+c) is true")
else:
    print("(a+b)+c = a+(b+c) is false")

"""


"""
l1= print(c+0)
if c.all(l1):
    print("c+0 = c is true")
else:
    print("c+0 = c is false")
    
"""


"""
l1= print(1*c)
if c.all(l1):
    print("1.c= c is true")
else:
    print("1.c= c is false")
    
"""

"""
c=5
n1=b+c
l1= print(a*n1)
n2=a*b
n3=a*c
l2= print(n2+n3)
if l1 == l2:
    print("a*(b+c) = a*b+a*c is true")
else:
    print("a*(b+c) = a*b+a*c is false")

"""


"""
a =[[1,0,1],[0,1,0],[1,0,1]]
choices=[-10,10]
print(np.choose(a,choices))
"""





"""
if C.tolist()==I and D.tolist()==I:
    print("")
else:
    print("")    
// if np.equal(A,B)
"""


