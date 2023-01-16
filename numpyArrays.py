import numpy as np

# INDEXING on 2d array

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) 
print(arr_2d)

print(arr_2d[1]) # returns 2nd row (index 1) [20,25,30]])
print(arr_2d[1][0]) # returns 2nd row, 1st column (index 1,0) 20

print(arr_2d[:2,1:]) # returns 1st 2 rows, 2nd column and all columns after it [[10,15],[25,30]]

arr = np.arange(1,11)

print(arr > 4) # returns boolean array [False False False False  True  True  True  True  True  True]


arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)
print(arr_2d.shape) # returns (3,4) 3 rows, 4 columns

print(arr_2d.sum(axis=0)) # returns sum of each column 
print(arr_2d.sum(axis=1)) # returns sum of each row

