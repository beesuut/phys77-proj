import numpy as np
from density_functions import inv

# first function to run through all the possible reaction in the reactor to get counts of which occur
def escape(neutron, count, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n):
    
    # allow global event counters to update
    global fcount
    global acount
    global scount
    global ecount

    dist = np.arange(0,count)

    # Calculates distance travelled before interaction using invCDF fuction and diffentiating between fast (Energy=1) and slow (Energy=0) neutrons
    dist = np.array(list((map(lambda x:inv((np.random.uniform(0, 1)), n, f_stot) if neutron[2,0,int(x)] == 1 else inv((np.random.uniform(0, 1)), n, s_stot), dist))))    
    # check if particle escapes

    neutron[0] = np.add(neutron[0], dist * neutron[1])  # change neutron position by dist in movement direction
    rad = np.linalg.norm(neutron[0], axis=0)  # find final position

    newneutrons = np.zeros((3, 3, count)) # empty array for neutrons that must be re-run

    for i in range(count):
        if neutron[2,0,i] == 1: # if the neutron is a fast neutron
            if rad[i] <= reactorradius:  # particle didn't leave
                prob = np.random.uniform(0, f_stot * (10**24))
                if prob < f_ss * (10**24):  # probability of elastic collision 
                    newneutrons[:, :, i] = neutron[:, :, i] # if the neutron scatters it must be simulated again
                    tempprob = np.random.uniform(0, np.sum(prpl_cs[:,2]))
                    if tempprob < (prpl_cs[:,2][1]+prpl_cs[:,2][0]): # probability of scattering off D20 or boron (uranium scatters dont effect energy of neutron)
                        newneutrons[:,:,i][2,0] = 0 # rewrite the energy of the neutron to be re-simulates as 0, i.e. making it slow
                    scount += 1
                elif prob < (f_ss + f_sa) * (10**24):  # probability of inelastic collision (neutron `gone`)
                    acount += 1
                else: # fission occurs (neutron `gone`)
                    fcount += 1
            else:  # particle left reactor (neutron `gone`)
                ecount += 1
        else: # the neutron is a slow neutron
            if rad[i] <= reactorradius:  # particle didn't leave
                prob = np.random.uniform(0, s_stot * (10**24))
                if prob < s_ss * (10**24):  # probability of elastic collision 
                    newneutrons[:, :, i] = neutron[:, :, i] # if the neutron scatters it must be simulated again
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
            while np.all(newneutrons[:,:,i]==0): # the while statement avoids slices being "skipped" over, also the try except is to avoid the error when the while fails
                newneutrons = np.delete(newneutrons, i, axis=2)
        except:
            i +=1
    newcount = np.size(newneutrons,axis=2)
    if newcount != 0: # if there are neutrons that need to be reran, run the simulation again for them
        escape(newneutrons, newcount, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n)
        
    return fcount, acount, scount, ecount


# second function with purpose of running the first function, but reseting all the global counts first to allow multiple non-accumulative uses
def baseline_escape(neutron, count, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n):
    
    # ties function into global counts
    global fcount
    global acount
    global scount
    global ecount
    
    # resets event counters
    fcount = 0      # fission
    acount = 0      # absorption
    scount = 0      # scattering
    ecount = 0      # escape
    
    # runs escape function and returns outputs
    fcount, acount, scount, ecount = \
        escape(neutron, count, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n)
    
    return fcount, acount, scount, ecount
