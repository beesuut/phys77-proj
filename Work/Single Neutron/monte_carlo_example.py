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