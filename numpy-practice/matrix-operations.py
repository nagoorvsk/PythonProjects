import numpy as np

# 1D array... 
a = np.array([1,2,3,4,5,6])
print(a)
# 2D array - Row Vector
a = np.array([[1,2,3,4]])
print(a)
# 2D array - Column vector
a = np.array([[1],
              [2],
              [3]])
print(a)

# Element-wise operations
a = np.array([[1,2,4],
              [2,5,8]])
print(a)

b = np.array([[1,2,3]])
print(b)

print(a*b)
print(a+b)

# Matrix multiplication
try:
    print(a@b)
except:
    print("Not a valid operation as columns of first matrix not equal to" \
    "rows of seconf matrix") 

a = np.array([[1,2,3],
              [4,5,6]])
print(a.shape)
b = np.array([[1],[2],[3]])
print(b.shape)

print(a@b)