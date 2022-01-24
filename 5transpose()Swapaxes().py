import numpy as np

# Transpose() : gives view of the orginal array in
               # transpose format

a =np.arange(1,11).reshape(5,2)
b= np.transpose(a)

print(a.shape)
print(b.shape)  # np.transpose(a).shape
 # Transpose is useless for 1-D array
print(b)
print(np.transpose(a,axes=(1,0)))  #Default
print(np.transpose(a,axes=(0,1)))

# a.transposoe()
# a.T


# Swapaxes(): to interchange any two dimension
# np.swapaxes(array,axis1,axis2)
# a.swapaxes(axis1, axis2)



















