# matrixsketcher/fast_transforms.py


import numpy as np
from numpy.random import default_rng
from scipy.sparse import isspmatrix
from ._utils import _is_power_of_two


def fft(X):
    """
    FFT along columns. Not a FWHT.
    ...
    """
    if isspmatrix(X):
        X = X.toarray()
    return np.fft.fft(X, axis=0).real


def fwht(X, random_state=None, pad_or_error="error"):
    """
    Randomized FWHT with optional zero-padding.
    ...
    """
    rng = default_rng(random_state)
    if isspmatrix(X):
        X = X.toarray()
    n, p = X.shape

    if not _is_power_of_two(n):
        if pad_or_error == "error":
            raise ValueError(f"{n} not a power of 2.")
        elif pad_or_error == "pad":
            n_power2 = 1 << (n - 1).bit_length()
            X = np.vstack([X, np.zeros((n_power2 - n, p))])
            n = n_power2
        else:
            raise ValueError("pad_or_error must be 'error' or 'pad'")

    signs = rng.choice([-1, 1], size=n)
    X = (X.T * signs).T

    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = X[j]
                y = X[j + h]
                X[j] = x + y
                X[j + h] = x - y
        h *= 2

    return X
