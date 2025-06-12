import numpy as np  # Importing numpy library

# Create a 1D numpy array 'art' with some specific values
art = np.array([4, 46, 78, 443, 7456, 83988])

# Create an array 'arr' with a range of values from 0 to 98 (total 99 values)
arr = np.arange(99)

# Print the 1D array 'arr' (this will print numbers from 0 to 98)
print(arr)

# Reshape the 1D array 'arr' into a 3x33 2D array (since 99 is divisible by 3 and 33)
print(arr.reshape(3, 33))

# Reshape the 'art' array into a 2x3 2D array
print(art.reshape(2, 3))

# Assign the reshaped version of 'art' to a variable 'j'
j = art.reshape(2, 3)

# Use the ravel() function to flatten the reshaped 'art' array back into 1D
# Ravel returns a flattened 1D array from the multi-dimensional array
print(j.ravel())
