import numpy as np
from numpy import random
from numpy.core.records import array

#------------- Review ------------------#


#  0-D array
arr = np.array(42)
print ("0-D Array")
print(arr,"\n")

# 1-D array 
arr1 = np.array([1, 2, 3, 4, 5])
print ("1-D Array")
print(arr1)
print ("First Element = ",arr1[0],"\n")


# 2-D array
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print ("2-D Array")
print(arr2)
print("5th element on 1st dim:",arr2[0,4],"\n") 


# 3-D array
arr3 = np.array([[[1,2,3,4,5], [6,7,8,9,10]]])
print ("3-D Array")
print(arr3)
print (arr3.ndim)
print(arr3[0,0,1],"\n")


arr3n = np.array ([[[9,10],[11,12]],[[5,6],[7,8]],[[1,2],[3,4]]])
print(arr3n)
print('Test =', arr3n[2,1,1],"\n")

# 4-D array
arr4 = np.array([[[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]])
print ("4-D Array")
print(arr4)
print (arr4.ndim)
print('Hi ', arr4[0,0,1,1])
print('Bye', arr4[0,0,1,4],"\n")

arr4n = np.array ([[[[1,2],[3,4],[5,6],[7,8]]],[[[9,10],[11,12],[13,14],[15,16]]]])
print(arr4n)

print('Test2 =', arr4n[1,0,0,0],"\n")

# 5-D array
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print ("5-D Array")
print(arr5)
print (arr5.ndim)
print(arr5[0,0,0,0,3])


# --------------------------- Negative Indexing --------------------------- #

arrn = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arrn[1, -1]) 


# --------------------------- Slicing --------------------------- #
arrm = np.array([1,2,3,4,5,6,7,8,9,10])
print(arrm[1:5]) 
print(arrm[::2]) 
print(arrm[1:5:2]) 

arrz = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('\narrz:',arrz[1, 1:4]) 

# --------------------------- Data Type --------------------------- #
arrm = np.array([1,2,3,4,5,6,7,8,9,11])
print (arrm.shape)


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) 
print ('Print=',arr.reshape(1,8))
print ('Print=',arr.reshape(2,2,2))
arr4n = np.array ([[[[1,2],[3,4],[5,6],[7,8]]],[[[9,10],[11,12],[13,14],[15,16]]]])
print (arr4n.reshape(-1))



# arr4n = np.array ([[[[1,2],[3,4],[5,6],[7,8]]],[[[9,10],[11,12],[13,14],[15,16]]]])
# print (arr4n[1,0,3,1])
# print(arr4n.shape)


arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

for i in arr2:
    for j in i:
        print (j)


arr3 = np.array([[[1,2,3,4,5], [6,7,8,9,10]]])

for i in arr3:
    for j in i:
        for k in j:
            print (k)
