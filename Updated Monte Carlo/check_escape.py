from density_functions import *

def escape(neutron, count, reactorradius, sa, ss, stot, n):

    # allow global event counters to update
    global fcount
    global acount
    global scount
    global ecount

    dist = np.empty(count)
    #dist = np.array(list((map(lambda x:(inv((np.random.uniform(0, 1)), n, stot).item()), dist))))  # distance travelled before interaction
    #dist = np.array(list((map(lambda x:(inv((np.random.uniform(0, 1)), n, stotFAST)) if neutron[2,0] == 1 else (inv((np.random.uniform(0, 1)), n, stotSLOW)), dist))))
    for i in neutron:
        if neutron[2, 0, i] == 1:
            dist[i] = lambda x:(inv((np.random.uniform(0, 1)), n, stotFAST))
        else:
            dist[i] = lambda x:(inv((np.random.uniform(0, 1)), n, stotSLOW))
        i+=1
    # check if particle escapes
    #UPDATE THE PARAM NAMES FOR STOTFAST AND STOTSLOW

    neutron[0] = np.add(neutron[0], dist * neutron[1])  # change neutron position by dist in movement direction
    rad = np.linalg.norm(neutron[0], axis=0)  # find final position

    newneutrons = np.zeroes((3, 3, count))

    for i in range(count):
        if rad[i] <= reactorradius:  # particle didn't leave
            prob = np.random.uniform(0, stot * (10**24))
            if prob < ss * (10**24):  # probability of elastic collision (need to account for neutron)
                newneutrons[:, :, i] = neutron[:, :, i]
                scount += 1
            elif prob < (ss + sa) * (10**24):  # probability of inelastic collision (neutron `gone`)
                acount += 1
            else: # fission occurs (neutron `gone`)
                fcount += 1
        else:  # particle left reactor (neutron `gone`)
            ecount += 1

    # re-run function for remaining neutrons from elastic collisions
    newneutrons = newneutrons[~np.all(newneutrons == 0, axis=2)]
    newcount = newneutrons.size(axis = 2)
    if newcount != 0:
        escape(newneutrons, newcount, reactorradius, sa, ss, stot)