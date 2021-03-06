    
import numpy as np
from scipy.special import binom
from ThredgeCorr import FastThredgeCorrGraph
from ThredgeCorr import ThredgeCorrGraph
from ThredgeCorr import get_degrees_from_edge_list
from cThredgeCorr import get_slow_edge_list, get_edge_list
import networkx as nx
import matplotlib.pyplot as pl



from time import time
N = 1000

N_meas = 10


start = time()
numpymethod = FastThredgeCorrGraph(N,0.49,.5)
[ get_slow_edge_list(N,0.49,numpymethod.t,numpymethod.parameters) for n in range(N_meas) ]
end = time()

print("cpp fast method; N =", N, '; generating ', N_meas, 'networks took', end-start, 'seconds')

start = time()
numpymethod = FastThredgeCorrGraph(N,0.49,.5)
[ get_edge_list(N,0.49,numpymethod.t,numpymethod.parameters) for n in range(N_meas) ]
end = time()

print("cpp fast fast method; N =", N, '; generating ', N_meas, 'networks took', end-start, 'seconds')
