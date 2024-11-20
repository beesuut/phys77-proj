from initialize_neutrons import *
from check_escape import *

reactorradius = 1 # cm

# number of neutrons
count = 100

# initialize event counts
fcount = 0
acount = 0
ecount = 0
scount = 0

# numbers for pure u238; nenergy = 1 MeV
sf = 0.013 * (10 ** (-24))      # cm^2 crossection fission
si = 1.300 * (10 ** (-24))      # cm^2 crossection inelastic
se = 4.000 * (10 ** (-24))      # cm^2 crossection elastic
stot = (sf + si + se)           # the total crossection is just the sum of the crossections
n = 4.98 * (10**22)             # atoms/cm^3

neutrons = neutrons(count, reactorradius, nenergy = np.ones(count))

escape(neutrons, count, reactorradius, se, si, stot)