"""
Mriganka Bezbarauah (Cse21005)
Dizu Raj Madhukalya (Cse21008)

"""

import numpy as np

A= np.array([[1,2],
             [4,5],
             [7,8]])
print("A=",A,"\n")

B= np.array([[1,1,0],
             [0,1,1],
             [1,0,1]])

print("B=",B,"\n")
print("Dimension of A: ",A.ndim)
print("Dimension of B: ",B.ndim)

print("Shape of A: ",A.shape)
print("Shape of B: ",B.shape)

print("size of A: ",A.size,"elements")
print("size of B: ",B.size,"elements")

print("Data type of A: ",A.dtype)
print("Data type of B: ",B.dtype)

print("Each element of A takes",A.itemsize,"bytes")
print("Each element of B takes",B.itemsize,"bytes\n")

if A.shape==B.shape:
    C = np.add(A, B)
    print("A+B= ",C)
else:
    print("Can't be added! Try matrices of same dimension")


