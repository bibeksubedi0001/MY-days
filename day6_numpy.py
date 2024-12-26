import numpy as np  # Importing numpy library

# Creating a 2D numpy array 'arr'
arr = np.array([[2, 3, 4], [7, 5, 9], [0, 3, 0]])

# Sum of all elements in the array
print(arr.sum())  # Outputs the total sum of all values in the array

# Sum along columns (axis=0), meaning it sums values down each column
print(arr.sum(axis=0))  # Outputs [9 11 13], i.e., sum of columns

# Sum along rows (axis=1), meaning it sums values across each row
print(arr.sum(axis=1))  # Outputs [9 21 3], i.e., sum of rows

# Transpose of the array (rows become columns and vice versa)
print(arr.T)  # Transposes the array, interchanging rows and columns

# 'flat' returns an iterator over all elements of the array in a 1D manner
print(arr.flat)  # Outputs the flat iterator object

# Iterating through the 'flat' iterator to print each element in the array
for item in arr.flat:
    print(item)

# Number of dimensions of the array
print(arr.ndim)  # Outputs the number of dimensions (2D array)

# Number of elements in the array
print(arr.size)  # Outputs the total number of elements (3x3=9 elements)

# Shape of the array (rows, columns)
print(arr.shape)  # Outputs the shape of the array (3 rows, 3 columns)

# Total number of bytes consumed by the elements of the array
print(arr.nbytes)  # Outputs the total memory consumed by the array in bytes

# Creating a 2D numpy array 'arr'
arr = np.array([[2, 3, 4], [7, 5, 9], [0, 3, 0]])

# Finding the index of the maximum element in the flattened array
print(arr.argmax())  # Outputs 5 (index of the max value 9 in the flattened array)

# Finding the index of the minimum element in the flattened array
print(arr.argmin())  # Outputs 6 (index of the min value 0 in the flattened array)

# Finding the indices of the maximum element along columns (axis=0)
print(arr.argmax(axis=0))  # Outputs [1 1 1], i.e., the row indices of the max values for each column

# Finding the indices of the minimum element along rows (axis=1)
print(arr.argmin(axis=1))  # Outputs [0 1 0], i.e., the column indices of the min values for each row

# Returns the indices that would sort each column (axis=0)
print(arr.argsort(axis=0))  # Outputs a sorted index array along the columns
# Example output:
# [[2 0 2]  # For column 1 (2,7,0), sorted order is 0,2,7 (index 2,0,1)
#  [0 1 0]  # For column 2 (3,5,3), sorted order is 3,3,5 (index 0,2,1)
#  [1 2 1]] # For column 3 (4,9,0), sorted order is 0,4,9 (index 2,0,1)

# Returns the indices that would sort each row (default is axis=1)
print(arr.argsort())  # Outputs the sorted index array for each row
# Example output:
# [[0 1 2]  # For row 1 (2,3,4), indices in sorted order are [0,1,2]
#  [0 1 2]  # For row 2 (7,5,9), sorted order is [1,0,2]
#  [0 2 1]] # For row 3 (0,3,0), sorted order is [0,2,1]
