from initialize_neutrons import *
from check_escape import *
from materials_mixture import *

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
# outputs:
  # f_sf, f_sa, f_ss are summed fast cross-sections; f_stot is total
  # s_sf, s_sa, s_ss are summed slow cross-sections; s_stot is total
  # n is total number of atoms/cm^3 in the mixture; n_per is the atoms/cm^3 per material
  # prpl_cs is an array of all the specific effective cross-sections for each material; the array is organized as:
    #         f_sf  f_sa  f_ss  s_sf  s_sa  s_ss
    # u238
    # u235
    # boron
    # hw

nenergy_initial = np.ones(count)

neutrons = neutrons(count, reactorradius, nenergy_initial) # initialize neutrons for monte carlo

escape(neutrons, count, reactorradius, sa, ss, stot, n)  # runs overall function with inputs, giving outputs printed below

print('fission, absorption, scattering, escape')
print(fcount, acount, scount, ecount)
