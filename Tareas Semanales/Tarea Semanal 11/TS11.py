# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:14:39 2022

@author: Joaquin
"""

import ltspice

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

import splane as splane
import sympy as sim

#%% Punto 1
l = ltspice.Ltspice('TS11.raw')
l.parse()


freq = l.get_frequency()
Z =1/ l.get_data('I(V1)')


plt.close('all')
fig, ax = plt.subplots(1, 1, figsize=(7,7))
fig.suptitle('Impedancia de entrada Z(s)')
ax.semilogx(freq, 20 * np.log10(np.abs(Z)), label='LTSpice',linewidth=3)


ax.grid()
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude (dB)")


num = np.array([1,6,8])
den = np.array([1,4,3])

w,H = sig.freqs(num,den)

ax.semilogx(w/(2*np.pi),20*np.log10(np.abs(H)),label='Python',ls='--',linewidth=3)
ax
plt.legend()
plt.show()

# #%% Mediante Modulo de splane


# s =sim.symbols('s',complex=True)

# ZZ = (s**2 + 6*s+ 8) / (s**2 + 4*s+ 3)

# Z2, RA = splane.remover_valor(ZZ,sigma_zero=6)


# Y2 = 1/Z2

# Y3, YD1,RD1,CD1 = splane.remover_polo_sigma(Y2,sigma=6,isImpedance=False)

# Z3 = 1/Y3

# Z5, RB = splane.remover_valor(Z3,sigma_zero=3.5)

# Y5 = 1/Z5

# Y6, YD2,RD2,CD2 = splane.remover_polo_sigma(Y5,sigma=3.5,isImpedance=False)


#%% Punto 2

l = ltspice.Ltspice('TS11_2.raw')
l.parse()






freq = l.get_frequency()
Z =1/ l.get_data('I(V1)')

fig, ax = plt.subplots(1, 1, figsize=(7,7))
fig.suptitle('Impedancia de entrada Z(s)')

ax.semilogx(freq, 20 * np.log10(np.abs(Z)), label='LTSpice',linewidth=3)


ax.grid()
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude (dB)")


num = np.array([1,1,1])
den = np.array(np.convolve([1,2,5],[1,1]))


w,H = sig.freqs(num,den)

ax.semilogx(w/(2*np.pi),20*np.log10(np.abs(H)),label='Python',ls='--',linewidth=3)

plt.legend()
plt.show()