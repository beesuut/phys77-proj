from initialize_neutrons import *
from check_escape import *

reactorradius = 1  # cm

count = 3  # neutrons

# event counters
fcount = 0      # fission
acount = 0      # absorption
scount = 0      # scattering
ecount = 0      # escape

# numbers for pure u238; nenergy = 1 MeV
sf = 0.013 * (10 ** (-24))      # cm^2 fission crossection
sa = 1.300 * (10 ** (-24))      # cm^2 absorption crossection
ss = 4.000 * (10 ** (-24))      # cm^2 scattering crossection
stot = (sf + sa + ss)           # total crossection
n = 4.98 * (10**22)             # atoms/cm^3

nenergy_initial = np.ones(count)

neutrons = neutrons(count, reactorradius, nenergy_initial) # initialize neutrons for monte carlo

escape(neutrons, count, reactorradius, sa, ss, stot, n)

print('fission, absorption, scattering, escape')
print(fcount, acount, scount, ecount)