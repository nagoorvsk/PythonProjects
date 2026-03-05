import numpy as np

# Create a ndarray (N-Dimensional Array)...
arr = np.array([1,2,3,6,7,8])
print("Printing 1D array:\n ",arr)

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]
                   ])
print("Printing 2D array:\n",arr_2d)

# Initializing ndarray...
arr = np.zeros(5)
print(arr)

# Generating an array with evenly spaced values for a provided range...
arr = np.arange(1,20,2)
print(arr)

arr = np.linspace(10,20,2)
print(arr)