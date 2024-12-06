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


