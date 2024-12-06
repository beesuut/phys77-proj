import numpy as np
import matplotlib.pyplot as plt
from reactor_function import reactor

def enrichment(n):
    
    power = []
    
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 1-0.01*i, 0.01*i, 0, 0)
        power.append(fcount)
    
    X = np.arange(1,101)
    
    plt.plot(X, power, color = 'red')
    plt.vlines([5, 20, 85], 5, 150, color = 'black', linestyle = '--')
    plt.title('Rate of Fission Based on Enrichment - (with ' + str(n) + ' neutrons)')
    plt.xlabel('% of core that is U-235')
    plt.ylabel('# of fission reactions')
    
    plt.savefig('enrichment.png')
    plt.show()

def heavy_water(n):
    
    events = []
    
    for i in range(1, 67):
        fcount, acount, scount, ecount = reactor(n, 0.8*(1-0.01*i), 0.2*(1-0.01*i), 0, 0.01*i)
        events.append(scount)
    
    X = np.arange(1,67)
    
    plt.plot(X, events, color = 'red')
    plt.title('Scattering from Heavy Water - (with ' + str(n) + ' neutrons, 20% enrichment)')
    plt.xlabel('% of reactor that is heavy water')
    plt.ylabel('# of scattering events')
    
    plt.savefig('heavy_water.png')
    plt.show()

def boron(n):
    
    power = []
    
    for i in range(1, 76):
        fcount, acount, scount, ecount = reactor(n, 0.8*(1-0.01*i), 0.2*(1-0.01*i), 0.01*i, 0)
        power.append(fcount)
    
    X = np.arange(1,76)
    
    plt.plot(X, power, color = 'red')
    plt.title('Boron Poisoning Reactor - (with ' + str(n) + ' neutrons, 20% enrichment)')
    plt.xlabel('% of core that is Boron-10')
    plt.ylabel('# of fission reactions')
    
    plt.savefig('boron.png')
    plt.show()

def criticality_enrichment(n):
    
    chain_reaction = []
    
    for i in range(1, 101):
        fcount, acount, scount, ecount = reactor(n, 1-0.01*i, 0.01*i, 0, 0)
        chain_reaction.append(fcount*2.5)
    
    X = np.arange(1,101)
    
    plt.plot(X, chain_reaction, color = 'red')
    plt.hlines(n, 0, 100, color = 'black', linestyle = '--')
    plt.title('Neutrons Produced From Fission - (with ' + str(n) + ' neutrons)')
    plt.xlabel('% of core that is U-235')
    plt.ylabel('# of neutrons produced')
    
    plt.savefig('criticality.png')
    plt.show()

def criticality_neutrons(n_max):
    
    chain_reaction = []
    
    for i in range(1, n_max+1):
        fcount, acount, scount, ecount = reactor(i, 0.8, 0.2, 0, 0)
        chain_reaction.append(fcount*2.5)
    
    X = np.arange(1,n_max+1)
    
    plt.plot(X, chain_reaction, color = 'red')
    plt.hlines(n_max, 0, 100, color = 'black', linestyle = '--')
    plt.title('Neutrons Produced From Fission')
    plt.xlabel('number of neutrons')
    plt.ylabel('# of neutrons produced')
    
    plt.savefig('criticality.png')
    plt.show()