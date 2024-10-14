# working with numpy to perform numerical/scientific operations on arrays
# three main characteristics of numpy arrays
# 1.) Homogenous Arrays
# 2.) You cannot add or remove elements from these arrays as you can do with lists but you can modify an array.
# 3.) Rectangular not jagged arrays - every row should have similar number of columns.

# initialize an array using a list
import numpy as np

num_array = np.array([1, 2, 3, 4, 5, 6])
print(num_array)

# accessing an individual element through indexing
print(num_array[0])

# an array is also mutable
num_array[5] = 7
print(num_array)

# lets access multiple elements in the array using slice notation In Python, when you slice a list, it creates a new
# list that contains copies of the elements from the original list. This means that changes made to the new list do
# not affect the original list. However, when you slice a NumPy array, it behaves differently. Instead of making a
# copy, NumPy returns a view of the original array. This view references the same data in memory, meaning that
# changes made to the view will also affect the original array. For example:

try:
    view = num_array[3:]
    view[2] = 7
    print(view)
    print(num_array)
except  IndexError as error:
    print(f"Error : {error}")
finally:
    print("Execution successfully")

# how to create a basic array
# we use various methods to create arrays
# create an array filled with 0s
zero_array = np.zeros(3)

# create an array filled with ones
one_array = np.ones(3)

# create an empty array - fast way
# fill every element later
# the content we can specify is randomly generated
empty_array = np.empty(2)

# You can create an array with a range of elements:
range_array = np.arange(5)
print(range_array)

# as you create this arrays remember, the default data type is always float64(thats why you see a decimal after the
# value)
# you can specify your own datatype
ones_array = np.ones(2, dtype=int)
print(ones_array)

# printing arrays
# 1-D arrays
numbers_arrays = np.arange(12)

# printing 2-D arrays
new_array = np.arange(12).reshape(4, 3)
print(new_array)

# Reshaping Arrays
# you can change the shape of an array using the reshape()
# but remember, the reshaped array should have similar number of items as the original array
# e.g if the origonal array has 12 items, similary the reshaped array should also have 12 items
# To reshape a 1D array of 7 elements, you need to reshape it into shapes that multiply to 7
original_array = np.empty(7, dtype=int)
original_array[:] = [10, 20, 30, 40, 50, 60, 70]

reshaped_array = original_array.reshape((1, 7))
reshaped_array_two = original_array.reshape((7, 1))
