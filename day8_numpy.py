import numpy as np

# Define two 2x2 numpy arrays
ar = np.array([[2, 3], [6, 7]])
ar0 = np.array([[3, 1], [0, 1]])

# 1. Element-wise addition of arrays
print("Addition of ar and ar0:\n", ar + ar0)

# 2. Element-wise multiplication of arrays (not matrix multiplication)
print("\nElement-wise multiplication of ar and ar0:\n", ar * ar0)

# 3. Element-wise division of arrays
# Note: Division by zero will generate a runtime warning and return 'inf' (infinity) where the division occurs
print("\nElement-wise division of ar by ar0:\n", ar / ar0)

# 4. Square root of each element in the array 'ar'
print("\nSquare root of each element in ar:\n", np.sqrt(ar))

# 5. Where function to get indices where the condition (ar > 3) is true
# This will return the indices where the values in 'ar' are greater than 3
print("\nIndices where elements in ar are greater than 3:\n", np.where(ar > 3))

# 6. Count the number of non-zero elements in 'ar'
print("\nNumber of non-zero elements in ar:\n", np.count_nonzero(ar))

# 7. Return the indices of non-zero elements in 'ar'
# This returns a tuple of arrays (one for each axis) where non-zero elements are found
print("\nIndices of non-zero elements in ar:\n", np.nonzero(ar))
