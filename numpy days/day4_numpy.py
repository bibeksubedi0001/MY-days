import numpy as np
# 1. Creating a simple array from a list
arr = np.array([1, 2, 3, 4, 5, 6])

# 2. Checking Array Attributes
arr_shape = arr.shape
arr_size = arr.size
arr_dtype = arr.dtype

# 3. Creating arrays with specific values
zeros_arr = np.zeros((2, 3))   # 2x3 array of zeros
ones_arr = np.ones((3, 4))     # 3x4 array of ones
random_arr = np.random.rand(2, 2)  # 2x2 array of random values

# 4. Array Operations
add_2 = arr + 2
multiply_3 = arr * 3
square = arr ** 2

# 5. Array Slicing and Indexing
arr_slice = arr[1:4]           # Elements from index 1 to 3 (exclusive)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
element = matrix[0, 1]         # Element in first row, second column
second_row = matrix[1, :]      # Entire second row

# 6. Reshaping Arrays
reshaped = arr.reshape((2, 3))  # Reshape into 2x3 matrix

# 7. Mathematical Functions
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_max = np.max(arr)
arr_min = np.min(arr)

# Collecting all outputs and printing them properly
print("Simple array:", arr)
print("Shape:", arr_shape)
print("Size:", arr_size)
print("Data type:", arr_dtype)
print("Zeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Random array:\n", random_arr)
print("Array + 2:", add_2)
print("Array * 3:", multiply_3)
print("Array squared:", square)
print("Array slice:", arr_slice)
print("Matrix:\n", matrix)
print("Element (0,1) in matrix:", element)
print("Second row in matrix:", second_row)
print("Reshaped array:\n", reshaped)
print("Sum:", arr_sum)
print("Mean:", arr_mean)
print("Max:", arr_max)
print("Min:", arr_min)
