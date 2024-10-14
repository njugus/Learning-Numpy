import numpy as np

# To reshape a 1D array of 7 elements, you need to reshape it into shapes that multiply to 7
original_array = np.empty(7, dtype=int)
original_array[:] = [10, 20, 30, 40, 50, 60, 70]

reshaped_array = original_array.reshape((1, 7))
reshaped_array_two = original_array.reshape((7, 1))








