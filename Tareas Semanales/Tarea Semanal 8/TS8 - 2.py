import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
import zplane as zplane

## Filtro Media Movil 

##FIR Simetrico N PAR

num1 = np.array([1,1])
den1 = np.array([1,0,0])


wz, Hz1 = sig.freqz(num1)

plt.close('all')


fig,ax = plt.subplots(1,2,figsize=(10,5))
fig.suptitle('FIR Simetrico N Par', fontsize=16)


ax[0].plot(wz, np.abs(Hz1),label=r'$|H_z(e^{j \Omega})|$')

ax[0].legend()
ax[0].set_xlabel(r'$\Omega [rad]$')
ax[0].set_ylabel(r'$|H(\Omega)|$')    
ax[0].grid(True)


ax[1].plot(wz, np.angle(Hz1),label=r'$\angle H_z(e^{j \Omega})$')

ax[1].legend()
ax[1].set_xlabel('$\Omega [rad]$')
ax[1].set_ylabel(r'$\angle H(\Omega)$')    
ax[1].grid(True)

zplane.zplane(num1,den1)
##FIR Simetrico N IMPAR

num2 = np.array([1,1,1])
den2 = np.array([1,0,0])

wz, Hz2 = sig.freqz(num2, den2)




fig,ax = plt.subplots(1,2,figsize=(10,5))
fig.suptitle('FIR Simetrico N Impar', fontsize=16)


ax[0].plot(wz, np.abs(Hz2),label=r'$|H_z(e^{j \Omega})|$')

ax[0].legend()
ax[0].set_xlabel(r'$\Omega [rad]$')
ax[0].set_ylabel(r'$|H(\Omega)|$')    
ax[0].grid(True)



ax[1].plot(wz, np.angle(Hz2),label=r'$\angle H_z(e^{j \Omega})$')

ax[1].legend()
ax[1].set_xlabel('$\Omega [rad]$')
ax[1].set_ylabel(r'$\angle H(\Omega)$')    
ax[1].grid(True)


zplane.zplane(num2,den2)

## Eliminacion Ruido 50Hz
fs = 150

fig,ax = plt.subplots(figsize=(10,5))

fig.suptitle('Eliminacion Ruido 50Hz', fontsize=16)

ax.plot(wz*fs/(2*np.pi), np.abs(Hz2),label=r'$|H_z(e^{j \Omega})|$')

ax.legend()
ax.set_xlabel(r'$f [Hz]$')
ax.set_ylabel(r'$|H(f)|$')    
ax.grid(True)

## Filtro Diferenciador

##FIR Asimetrico N PAR

num1 = np.array([1,-1])
den1 = np.array([1,0,0])


wz, Hz1 = sig.freqz(num1)


fig,ax = plt.subplots(1,2,figsize=(10,5))
fig.suptitle('FIR Asimetrico N Par', fontsize=16)


ax[0].plot(wz, np.abs(Hz1),label=r'$|H_z(e^{j \Omega})|$')

ax[0].legend()
ax[0].set_xlabel(r'$\Omega [rad]$')
ax[0].set_ylabel(r'$|H(\Omega)|$')    
ax[0].grid(True)


ax[1].plot(wz, np.angle(Hz1),label=r'$\angle H_z(e^{j \Omega})$')

ax[1].legend()
ax[1].set_xlabel('$\Omega [rad]$')
ax[1].set_ylabel(r'$\angle H(\Omega)$')    
ax[1].grid(True)

zplane.zplane(num1,den1)
##FIR Asimetrico N IMPAR

num2 = np.array([1,0,-1])
den2 = np.array([1,0,0])

wz, Hz2 = sig.freqz(num2, den2)




fig,ax = plt.subplots(1,2,figsize=(10,5))
fig.suptitle('FIR Asimetrico N Impar', fontsize=16)


ax[0].plot(wz, np.abs(Hz2),label=r'$|H_z(e^{j \Omega})|$')

ax[0].legend()
ax[0].set_xlabel(r'$\Omega [rad]$')
ax[0].set_ylabel(r'$|H(\Omega)|$')    
ax[0].grid(True)



ax[1].plot(wz, np.angle(Hz2),label=r'$\angle H_z(e^{j \Omega})$')

ax[1].legend()
ax[1].set_xlabel('$\Omega [rad]$')
ax[1].set_ylabel(r'$\angle H(\Omega)$')    
ax[1].grid(True)


zplane.zplane(num2,den2)








