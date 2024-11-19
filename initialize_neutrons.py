import numpy as np

def neutrons(count, reactorradius, nenergy): # nenergy is array-like w/ length `count`
    neutron = np.random.uniform(low=0, high=1.0, size=(3, 3, count))  # row 1: location; row 2: direction; multiple particles; row 3 column 1: energy

    x, y, z = neutron[1, :] # component vectors
    vec = np.empty(count) # direction vector
    for i in range(count):
        vec[i] = (np.sum(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)) ** 0.5 # magnitude of direction vector
    neutron[1, :] = neutron[1, :] / vec  # direction vector has length 
    
    neutron[2, 0] = nenergy # set neutron energy

    # define position in spherical coordinates
    rho = neutron[0, 0] * reactorradius
    phi = neutron[0, 1] * np.pi
    theta = neutron[0, 2] * 2 * np.pi

    sinphi = np.sin(phi)
    cosphi = np.cos(phi)
    sint = np.sin(theta)
    cost = np.cos(theta)

    # convert to cartesian coordinates
    neutron[0, :] = [rho * sinphi * cost, rho * sinphi * sint, rho * cosphi]

    return neutron