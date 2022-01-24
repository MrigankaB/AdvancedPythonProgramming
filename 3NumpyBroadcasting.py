import numpy as np
M=np.ones((2,3))
a=np.arange(3)

print(a)
print(M)
"""
M.shape=(2,3)
a.shape=(3,)
M.shape=(2,3)
a.shape=(1,3)
"""
print(M+a)

"""
Condition for broadcasting:

* Size of each dimension should be same
* Size of one dimension should be 1

Rules of Broadcasting :

Rule1:  If the two arrays differ in their number of dimensions, the shape of the one  with fewer dimensions is padded with ones on its leading (left) side.
Rule2: If the shape of the two arrays does not match in any dimension, the arry with shape equal to 1in that dimension is stretched to match other  shape 
Rule3: If in any dimension the sizes disagree and neither is equal to ,anerror is rated.

"""
#Otput of array contains heigher dimension