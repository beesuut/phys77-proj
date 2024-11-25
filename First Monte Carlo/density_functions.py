import numpy as np
from scipy.integrate import quad
from pynverse import inversefunc


# for a particle density of "n" and a cross section of "s", the free path pdf is given by: ns * e^-xns
def pdf(x, n, stot):
    return (n * stot) * np.exp(-x * (n * stot))

# adjust pdf to take input of n (array-like) (NEED TO DO)

# integrate the pdf to get a cdf that goes from 0<y<1
def cdf(x):
    return quad(pdf, 0, x)[0]

# pick a random number from 0-1 to use as the y value for the cdf
# gives the distance the particle will travel
def inv(y, n, stot):
    temperary = inversefunc(cdf, args=(n, stot))
    return temperary(y)
