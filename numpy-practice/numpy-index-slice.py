import numpy as np

# Index starts from zero...
arr = np.array([5,10,15,20])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

# Accessing elements from a 2D array...
arr = np.array([[1,4,7],
                [2,6,8],
                [3,6,9]])

# We are going to have row index and column index. Both started with zero(0)...

# Row zero + column 1...
print(arr[0,1])

# First element always represents row. Hence if we provide single value, it is considered as row number...
print(arr[2])

# All rows and 2nd column...
print(arr[:,2])

