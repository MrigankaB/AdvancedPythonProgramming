#8-12-2021

import numpy as np
import numpy.linalg as la


#Orthogonal vectors
"""
u= np.array([[0],[2]])
v= np.array([[2],[0]])
inner= np.dot(u.T,v)
print(inner)
inner1= la.norm(u)*la.norm(v)*np.cos(rad,0)
if(inner == 0):
    print("u and v are orthogonal vectors")
else:
    print("u and v are not orthogonal")
"""



# Cauchy Schwarz inequality proof
"""
u= np.array([[-1],[2]])
v= np.array([[4],[-2]])
inner=abs(np.dot(u.T,v))
print(inner)
normProd= round(la.norm(u)*la.norm(v),3)
print(normProd)

if( inner!= normProd):
    print("Cauchy Schwarz inequality proved")
else:
    print("Something went wrong")
"""



# Triangular inequality proof
"""
u= np.array([[-1],[2]])
v= np.array([[4],[-2]])

uv_norm1= la.norm(u+v)
print(uv_norm1)

uv_norm2= round(la.norm(u)+ la.norm(v), 3)
print(uv_norm2)

if( uv_norm1 != uv_norm2):
    print("triangular inequality proved")
else:
    print("Something went wrong")
"""



#Projection

u= np.array([[1],[0]])
v= np.array([[2],[1]])
inner= np.dot(u.T,v)
unorm= (la.norm(u))**2
vproj= (inner*u)/unorm
print(vproj)

