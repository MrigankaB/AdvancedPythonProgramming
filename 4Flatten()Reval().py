import numpy as np
# Flatten:
# Returns a copy of the array collapsed into 1 dimension
a=np.arange(10)
b= a.flatten(order="F")  # C(default)=row major, F=column major
                       # K= as in the menory
print(b)


#Ravel:
# Copy the element only if its needed, otherwise it only gives
# the view of the array

np.ravel(a,order="F")
a.ravel(order="F")  # done on ndarray

"""
Differences:

flatten(): gives copy of the array
           Since flatten is a method of ndarray object, we cannot write it as
           np.flatten()
ravel(): Gives the view of the array.
         Ravel is a library level function, can be written as np.ravel() 

"""