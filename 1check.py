
#matmul() and dot() does the same thing ?

import numpy as np

A= np.array([[1,2,3],
             [3,2,1],
            [1,2,1]])
print("A=",A,"\n")

B= np.array([[1,2,1],
             [1,-1,2],
             [0,1,4]])

print("B=",B,"\n")

C= np.dot(A,B)
print("AB= \n",C,"\n")

D=np.matmul(A,B)
print("AB= \n",D,"\n")


# Calculating the inverse of the matrix
invA= np.linalg.inv(A)
print("Inverse of A is :")
print(invA)


# calculating the determinant of matrix
det = int(np.linalg.det(A))
print("\nDeterminant of given 3X3 square matrix:", det)


# applying matrix.transpose() method
transpose = A.transpose()
print(transpose)


#Creating Empty Matrix
#1
x = np.empty((0, 5))
print('The value is :', x)
print('The shape of matrix is :', x.shape)

# print the matrix consist of 8 random numbers
random = np.empty(8)
print('The matrix with 25 random values: \n', random)

#2
y=np.zeros((4,5))
print(y)

#print(y.arrange())
#print(y.reshape(5,4))



#Row matrix & Coloumn matrix
a=np.arange(3)
b=np.arange(3)[:,np.newaxis]
print(a)
print(b)


"""
#print(puls1.__doc__)


# lamda argument : expression
# small ananomous functio that can take any number of arguments
# but can only have 1 expression
#x= lamda a:a+10
#print(x(5))
#y= lamda a,b,c : a+b+c
#print(x(5,2,7))

#helps to construct an array by using a function
# f= np.fromfunction(lamda a,b:a==b,(3,3))
# print(f)

"""