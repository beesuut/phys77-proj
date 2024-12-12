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
    for i in range(1, 76):
        fcount, acount, scount, ecount = reactor(n, 0.8*(1-0.01*i), 0.2*(1-0.01*i), 0.01*i, 0)
        power.append(fcount)

    # arrange percentages for x-axis
    X = np.arange(1,76)
    
    plt.plot(X, power, color = 'red')    # graph control rod data
    plt.title('Boron Poisoning Reactor - (with ' + str(n) + ' neutrons, 20% enrichment)')
    plt.xlabel('% of core that is Boron-10')
    plt.ylabel('# of fission reactions')
    
    plt.savefig('boron.png')
    plt.show()

# graphical function varying enrichment levels to see resulting fission output and compare to criticality threshold, with neutrons as an input
def criticality_enrichment(n):

    # initiate empty list to be filled with power outputs, ideally approaching chain reaction levels
    chain_reaction = []

    # run through reactor function at enrichment levels 1% to 100% 
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 1-0.01*i, 0.01*i, 0, 0)
        chain_reaction.append(fcount*2.5)    # multiply fission count by average neutrons produced per fission

    # arrange percentages for x-axis
    X = np.arange(1,101)
    
    plt.plot(X, chain_reaction, color = 'red')    # graph neutron output data
    plt.hlines(n, 0, 100, color = 'black', linestyle = '--')    # graph horizontal line indicating threshold for criticality based on input neutrons
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('% of core that is U-235')
    plt.ylabel('# of neutrons produced')
    
    plt.savefig('criticality.png')
    plt.show()


def antineutrinos(num, area):
    prpl_cs, f_sf, f_sa, f_ss, s_sf, s_sa, s_ss, f_stot, s_stot, n_per, n = mixture(0.4, 0.1, 0, 0.5)
    fcount, acount, scount, ecount = reactor(num, 0.4, 0.1, 0, 0.5)
    
    antineutrinocount = 6*fcount+ 1.5*((prpl_cs[0,1] / np.sum(prpl_cs[:,1])) + (prpl_cs[1,1] / np.sum(prpl_cs[:,1]))+ (prpl_cs[0,3] / np.sum(prpl_cs[:,3]))+ (prpl_cs[1,3] / np.sum(prpl_cs[:,3])))/2
    
    # for a 1 sq meter detector, this is how many antineutrinos will hit it
    flux = []
    for r in range(1, 101):
        numberhit = (((np.arctan(np.sqrt(area)/(2*r)))**2)/np.pi)*antineutrinocount/2
        flux.append(numberhit)
    
    X = np.arange(1,101)
    plt.plot(X, flux, color = 'red')
    plt.title('Number of Antineutrinos incident on a detector - (with ' + str(area) + 'm^2 area)')
    plt.xlabel('Distance from reactor (Meters)')
    plt.ylabel('# of Antineutrinos detected')
    plt.savefig('Neutrinos.png')
    plt.show()
