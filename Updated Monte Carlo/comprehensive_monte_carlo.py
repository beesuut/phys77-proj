from initialize_neutrons import *
from check_escape import *

reactorradius = 1  # cm

count = 3  # neutrons

# event counters
fcount = 0      # fission
acount = 0      # absorption
scount = 0      # scattering
ecount = 0      # escape

# mixture percentages (of total volume)
u238 = 0.25  # uranium-235 
u235 = 0.25  # uranium-238
boron = 0.25  # boron-10
hw = 0.25  # heavy water

mixture(u238, u235, boron, hw)  # outputs all needed atom totals and cross-sections

nenergy_initial = np.ones(count)

neutrons = neutrons(count, reactorradius, nenergy_initial) # initialize neutrons for monte carlo

escape(neutrons, count, reactorradius, sa, ss, stot, n)  # runs overall function with inputs, giving outputs printed below

print('fission, absorption, scattering, escape')
print(fcount, acount, scount, ecount)
