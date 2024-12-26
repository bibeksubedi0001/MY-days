#Array_creation::
#Conversion_from_other_Python_structures
import numpy as np

# From list
list_data = np.array([[2, 3, 4], [5, 47, 43], [42, 565, 756], [344, 464, 646]])
print(list_data)
print(list_data.shape)  # Shape of the array
print(list_data.size)   # Total number of elements
print(list_data.dtype)  # Data type of elements
print(type(list_data))  # Type of object

# From set
set_data = np.array(list({4, 3, 56, 6, 5, 7658}))  # Convert set to list first
print(set_data)
print(type(set_data))   # Type of object

# From tuple
tuple_data = np.array((5, 67, 865, 46578))
print(tuple_data)
print(type(tuple_data))  # Type of object

# From dict
dict_data = np.array(list({4: 4, "RAM": 54, 989: "Bibek"}.keys()))  # Convert dict keys to list
print(dict_data)
print(type(dict_data))  # Type of object
