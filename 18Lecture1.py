
#Lecture Class (12/1/2021)

import numpy as np

a= np.array([0,1]).reshape((2,1,1))
c1=np.array([1,2,3]).reshape((1,3,1))
c2= np.array([-1,-2,-3,-4,-5]).reshape((1,1,5))
print(a)
print("Shape of a: ",a.shape)
print()
print(c1)
print("Shape of c1: ",c1.shape)
print()
print(c2)
print("Shape of c2: ",c2.shape)
print()
print(np.choose(a,(c1,c2)))
print("Shape of resultant array: ", np.choose(a,(c1,c2)).shape)