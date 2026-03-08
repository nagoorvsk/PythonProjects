import numpy as np

arr = np.array([[1,4,7],
               [2,5,8],
               [3,6,9]])

print("Sum is:", np.sum(arr))
print("Average is:", np.mean(arr, axis=0))

print("Max is:", np.min(arr))
print("Min is:", np.max(arr))

print("Max index is: ", np.argmax(arr))
print("Min index is: ", np.argmin(arr))

print("Prod is: ", np.prod(arr, axis=1))
