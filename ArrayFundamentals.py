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

