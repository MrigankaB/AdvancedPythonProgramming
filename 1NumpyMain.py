import numpy as np

"""
Basic scientific operations include ARR, mat, Int, Diff, 
Stats and much more. but python by default doesn't have any 
of these fundamentals built in. It can inly deal with variables 
and not with array and matrices.


List and numpy array similarities:

* Storing data
* Mutable
* Can be indexed
* Slicing operations are allowed

List and numpy array differences:

* List Can Store different data type
* List may return erroe while performing divide
* List is Built in  in python


Advantages over list:

* Less memory
* fast
* More convinient for mathematical opeations


Ways to create numpy array:

* array(array, shape)
* Arange(start, stop, step)
* zeros(shape)
* ones(shape,dtype,order)
* linspace(start, stop, num)

* eye(r, c, diagonal_index, dtype, order)  or identity(n)

*Random.: rand(s), Randf(s), Randn(s), Randint(low, size)



Attributes:

ndim
shape
size
dtype
itemsize
flag


Indexing:

Selecting:

np.where(condition,array(T,F))
np.select([condition], [array])
np.choose([indices],[arrays(0,1,.....])


"""

#inverse= np.linalg.inv(a)
#
#np.allclose(dot(a,b),np.eye(2))

# A= [a b]
#    [c d]
# A^-1= = 1/ad-bc[d  -b]
#                [-c  a]



np.fill()