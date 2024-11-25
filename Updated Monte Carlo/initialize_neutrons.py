import numpy as np

def neutrons(count, reactorradius, nenergy): # nenergy is array-like w/ length `count`
    neutron = np.random.uniform(low=0, high=1.0, size=(3, 3, count))

    #   each slice is a single neutron with position, unit direction, and energy
    #   x           y           z
    #   xdir        ydir        zdir
    #   nenergy     n/a         n/a

    x, y, z = neutron[1] # component vectors
    len = np.empty(count) # length of direction vector
    for i in range(count):
        len[i] = (np.sum(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)) ** 0.5 # pythagorean theorem
    neutron[1] = neutron[1] / len  # write unit direction vector as x, y, z components
    
    neutron[2, 0] = nenergy # set neutron energy

    # define position in spherical coordinates (random 0-1 always within the sphere of reactor)
    rho = neutron[0, 0] * reactorradius
    phi = neutron[0, 1] * np.pi
    theta = neutron[0, 2] * 2 * np.pi

    sinphi = np.sin(phi)
    cosphi = np.cos(phi)
    sint = np.sin(theta)
    cost = np.cos(theta)

    # convert to cartesian coordinates
    neutron[0] = [rho * sinphi * cost, rho * sinphi * sint, rho * cosphi]

    return neutron