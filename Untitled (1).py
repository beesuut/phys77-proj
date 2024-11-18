#!/usr/bin/env python
# coding: utf-8

# In[373]:


#crude montecarlo 

fcount = 0
acount = 0
ecount = 0
scount = 0

radiusofreactor = 5 # in cm

for i in range(2000):
    neutron = np.random.uniform(low=-1.0, high=1.0, size =(2,3))    # row 1: location; row 2: direction; columns for 3d
    neutron[1,:] = neutron[1, :] / ((np.sum((neutron[1, :])**2))**0.5)    # direction vector has length 1

    #convert the spherical coordinates to cartesian coordinates
    ρ = neutron[0,0]*radiusofreactor
    φ = neutron[0,1]*np.pi
    θ = neutron[0,2]*np.pi

    neutron[0,:] = [ρ*np.sin(φ)*np.cos(θ),ρ*np.sin(φ)*np.sin(θ),ρ*np.cos(φ)]
    
    escape(neutron)
print(fcount)
print(acount)
print(ecount)
print(scount)


# In[ ]:




