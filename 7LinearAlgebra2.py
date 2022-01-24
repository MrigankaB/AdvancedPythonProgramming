#LAB 1/12/2021

# inner Product
# Norm
# Angle between two vectors

import numpy as np
import numpy.linalg as la
import pandas as pd

"""
a= np.array([2,7])
b= np.array([5,2])

at= a.transpose()

print(np.dot(at,b))
"""

a= np.array([2,7])
b= np.array([5,2])

theta = 52.25
rad= np.radians(theta)    # converting to radians
print(rad)

#print(la.norm(a))         # norm of a vector
#print(la.norm(b))
#print(np.cos(rad))

# Dot product of two vectors
inner= np.round(la.norm(a)*la.norm(b)*np.cos(rad),2)
print(inner)




# Angle between a and b

a= np.array([[-2],[1]])
b= np.array([[-3],[1]])

ab=np.dot(a.T,b)

cos= ab/(la.norm(a)*la.norm(b))
print(cos)

rad=np.arccos(cos)
print(rad)

deg= np.rad2deg(rad)
print(deg)