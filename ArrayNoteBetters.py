# For testing purposes it is often necessary to generate random arrays
# how to generate random arrays - 1-D arrays
# using np.random.default_rng()

# for generating random integer numbers
import numpy as np

rng = np.random.default_rng()
integer_array = rng.integers(0, 10, 4)


# for generating random float arrays
float_array = rng.random(3)

# for uniformly distributed arrays
uniform_values_array = rng.uniform(0, 10, 3)

# for normal distributed arrays
normal_values_array = rng.normal(5, 2, 3)
print(normal_values_array)

# use the copy() to create a copy of the original array, otherwise direct initialization( b = a) results to creation
# of a view
a = np.array([1, 2, 3, 4, 5])
b = a.copy()
b[1] = 9
print(b)
print(a)

# another powerful way of getting data from an array is using boolean indexing, which allows you
# to use all kinds of logical operators

# boolean indexing
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# get elements greater than 5
# method 1
# print(a[a > 5])

# method 2
# using np.any(condition)
# returns a boolean value if there are elements in the array greater than the value provided
print(np.any(a > 5))

# after knowing true or false, now get those values
print(a[a > 5])


# replace the placeholder elements in the 1D array with our own elements
numbers_array = np.zeros(5, dtype=int)
numbers_array[:] = [10, 20, 30, 40, 50]
print(numbers_array)

# 2D array
my_numbers = np.zeros((2, 3), dtype=int)
my_numbers[:] = [[1, 2, 3], [4, 5, 6]]
print(my_numbers)

# for the empty()
# 1-D arrays
integer_numbers = np.empty(5, dtype=int)
integer_numbers[:] = [100, 200, 300, 400, 500]
print(integer_numbers)

# 2-D arrays
float_numbers = np.empty((2, 3))
float_numbers[:] = [[100, 200, 300],
                    [400, 500, 600]]

print(float_numbers)










