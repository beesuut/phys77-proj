from density_functions import *

def escape(neutron, count, reactorradius, se, si, stot):

    # allow global counters to update
    global fcount
    global acount
    global ecount
    global scount

    dist = np.empty(count)
    dist = np.array(list((map(lambda x:(inverse_cdf(np.random.uniform(0, 1)).item()), dist))))  # distance travelled before interaction

    # check if particle escapes
    neutron[0, :1] = np.add(neutron[0, :1], dist * neutron[1, :1])  # change neutron position by dist in movement direction

    pos = np.linalg.norm(neutron[0, :], axis=0)  # find final position

    for i in range(count):
        if pos[i] <= reactorradius:  # particle didn't leave
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