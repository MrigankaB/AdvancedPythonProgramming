#6-12-2021


# angle betwee vector a and b

import numpy as np
import numpy.linalg as la
import pandas as pd

"""
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
a=np.array([2,7])
b=np.array([[5],[2]])
x=np.dot(a,b)
print(x)        # array --> [24]

anorm= la.norm(a)
bnorm= la.norm(b)
print(anorm)
print(bnorm)

inner= np.round(la.norm(a)*la.norm(b)*np.cos(rad),0)
print(inner)       # Scalar value -->  24

cos=x/(anorm*bnorm)
print(cos)

rad= np.arccos(cos)
print(rad)

deg= np.rad2deg(rad)
print(deg)

"""


a=np.array([-2,1])
b=np.array([[-3],[1]])
x= np.dot(a,b)
print(x)

anorm= la.norm(a)
bnorm= la.norm(b)
print(anorm)
print(bnorm)

cos=x/(anorm*bnorm)
print(cos)

rad= np.arccos(cos)
print(rad)

inner= np.round(la.norm(a)*la.norm(b)*np.cos(rad),0)
print(inner)

deg= np.rad2deg(rad)
print(deg)
