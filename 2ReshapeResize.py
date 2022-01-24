import numpy as np

a=np.arange(10)
print(a.shape)
b= np.reshape(a,(5,2))  #shape should saisfy the number of elements
print(b)


#Reshape: Doesn't change the data of the element
         #shape should be suitable for the number of elements
# np.reshape(array,shape,order)
# a.reshape(shape,order)


#Resize: Can Change the data of the element, So we can mention any size.
        # repeats from the beginning
# np.resize(array, shape)    #Gives a new array
#a.resize((5,2))    # changes the versional array itself

#help (np.reshape)
