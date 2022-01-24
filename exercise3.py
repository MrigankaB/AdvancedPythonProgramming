"""
Mriganka Bezbarauah(Cse21005)
Dizu Raj Madhukalya(Cse21008)

"""

import numpy as np

A= np.array([[1,2,1],
             [4,4,5],
             [6,7,7]])
print("A=",A,"\n")

B= np.array([[-7,-7,6],
             [2,1,-1],
             [4,5,-4]])

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

C= np.matmul(A,B)
D= np.matmul(B,A)

I= [[1,0,0],[0,1,0],[0,0,1]]

if C.tolist()==I and D.tolist()==I:
    print("A and B are inverse of each other")
else:
    print("A and B are not inverse of each other")
