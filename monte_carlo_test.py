# %% monte carlo test

import numpy as np
from scipy.integrate import quad
from pynverse import inversefunc

# %% initial conditions

radiusofreactor = 1  # cm

count = 100  # number of neutrons

fcount = 0  # initialize counts of events for MC sim
acount = 0
ecount = 0
scount = 0

# numbers for pure u238; nenergy = 1 MeV
sf = 0.013 * (10 ** (-24))  # cm^2 crossection fission
si = 1.300 * (10 ** (-24))  # cm^2 crossection inelastic
se = 4.000 * (10 ** (-24))  # cm^2 crossection elastic
n = 4.98 * (10**22)  # atoms/cm^3
stot = (sf + si + se)  # the total crossection is just the sum of the crossections


# initialize a neutron with a random direction, energy, and location

nenergy = 1  # 1 is a fast/high energy neutron, all neutrons are made this way
neutron = np.random.uniform(low=0, high=1.0, size=(2, 3, count))  # row 1: location; row 2: direction; multiple particles

x, y, z = neutron[1, :] # component vectors
vec = np.zeros(count) # direction vector
for i in range(count):
    vec[i] = (np.sum(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)) ** 0.5 # magnitude of direction vector
neutron[1, :] = neutron[1, :] / vec  # direction vector has length 1

# define position in spherical coordinates
rho = neutron[0, 0] * radiusofreactor
phi = neutron[0, 1] * np.pi
theta = neutron[0, 2] * 2 * np.pi

sinphi = np.sin(phi)
cosphi = np.cos(phi)
sint = np.sin(theta)
cost = np.cos(theta)

# convert to cartesian coordinates
neutron[0, :] = [rho * sinphi * cost, rho * sinphi * sint, rho * cosphi]


# %% probability of escape

# for a particle density of "n" and a cross section of "s", the free path pdf is given by: ns * e^-xns


def pdf(x):
    return (n * stot) * np.exp(-x * (n * stot))


# integrate the pdf to get a cdf that goes from 0<y<1
def cdf(x):
    return quad(pdf, 0, x)[0]


# from there we pick a random number from 0<y<1, and then we can use that as the y value for the cdf,
# which then can tell us the distance the particle will travel


def escape(neut):
    global fcount
    global acount
    global ecount
    global scount

    inverse_cdf = inversefunc(cdf)

    dist = np.empty(count)

    map(inverse_cdf, dist)  # distance travelled before interaction

    # check if particle escapes

    neut[0, :] = np.add(neut[0, :], dist * neut[1, :])  # change neutron position by dist in movement direction

    pos = np.linalg.norm(neut[0, :], axis=0)  # find final position

    for i in range(count):
        if pos[i] <= radiusofreactor:  # particle didn't leave
            prob = np.random.uniform(0, stot * (10**24))
            if prob < se * (10**24):  # probability of elastic collision
                # append position and velocity into new list of neutrons; use recursion to run escape(newlist) (NEED TO DO)
                # change energy if colliding with a light particle; requires newlist to have 4th dimension of energy; may need to redefine pdf(x) (NEED TO DO)
                scount += 1
            elif prob < (se + si) * (10**24):  # probability of inelastic collision
                acount += 1
            else:
                # do a fission (NEED TO DO)
                fcount += 1  # increase fission count
        else:
            ecount += 1


escape(neutron)

print(fcount, acount, scount, ecount)
