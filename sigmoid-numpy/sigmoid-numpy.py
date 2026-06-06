import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    a = np.array(x)
    val = np.divide(1, 1 + np.exp(-a))
    return val

print(sigmoid([0,2,-2]))