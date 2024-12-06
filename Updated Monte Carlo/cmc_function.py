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
    
    # initiate event counters
    fcount = 0      # fission
    acount = 0      # absorption
    scount = 0      # scattering
    ecount = 0      # escape

    mixture(u238, u235, boron, hw)  # outputs all needed atom totals and cross-sections

    nenergy_initial = np.ones(count)

    neutrons = neutrons(count, reactorradius, nenergy_initial) # initialize neutrons for monte carlo
    
    escape(__________________)  # runs overall function with inputs, giving outputs printed below
    
    return fcount, acount, scount, ecount
