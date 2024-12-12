import numpy as np
import matplotlib.pyplot as plt
from reactor_function import reactor

# graphical function varying enrichment levels of uranium to see resulting fission output, with neutron count as an input
def enrichment(n):

    # initiate empty list to be filled with power outputs
    power = []

    # run through reactor function at enrichment levels 1% to 100% 
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 1-0.01*i, 0.01*i, 0, 0)
        power.append(fcount)    # add outputs to power list

    # arrange percentages for x-axis
    X = np.arange(1,101)
    
    plt.plot(X, power, color = 'red')    # graph enrichment data
    plt.vlines([5, 20, 85], 5, 150, color = 'black', linestyle = '--')    # graph vertical lines indicating the boundaries between enrichment categories (natural, reactor-grade, and weapons-grade)
    plt.title('Rate of Fission Based on Enrichment - (with ' + str(n) + ' neutrons)')
    plt.xlabel('% of core that is U-235')
    plt.ylabel('# of fission reactions')
    
    plt.savefig('enrichment.png')
    plt.show()


# graphical function varying moderator to see resulting scattering events, with neutron count as an input
def heavy_water(n):

    # initiate empty list to be filled with scattering event counts
    events = []

    # run through reactor function at moderator levels 1% to 66%, varying 20% enriched uranium makeup accordingly
    for i in range(1, 67):
        fcount, acount, scount, ecount = reactor(n, 0.8*(1-0.01*i), 0.2*(1-0.01*i), 0, 0.01*i)
        events.append(scount)

    # arrange percentages for x-axis
    X = np.arange(1,67)
    
    plt.plot(X, events, color = 'red')    # graph moderator data
    plt.title('Scattering from Heavy Water - (with ' + str(n) + ' neutrons, 20% enrichment)')
    plt.xlabel('% of reactor that is heavy water')
    plt.ylabel('# of scattering events')
    
    plt.savefig('heavy_water.png')
    plt.show()

# graphical function varying control rod "insertion" to see resulting fission output, with neutron count as an input
def boron(n):

    # initiate empty list to be filled with power outputs
    power = []

    # run through reactor function at "insertion" levels 1% of reactor volume to 75%
    for i in range(1, 51):
        fcount, acount, scount, ecount = reactor(n, 0.8*(1-0.01*i), 0.2*(1-0.01*i), 0.01*i, 0)
        power.append(fcount)

    # arrange percentages for x-axis
    X = np.arange(1,51)
    
    plt.plot(X, power, color = 'red')    # graph control rod data
    plt.title('Boron Poisoning Reactor - (with ' + str(n) + ' neutrons, 20% enrichment)')
    plt.xlabel('% of core that is Boron-10')
    plt.ylabel('# of fission reactions')
    
    plt.savefig('boron.png')
    plt.show()

# graphical function varying radius, in cm, to see resulting neutron output and compare to criticality threshold, with neutrons as an input
def criticality_radius(n):

    # initiate empty list to be filled with neutron outputs, ideally approaching chain reaction levels
    chain_reaction = []

    # run through reactor function at radii of 0.1 cm to 10 cm
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 0.8, 0.2, 0, 0, 0.1*i)
        chain_reaction.append(fcount*2.5)    # multiply fission count by average neutrons produced per fission
    
    # arrange radii for x-axis
    X = np.linspace(0.1, 10.1, 100)
    
    plt.plot(X, chain_reaction, color = 'red')     # graph neutron output data
    plt.hlines(n, 0.1, 10, color = 'black', linestyle = '--')    # graph horizontal line indicating threshold for criticality based on input neutrons
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('Radius of core, in cm')
    plt.ylabel('# of neutrons produced')
     
    plt.savefig('criticality_radius_nr.png')
    plt.show()

# graphical function varying distance from the reactor to see resulting number of antineutrinos
def antineutrinos(num, area): # inputs take the number neutrons being modeled and the area of the detector
    prpl_cs, f_sf, f_sa, f_ss, s_sf, s_sa, s_ss, f_stot, s_stot, n_per, n = mixture(0.4, 0.1, 0, 0.5) # runs the regular code for some hard coded volume ratios
    fcount, acount, scount, ecount = reactor(num, 0.4, 0.1, 0, 0.5)

    # this function counts how many antineutrinos are made in total, calculated by multiplying the fissions by 6(assuming that the vast majority of fissions just come from U235
    # and then multiplying 1.5 by the number of absorbtions for U238 and 235 (calculated approximately by taking what fraction of the cross-section they each are and multiplying that by total absorbtion)
    # 1.5 because there are 2 and 1 antineutrinos for U329 and U236 decay chains respecively, and U235 and U238 have approximately the same absorbtion cross-sections
    antineutrinocount = 6*fcount+ 1.5*((prpl_cs[0,1] / np.sum(prpl_cs[:,1])) + (prpl_cs[1,1] / np.sum(prpl_cs[:,1]))+ (prpl_cs[0,3] / np.sum(prpl_cs[:,3]))+ (prpl_cs[1,3] / np.sum(prpl_cs[:,3])))/2
    
    # for a 1 sq meter detector, this is how many antineutrinos will hit it, just an inverse square law as the sphere of emmited antineutrinos gets larger
    flux = []
    for r in range(1, 101):
        numberhit = (((np.arctan(np.sqrt(area)/(2*r)))**2)/np.pi)*antineutrinocount/2
        flux.append(numberhit)

    # make a pretty plot of the results!
    X = np.arange(1,101)
    plt.plot(X, flux, color = 'red')
    plt.title('Number of Antineutrinos incident on a detector - (with ' + str(area) + 'm^2 area)')
    plt.xlabel('Distance from reactor (Meters)')
    plt.ylabel('# of Antineutrinos detected')
    plt.savefig('Neutrinos.png')
    plt.show()
