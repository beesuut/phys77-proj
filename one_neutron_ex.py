#%% working single particle model before monte-carlo

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pynverse import inversefunc

#%% initial conditions

radiusofreactor = 1 #cm

fcount = 0 #initialize counts of events for MC sim
acount = 0
ecount = 0
scount = 0

# numbers for pure u238; nenergy = 1 MeV
sf = 0.013* (10**(-24))     # cm^2 crossection fission
si = 1.300* (10**(-24))    # cm^2 crossection inelastic
se = 4.000* (10**(-24))    # cm^2 crossection elastic 
n = 4.98*(10**22) #atoms/cm^3
stot = sf+si+se  # the total crossection is just the sum of the crossections


# initialize a neutron with a random direction, energy, and location

nenergy = 1     # 1 is a fast/high energy neutron, all neutrons are made this way
neutron = np.random.uniform(low=-1.0, high=1.0, size =(2,3))    # row 1: location; row 2: direction; columns for 3d
neutron[1,:] = neutron[1, :] / ((np.sum((neutron[1, :])**2))**0.5)    # direction vector has length 1

#convert the spherical coordinates to cartesian coordinates
ρ = neutron[0,0]*radiusofreactor
φ = neutron[0,1]*np.pi
θ = neutron[0,2]*np.pi
neutron[0,:] = [ρ*np.sin(φ)*np.cos(θ),ρ*np.sin(φ)*np.sin(θ),ρ*np.cos(φ)]



#%% probability of escape

# for a particle density of "n" and a cross section of "s", the free path pdf is given by: ns * e^-xns

def pdf(x):
    return ((n*stot)*np.exp(-x*(n*stot)))

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
    global radiusofreactor
    
    inverse_cdf = inversefunc(cdf)

    dist = inverse_cdf(np.random.uniform(0,1))     # distance travelled before interaction

    # check if particle escapes

    neut[:, 0] = np.add(neut[:, 0], dist * neut[:, 1])     # change neutron position by dist in movement direction

    pos = np.linalg.norm(neut[:, 0], axis = 0)   # find final position

    if pos <= radiusofreactor:    # particle didn't leave
        prob = np.random.uniform(0, stot*(10**24))
        if prob < sf*(10**24):   # probability of fission
            # do a fission (NEED TO DO)
            fcount += 1     # increase fission count
        elif prob < (sf + se)*(10**24):  # probability of elastic collision
            # change energy if colliding with a light particle(NEED TO DO)
            scount += 1
            escape(neut)    # repeat until fission, absorption, or escape
        else: 
            acount += 1
    else:
        ecount +=1


escape(neutron)
