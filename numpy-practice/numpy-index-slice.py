import numpy as np

# Index starts from zero...
arr = np.array([5,10,15,20])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

# Printing multiple index at the same time using fancy indexing...
print(arr[[0,2,3]])

# Accessing elements from a 2D array...
arr = np.array([[1,4,7],
                [2,6,8],
                [3,6,9]])

# We are going to have row index and column index. Both started with zero(0)...

# Single element...
print(arr[0,1])

# Multiple elements...
print("Multiple elements:", arr[[0,1],[1,2]])

"""Single row or Single column"""
# Single row and all columns...
print(arr[2])                                         

# All rows and single column...
print(arr[:,2])

"""Multiple rows and multiple columns"""
# Printing multiple rows based on index at the same time...
print(arr[[0,2]])                                       # Multiple rows

# All rows and multiple columns...
print(arr[:,[0,2]])

""" Basic slicing for single element and Fancy indexing for multiple elements"""