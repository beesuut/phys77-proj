import numpy as np
from density_functions import inv

# event counters
fcount = 0      # fission
acount = 0      # absorption
scount = 0      # scattering
ecount = 0      # escape

def escape(neutron, count, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n):
    
    # allow global event counters to update
    global fcount
    global acount
    global scount
    global ecount

    dist = np.arange(0,count)

    dist = np.array(list((map(lambda x:inv((np.random.uniform(0, 1)), n, f_stot) if neutron[2,0,int(x)] == 1 else inv((np.random.uniform(0, 1)), n, s_stot), dist))))    # distance travelled before interaction
    # check if particle escapes

    neutron[0] = np.add(neutron[0], dist * neutron[1])  # change neutron position by dist in movement direction
    rad = np.linalg.norm(neutron[0], axis=0)  # find final position

    newneutrons = np.zeros((3, 3, count))

    for i in range(count):
        if neutron[2,0,i] == 1:
            if rad[i] <= reactorradius:  # particle didn't leave
                prob = np.random.uniform(0, f_stot * (10**24))
                if prob < f_ss * (10**24):  # probability of elastic collision (need to account for neutron)
                    newneutrons[:, :, i] = neutron[:, :, i]
                    tempprob = np.random.uniform(0, np.sum(prpl_cs[:,2]))
                    if tempprob < (prpl_cs[:,2][1]+prpl_cs[:,2][0]):
                        newneutrons[:,:,i][2,0] = 0
                    scount += 1
                elif prob < (f_ss + f_sa) * (10**24):  # probability of inelastic collision (neutron `gone`)
                    acount += 1
                else: # fission occurs (neutron `gone`)
                    fcount += 1
            else:  # particle left reactor (neutron `gone`)
                ecount += 1
        else:
            if rad[i] <= reactorradius:  # particle didn't leave
                prob = np.random.uniform(0, s_stot * (10**24))
                if prob < s_ss * (10**24):  # probability of elastic collision (need to account for neutron)
                    newneutrons[:, :, i] = neutron[:, :, i]
                    scount += 1
                elif prob < (s_ss + s_sa) * (10**24):  # probability of inelastic collision (neutron `gone`)
                    acount += 1
                else: # fission occurs (neutron `gone`)
                    fcount += 1
            else:  # particle left reactor (neutron `gone`)
                ecount += 1

    # re-run function for remaining neutrons from elastic collisions
    for i in range(np.size(newneutrons,axis=2)+1):
        try :
            while np.all(newneutrons[:,:,i]==0):
                newneutrons = np.delete(newneutrons, i, axis=2)
        except:
            i +=1
    newcount = np.size(newneutrons,axis=2)
    if newcount != 0:
        escape(newneutrons, newcount, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n)
        
    return fcount, acount, scount, ecount