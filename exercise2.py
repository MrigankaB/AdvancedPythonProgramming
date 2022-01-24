"""
Mriganka Bezbarauah(Cse21005)
Dizu Raj Madhukalya(Cse21008)

"""

import numpy as np

A= np.array([[1,2,3],
             [3,2,1]])
print("A=",A,"\n")

B= np.array([[1,2],
             [1,-1],
             [0,1]])

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
print("AB= \n",C,"\n")
print("Dimension of resultant matrix AB is ",C.ndim)
print("Shape of AB: ",C.shape)
print("size of AB: ",C.size,"elements")
print("Data type of AB: ",C.dtype)
print("Each element of AB takes",C.itemsize,"bytes\n")

D= np.matmul(B,A)

Compare= C.tolist()==D.tolist()
print("AB=BA is",Compare)