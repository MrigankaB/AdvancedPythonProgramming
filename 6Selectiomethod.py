import numpy as np

#x=np.array([[0,0,0,1,1]])

x=np.linspace(-5,5,11)
print(x)
def puls(x,position,height,width):
    return height*(x>=position)*(x<=(position+width))

print(puls(x,position=-2, height=1, width=5))
print(puls(x,position=1, height=1, width=5))


def puls1(x,position,height,width):
    "Returns pulse value when the boolean value is true "
    return height * np.logical_and(x>= position,x<=(position + width))

x =np.linspace(-4,4,9)
np.where(x<0,x**2,x**3)


#np.all(x>0)

#np.any(x>0)

#print(np.where(x<0,x**2, x**3))
#print(np.where(x<0,x**2, x**3))

print(np.select([x<-1,x<2,x>=2],[x**2,x**3,x**4]))

print(np.choose([0,0,0,1,1,1,2,2,2],[x**2,x**3,x**4]))
print(np.choose([0,0,0,1,1,1,2,2,2],[x**2,x**3,x**4]))
"""
np.nonzero(abs(x)>2)


x[np.nonzero(abs(x)>2)]
x[abs(x)>2]
"""