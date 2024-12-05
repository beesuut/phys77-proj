import numpy as np
import pandas as pd

# unpack data from csv
Materials = pd.read_csv('MaterialsSheet.csv')

numden = Materials['numden'].to_numpy()    # extract specifically the numerical densities of each material for later use
materials = Materials.iloc[0:, 1:7].to_numpy()    # extract the rest of the data from the DataFrame

# establish function to be used in comprehensive_monte_carlo
def mixture(u238, u235, boron, hw):    # input volume percentages for each material
    densities = np.array([u238, u235, boron, hw])    # turn inputs into an array

    # process the volume densities for each material into weighted proportions of the total number of atoms
    eff_den = (numden.T * densities).T
    weigh_den = eff_den/sum(eff_den)

    # multiply each row of cross-sections from the csv by their weighted proportions
    prpl_cs = (materials.T * weigh_den).T
    total_cs = [sum(i) for i in zip(*prpl_cs)]    # sum each column for total cross-sections

    # unpack total_cs list into fast & slow cm^2 fission, absorption, and scattering cross-sections
    f_sf, f_sa, f_ss, s_sf, s_sa, s_ss = total_cs * (10 ** (-24))    # although unpacking is generally inefficient strategy, necessary  for usage across modules
    
    f_stot = f_sf + f_sa + f_ss    # total fast cross-section
    s_stot = s_sf + s_sa + s_ss    # total slow cross-section
    n = np.sum(eff_den) * (10**22)    # atoms/cm^3
    
    return f_sf, f_sa, f_ss, s_sf, s_sa, s_ss, f_stot, s_stot, n
