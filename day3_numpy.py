#Array_creation::
#Intrinsic numpy array creation objects
import numpy as np
# ram=np.zeros((34,21,42,576,869))

# Zeros array
# Creates a 3x6 array filled with zeros
ram = np.zeros((3, 6))
print("Zeros Array Data Type:", ram.dtype)
print(ram)

# Range array
# Creates an array with values from 0 to 4
sam = np.arange(5)
print("Range Array (0 to 4):", sam)

# Creates an array with values from 3 to 41
dam = np.arange(3, 42)
print("Range Array (3 to 41):", dam)

# Linspace array
# Creates an array with 3 evenly spaced values between 10 and 6
space = np.linspace(10, 6, 3)
print("Linspace Array (10 to 6, 3 values):", space)

# Empty array
# Creates an empty 2x3 array (uninitialized, may contain arbitrary values)
empt = np.empty((2, 3))
print("Empty Array (2x3):")
print(empt)

# Empty like array
# Creates an empty array with the same shape as 'space' (linspace array)
empt1 = np.empty_like(space)
print("Empty Like Array (same shape as linspace array):")
print(empt1)

# Identity matrix
# Creates a 2x2 identity matrix
identity_the = np.identity(2)
print("Identity Matrix (2x2):")
print(identity_the)

# Ones array
# Creates a 4x5 array filled with ones
ones_arr = np.ones((4, 5))
print("\nOnes Array (4x5):\n", ones_arr)

# Full array
# Creates a 3x3 array filled with a specific value (e.g., 7)
full_arr = np.full((3, 3), 7)
print("\nFull Array (3x3, filled with 7):\n", full_arr)

# Eye (identity) matrix
# Creates a 4x4 identity matrix
eye_arr = np.eye(4)
print("\nIdentity Matrix (4x4):\n", eye_arr)

# Diagonal array
# Creates a 1D array and places it on the diagonal of a 4x4 matrix
diag_arr = np.diag([10, 20, 30, 40])
print("\nDiagonal Matrix with elements 10, 20, 30, 40:\n", diag_arr)

# Random array
# Creates a 2x3 array with random values between 0 and 1
random_arr = np.random.random((2, 3))
print("\nRandom Array (2x3):\n", random_arr)

# Random integers
# Creates a 3x3 array with random integers between 1 and 50
rand_int_arr = np.random.randint(1, 50, (3, 3))
print("\nRandom Integer Array (3x3, integers between 1 and 50):\n", rand_int_arr)

# Arange array
# Creates an array with values from 10 to 30 with a step of 2
arange_arr = np.arange(10, 30, 2)
print("\nArange Array (10 to 30, step of 2):\n", arange_arr)

# Logspace array
# Creates an array of 5 values evenly spaced on a log scale between 10^1 and 10^3
logspace_arr = np.logspace(1, 3, 5)
print("\nLogspace Array (log scale from 10^1 to 10^3, 5 values):\n", logspace_arr)

