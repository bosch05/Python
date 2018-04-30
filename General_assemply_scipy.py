import numpy as np
from scipy import stats

sample = [3, 75, 98, 2, 10, 3, 14, 99, 44, 25, 31, 100, 356, 4, 23, 55, 327, 64, 6, 20]

mean = np.mean(sample)
print(mean)

median = np.median(sample)
print(median)

mode = stats.mode(sample)
print(mode)
