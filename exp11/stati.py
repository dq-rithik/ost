import numpy as np
from scipy import stats
import statistics
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = np.mean(sample)
print("Sample mean using NumPy:", mean)
print()
mean= stats.describe(sample)
print("Sample mean using SciPy:", mean)

print()
print("Statistics",statistics.mean(sample))
