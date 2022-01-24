import numpy as np

#print(np.eye(3,k=-1))

"""
a=np.array( [[1,0,1],[0,1,0]])
print(np.choose(a,[-10,10]))



a= np.array([[4,-1,2],
             [2,-1,4],
             [0,-3,6]])
print(np.where(a<0,a,-1 ))




x = np.array([-3,-2,-1,0,1,2,3])
a= np.float64(x[x < -1])
print(a+20.)



np.full():  Return an array of ones with the same shape and type as a given array.
np.full(shape, fill_value, dtype=None, order='C'
np.full((2, 2), 10)
    array([[10, 10],
           [10, 10]])
           
(1) np.full() function is used to return a new array with the same shape and type as a given 
array filled with a fill_value whereas np.fill() function is used to fill the array with a scalar value.

(2) For np.full(), parameters are (shape, order, dtype, fill_value) while for np.fill(), the 
parameters are value:scalar, such that each element of the defined array shall now contain this value





#let
def f(a,b):
return a+2*b
#now,
print(np.formfunction(f,(2,2),dtype='int'))

#Here np.fromfunction() will take function 'f' as an argument and evaluate the values at #each points/indices of the new 2x2 array of dtype=int. The values of a and b will be the #index values of each element respectively.
#So, the above line gives following output:
# [[ 0 2 ]
# [ 1 3 ]]
"""
x = np.array([-3,-2,-1,0,1,2,3])
x[x < -1]+=20
print(x)

np.fill_diagonal((4,4),3)