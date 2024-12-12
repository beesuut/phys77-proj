import numpy as np
import matplotlib.pyplot as plt
from reactor_function_w_reflectivity import reactor

# graphical function varying enrichment levels to see resulting neutron output and compare to criticality threshold, with neutrons and reactor radius as an input
def criticality_enrichment(n, reactorradius):
    
    # initiate empty list to be filled with neutron outputs, ideally approaching chain reaction levels
    chain_reaction = []
    
    # run through reactor function at enrichment levels 1% to 100% 
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 1-0.01*i, 0.01*i, 0, 0, 0.5, reactorradius)
        chain_reaction.append(fcount*2.5)    # multiply fission count by average neutrons produced per fission
    
    # arrange percentages for x-axis
    X = np.arange(1,101)
    
    plt.plot(X, chain_reaction, color = 'red')    # graph neutron output data
    plt.hlines(n, 0, 100, color = 'black', linestyle = '--')    # graph horizontal line indicating threshold for criticality based on input neutrons
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('% of core that is U-235')
    plt.ylabel('# of neutrons produced')
    
    plt.savefig('criticality_enrichment_r.png')
    plt.show()

# graphical function varying radius, in cm, to see resulting neutron output and compare to criticality threshold, with neutrons as an input
def criticality_radius(n):
    
    # initiate empty list to be filled with neutron outputs, ideally approaching chain reaction levels
    chain_reaction = []
    
    # run through reactor function at radii of 0.1 cm to 10 cm
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 0.8, 0.2, 0, 0, 0.5, 0.1*i)
        chain_reaction.append(fcount*2.5)    # multiply fission count by average neutrons produced per fission
    
    # arrange radii for x-axis
    X = np.linspace(0.1, 10.1, 100)
    
    plt.plot(X, chain_reaction, color = 'red')     # graph neutron output data
    plt.hlines(n, 0.1, 10, color = 'black', linestyle = '--')    # graph horizontal line indicating threshold for criticality based on input neutrons
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('Radius of core, in cm')
    plt.ylabel('# of neutrons produced')
     
    plt.savefig('criticality_radius_r.png')
    plt.show()

def criticality_reflectivity(n, reactorradius):
    
    # initiate empty list to be filled with neutron outputs, ideally approaching chain reaction levels
    chain_reaction = []
    
    # run through reactor function at radii of 0.1 cm to 10 cm
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 0.8, 0.2, 0, 0, 0.01*i, reactorradius)
        chain_reaction.append(fcount*2.5)    # multiply fission count by average neutrons produced per fission
    
    # arrange radii for x-axis
    X = np.linspace(0.01, 1, 100)
    
    plt.plot(X, chain_reaction, color = 'red')     # graph neutron output data
    plt.hlines(n, 0.1, 10, color = 'black', linestyle = '--')    # graph horizontal line indicating threshold for criticality based on input neutrons
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('Radius of core, in cm')
    plt.ylabel('# of neutrons produced')
     
    plt.savefig('criticality_radius_r.png')
    plt.show()