import numpy as np

dataset = [1,4,6,2,4,6,23,7,8,32,6,78]

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


def exp_moving_average(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()

    a = np.convolve(values, weights)[:len(values)]
    a[:window] = a[window]
    return a

# print(moving_average(dataset, 3))
print(exp_moving_average(dataset, 3))
