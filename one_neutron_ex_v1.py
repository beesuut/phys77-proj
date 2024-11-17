#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
pip install pynverse
from pynverse import inversefunc

#I think we should prioritize getting one particle modeled then switch to monte carlo

#initialize a neutron with a random direction, energy, and location

nenergy = 1 # ideally a random value between 5 ish different possibilities
neutron = np.random.uniform(low=-1.0, high=1.0, size =(2,3)) #first row is location, 2nd row is direction

#numbers below for pure u238
#also for nenergy = 1 MeV
sf = 13 #mb fission
si = 1300 #mb inelastic
se = 4000 #mb elastic 

#the total crossection is just the sum of the fission, absorbtion and scattering crossections
stot = 1    #sf+si+se    I tried this but it gave numbers too low, so I think something is off

n = 1       #   19.05 #g/cm3 ^^^See above ^^^

#for a particle density of "n" and a cross section of "s"
#the free path pdf is given by: 1/ns * e^-x/ns

def pdf(x):
    return (1/(n*stot)*math.exp(-x/(n*stot)))

#integrate the pdf to get a cdf that goes from 0<y<1
def cdf(x):
    return quad(pdf, 0, x)[0]


#from there we pick a random number from 0< <1, and then we can use that as the y value for the cdf,
#which then can tell us the distance the particle will travel

inverse_cdf = inversefunc(cdf)

tempvar = np.random.uniform(0,1)

dist = inverse_cdf(tempvar)

#we can then compare to see if the distance in the direction of the neutron is travelling to the edge of our
#sphere reactor is greater than or less than the interaction distance we just calculated

#I am having some trouble trying to think about the distance traveled, maybe the right way to do this is with 
#linear algebra, saying that the vector direction continues by "dist" then see if that is >1 or <-1 for x,y, or z?
                            
#this essentially tells us if our neutron escaped or not, and from here we can do a similar simulation to see 
#what that neutron does (does it get absorbed, fission, or scatter)

