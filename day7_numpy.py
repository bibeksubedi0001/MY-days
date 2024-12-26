import numpy as np  # Importing numpy library

# Creating a 1D numpy array 'ar'
ar = np.array([2, 35, 544, 6540])

# Finding the index of the maximum element in the array
print(ar.argmax())  # Outputs 3 (index of the max value 6540)

# Finding the index of the minimum element in the array
print(ar.argmin())  # Outputs 0 (index of the min value 2)

# Returns the indices that would sort the array in ascending order
print(ar.argsort())  # Outputs [0 1 2 3], meaning the array is already sorted
