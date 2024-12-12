# phys77-proj
Physics 77 Capstone Project

Monte Carlo Simulation for an idealized (homogeneous and spherical) nuclear fission reactor.

# Notes on readability:

Comments should be lowercase and begin with a space
    
    '# example comment'

Inline comments should be tabbed at least once

Different comment to separate sections of code within a single file (also allows for python file to be run in blocks like a notebook)

    '#%% defining initial conditions'

# Necessary To-Do:

1. Create CSV with crossections for different energies / elements
2. Adjust existing code to work with an array (from CSV) instead of variables sf, stot, etc.
3. Inverse CDF still producing errors
4. Change neutron velocity and / or energy before doing recursion (check_escape.py)
5. Adjust density functions to be able to account for different energy states / crossections

# Interesting To-Do:
1. Calculate power production, antineutrino flux
2. Plutonium production + decay
3. Create graphs of neutrons v fissions (for different elements) (for different atom densities)
