import numpy as np

dataset = [1,4,6,2,4,6,23,7,8,32,6,78]

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

print(moving_average(dataset, 3))
