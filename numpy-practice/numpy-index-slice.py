import numpy as np

# Index starts from zero...
arr = np.array([5,10,15,20])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

# Printing multiple index at the same time using fancy indexing...
print(arr[[0,2,3]])

print("Examples - 2D Array")
# Accessing elements from a 2D array...
arr = np.array([[1,4,7],
                [2,5,8],
                [3,7,9]])
print(arr)

# We are going to have row index and column index. Both started with zero(0)...
# Single element... Index is an integer : Basic indexing
print(arr[0,1])

# Multiple elements... Index is list : Fancy indexig
print("Multiple elements:", arr[[0,1],[1,2]])

# Single row and all columns...
print(arr[2])                                         
# All rows and single column...
print(arr[:,2])

print(arr)

# Rows O to 2 (excluding 2)
print("Slicing example:", arr[0:2,1])

# Printing multiple rows based on index at the same time...
print(arr[[0,2]])                                       # Multiple rows

# All rows and multiple columns...
print(arr[:,[0,2]])
