# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 00:46:57 2022

@author: Joaquin
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
##1)

num = np.array(np.convolve([1,0,3], [1,0,1]))
den = np.array(np.convolve([0,0,1], [1,0,2]))

w,Z = sig.freqs(num,den,1000)


plt.close('all')

plt.semilogx(w,20*np.log10(abs(Z)))
plt.xlabel(r'$\omega [rad/s]$')
plt.ylabel(r"$|Z(\omega)|$")
plt.grid(which='both', axis='both')


##2)

num = np.array(np.convolve([0,0,3], [1,0,7/3]))
den = np.array(np.convolve([1,0,2], [1,0,5]))


w,Y = sig.freqs(num,den,1000)


plt.close('all')

plt.semilogx(w,20*np.log10(abs(Y)))
plt.xlabel(r'$\omega [rad/s]$')
plt.ylabel(r"$|Y(\omega)|$")
plt.grid(which='both', axis='both')