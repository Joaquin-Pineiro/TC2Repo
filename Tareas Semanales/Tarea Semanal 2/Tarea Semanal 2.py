import numpy as np

import matplotlib.pyplot as plt

from scipy import signal as sig
from splane import pzmap, bodePlot, pretty_print_bicuad_omegayq


C = 10e-6
R1=10e3
R2 = 300e3
R3 = 100e3

w0 = 1/(C*R3)


num = np.array([-R3/R1  * w0**2])
den = np.array([1,1/(C*R2),w0**2])



T = sig.TransferFunction(num , den)


plt.close('all')

pretty_print_bicuad_omegayq(num, den, displaystr = True)

bodePlot(T,[-2,2],[30,-10], 'none', 'none', 'Filtro Pasa Bajos', 1000 )
pzmap(T,True, 'Filtro Pasa Bajos', 'none', 'none')

##TRANSFERENCIA NORMALIZADA
Omega_z=R3
Omega_w=w0
R1_n=R1/Omega_z
R2_n = R2/Omega_z
R3_n=R3/Omega_z
C_n=C*Omega_z*Omega_w



num_n = np.array([-1/R1_n])
den_n = np.array([1,1/(R2_n),1])

T_n = sig.TransferFunction(num_n , den_n)


pretty_print_bicuad_omegayq(num_n, den_n, displaystr = True)


bodePlot(T,[-2,2],[30,-10], 'none', 'none', 'Filtro Pasa Bajos', 1000 )
pzmap(T_n,True, 'Filtro Pasa Todo Normalizado', 'none', 'none')


##TRANSFERENCIA Butterworth con epsilon=1 (WB = W0)

R2=70e3
num_b = np.array([-R3/R1  * w0**2])
den_b = np.array([1,1/(C*R2),w0**2])



T_b = sig.TransferFunction(num_b , den_b)

pretty_print_bicuad_omegayq(num_b, den_b, displaystr = True)

bodePlot(T_b,[-2,2],[30,-10], 'none', 'none', 'Filtro Pasa Bajos ButterWorth', 1000 )
pzmap(T_b,True, 'Filtro Pasa Todo ButterWorth', 'none', 'none')

