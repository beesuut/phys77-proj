#%% working single particle model before monte-carlo

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pynverse import inversefunc

#%% initial conditions

# initialize a neutron with a random direction, energy, and location

nenergy = 1     # ideally a random value between 5 ish different possibilities
neutron = np.random.uniform(low=-1.0, high=1.0, size =(2,3))    # row 1: location; row 2: direction; columns for 3d
neutron[:, 1] = neutron[:, 1] / np.sum(neutron[:, 1])   # direction vector has length 1

# numbers for pure u238; nenergy = 1 MeV
sf = 13     # mb fission
si = 1300   # mb inelastic
se = 4000   # mb elastic 

# the total crossection is just the sum of the fission, absorbtion (inelastic) and scattering (elastic) crossections
stot = 1   # sf+si+se    I tried this but it gave numbers too low, so I think something is off

n = 1   # densisty = 19.05 #g/cm3 ^^same issue^^

#%% probability of escape

# for a particle density of "n" and a cross section of "s", the free path pdf is given by: 1/ns * e^-x/ns

def pdf(x):
    return (1/(n*stot)*np.exp(-x/(n*stot)))

# integrate the pdf to get a cdf that goes from 0<y<1
def cdf(x):
    return quad(pdf, 0, x)[0]


# from there we pick a random number from 0<y<1, and then we can use that as the y value for the cdf,
# which then can tell us the distance the particle will travel

inverse_cdf = inversefunc(cdf)

tempvar = np.random.uniform(0,1)

dist = inverse_cdf(tempvar)     # distance travelled before interaction


#%% check if particle escapes

neutron[:, 0] = np.add(neutron[:, 0], dist * neutron[:, 1])     # change neutron position by dist in movement direction

pos = np.linalg.norm(neutron[:, 0], axis = 0)   # find final position

#%% 

if pos <= 1:
    prob = np.random.randint(0, sf + si + se)
    if prob < sf:
        # do a fission
        elif prob < (sf + se):
           # change energy

# ignore absorption