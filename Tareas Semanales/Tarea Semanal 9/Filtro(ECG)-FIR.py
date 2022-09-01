# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:13:58 2022

@author: Joaquin
"""

import scipy.signal as sig
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

data = genfromtxt('taps.CSV', delimiter=',')




fs = 1e3

f_paso1 = 2.5
f_paso2 = 25
f_stop1 = 1.25
f_stop2 = 35

alpha_max = 5
alpha_min = 45


b = data
f,H = sig.freqz(b,fs=fs)

plt.close('all')
fig,ax = plt.subplots(2,2,figsize=(10,5))
fig.suptitle('Butterworth bandpass filter FIR', fontsize=16)

ax[0,0].plot(f,20*np.log10(abs(1.79*H)))
ax[0,0].set_xlim([0,100])
ax[0,0].set_ylim([-60,10])
ax[0,0].set_xlabel('Frequency [Hz]')
ax[0,0].set_ylabel('Amplitude [dB]')

ax[0,0].fill([f_stop1, 0 ,  0,   f_stop1], [-alpha_min+5, -alpha_min+5, 0, 0], '0.9', lw=0) # stop
ax[0,0].fill([f_paso2,  f_paso1,  f_paso1,   f_paso2], [-60, -60, -alpha_max+5, -alpha_max+5], '0.9', lw=0) # stop
ax[0,0].fill([f_stop2,  100,  100,   f_stop2], [-alpha_min+5, -alpha_min+5, -alpha_max+15, -alpha_max+15], '0.9', lw=0) # stop
ax[0,0].grid(which='both', axis='both')
ax[0,0].set_facecolor([204/255,230/255,204/255]) 

ax[0,1].plot(f,np.angle(H))
ax[0,1].set_xlim([0,100])
ax[0,1].set_xlabel('Frequency [Hz]')
ax[0,1].set_ylabel(r"$\angle [rad]$")
ax[0,1].grid(which='both', axis='both')



#tau = np.diff(np.angle(H)/(f[1]-f[0]))
f_tau,tau = sig.group_delay((b,1),f,fs=fs)
ax[1,0].plot(f_tau,tau)
ax[1,0].set_xlim([0,100])
ax[1,0].set_xlabel('Frequency [Hz]')
ax[1,0].set_ylabel(r"$\tau [rad]$")
ax[1,0].set_ylim([1500,1800])
ax[1,0].grid(which='both', axis='both')

ax[1,1].plot(range(0,len(b)),b)
ax[1,1].grid(which='both', axis='both')

##FIltrado señal 

mat_struct = sio.loadmat('ecg.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
N0 = len(ecg_one_lead)

signal  = sig.filtfilt(b, 1, ecg_one_lead)

fig,ax = plt.subplots(1,1,figsize=(10,5))

t = np.linspace(0,N0/fs,N0)
ax.plot(t,signal,label='ECG Filtrado')
ax.plot(t,ecg_one_lead,label='ECG')
ax.legend()


plt.show()
