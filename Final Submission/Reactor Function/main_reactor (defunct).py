import numpy as np
from initialize_neutrons import neutrons
from check_escape import escape
from materials_mixture import mixture

#inputs:
    # count = number of neutrons
    # u238 = uranium-238, as a percentage of the total volume of the reactor
    # u235 = uranium-235, as % of the total V
    # boron = boron-10, as % of the total V
    # hw = heavy water, as % of the total V
    # reatorradius = the cm radius of reactor, set at 1

def reactor(count, u238, u235, boron, hw, reactorradius = 1):

    prpl_cs, f_sf, f_sa, f_ss, s_sf, s_sa, s_ss, f_stot, s_stot, n_per, n = mixture(u238, u235, boron, hw)  # outputs all needed atom totals and cross-sections

    #All neutrons start with energy level = 1
    nenergy_initial = np.ones(count)
    
    neutron = neutrons(count, reactorradius, nenergy_initial) # initialize neutrons for monte carlo
    
    fcount, acount, scount, ecount = \
        escape(neutron, count, reactorradius, f_sa, f_ss, s_sa, s_ss, f_stot, s_stot, prpl_cs, n) \
    # runs overall function with inputs, giving outputs printed below
    
    return fcount, acount, scount, ecount
