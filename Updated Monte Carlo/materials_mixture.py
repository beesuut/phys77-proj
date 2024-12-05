import numpy as np
import pandas as pd

# unpack data from csv
Materials = pd.read_csv('MaterialsSheet.csv')
numden = Materials['numden'].to_numpy()
materials = Materials.iloc[0:, 1:7].to_numpy()

def mixture(u238, u235, boron, hw):
    densities = np.array([u238, u235, boron, hw])
    
    eff_den = (numden.T * densities).T
    weigh_den = eff_den/sum(eff_den)
    prpl_cs = (materials.T * weigh_den).T
    
    total_cs = [sum(i) for i in zip(*prpl_cs)]
    
    f_sf, f_sa, f_ss, s_sf, s_sa, s_ss = total_cs * (10 ** (-24))
    
    f_stot = f_sf + f_sa + f_ss
    s_stot = s_sf + s_sa + s_ss
    n = np.sum(eff_den) * (10**22)
    
    return f_sf, f_sa, f_ss, s_sf, s_sa, s_ss, f_stot, s_stot, n