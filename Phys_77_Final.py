#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad

##To start, I think we just want to use a random crossection for the system, and just try to do a monte carlo 
##of if a random neutron can escape or not

#Example montecarlo loop
import numpy as np
import math

def MC_ND_Sphere(M, N, R):
    mreps = 100
    volumes = np.empty((mreps))
    exact_volume = (np.pi**(N/2) * R**N) / math.gamma(N/2 + 1)
    
    for i in range(mreps):
        points = np.random.uniform(-R, R, (M, N))
        distances = np.linalg.norm(points, axis = 1)
        inside_sphere = np.sum(distances < R)
        volumes[i] = (2 * R)**N * (inside_sphere / M)

    mean = np.mean(volumes)
    std = np.std(volumes)

    return mean, std, exact_volume


# In[2]:


#I also think we should prioritize getting one particle modeled then switch to monte carlo

#at 1 MeV neutrons
Sf = 10.3 #mb fission
Si = 1300 #mb inelastic
Se = 4000 #mb elastic 

#also a note, for the total crossection, it is just the sum of the fission, absorbtion and scattering crossections
Stot = Sf+Si+Se

N = 19.05 #g/cm3 
#for a particle density of "n" and a cross section of "s"
#the free path pdf is given by: 1/ns * e^-x/ns

def PDF(x):
    return (1/)

#integrate the pdf to get a cdf that goes from 0<y<1

#from there we pick a random number from 0< <1, and then we can use that as the y value for the cdf,
#which then can tell us the distance the particle will travel


#we also need to make a neutron with a random direction, velocity

#we can then compare to see if the distance in the direction of the neutron is travelling to the edge of our
#sphere reactor is greater than or less than the interaction distance we just calculated

#this essentially tells us if our neutron escaped or not, and from here we can do a similar simulation to see 
#what that neutron does (does it get absorbed does it fission or does it scatter)


# In[4]:


import numpy as np

import matplotlib.pyplot as plt

# Define a PDF function (example: Gaussian)
def pdf(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

# Calculate the CDF using numerical integration
def cdf(x):
    return quad(pdf, -np.inf, x)[0]

# Generate x values for plotting
x_vals = np.linspace(-3, 3, 100)

# Calculate corresponding PDF and CDF values
pdf_vals = [pdf(x) for x in x_vals]
cdf_vals = [cdf(x) for x in x_vals]

# Plot the PDF and CDF
plt.plot(x_vals, pdf_vals, label='PDF')
plt.plot(x_vals, cdf_vals, label='CDF')
plt.legend()
plt.show()


# In[ ]:




