import numpy as np

import matplotlib.pyplot as plt

from scipy import signal as sig
from splane import pzmap, bodePlot


C = 1e-6
R1=1e3
R2 = 5e3
R3 = 1e3

wc = 1/(C*R3)


num = np.array([1,-wc*R2/R1])
den = np.array([1,wc])



T = sig.TransferFunction(num , den)


plt.close('all')

bodePlot(T,[0,7],[-5,5], 'none', 'none', 'Filtro Pasa Todo', 1000 )
pzmap(T,True, 'Filtro Pasa Todo', 'none', 'none')

R1_n=R1
R2_n = R2/R1_n

num_n = np.array([1,-R2_n])
den_n = np.array([1,1])

T_n = sig.TransferFunction(num_n , den_n)


bodePlot(T_n,[-2,2],[-5,5] ,'none', 'none', 'Filtro Pasa Todo Normalizado', 1000)
pzmap(T_n,True, 'Filtro Pasa Todo Normalizado', 'none', 'none')

