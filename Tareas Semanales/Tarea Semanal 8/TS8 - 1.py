import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

#Armo LPF Butter con fo = 1KHz

wo = 2*np.pi *1e3
numS,denS = sig.butter(2, wo,btype='lowpass',analog = True)



# Aplico transformada bilineal
fs = 100e3

numZ,denZ = sig.bilinear(numS, denS,fs=fs)

wz, Hz = sig.freqz(numZ, denZ)

ws, Hs = sig.freqs(numS, denS, worN=fs*wz)

fig = plt.figure()
plt.close('all')
plt.title('LPF Fs= 100KHz')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hz).clip(1e-15)),
             label=r'$|H_z(e^{j \Omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('f[Hz]')
plt.ylabel(r'$|H(f)|_{dB}$')    
plt.grid(True)


#Baja fs a 10KHz

fs = 10e3

numZ,denZ = sig.bilinear(numS, denS,fs=fs)

wz, Hz = sig.freqz(numZ, denZ)

ws, Hs = sig.freqs(numS, denS, worN=fs*wz)

fig = plt.figure()
plt.title('LPF Fs= 10KHz')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hz).clip(1e-15)),
             label=r'$|H_z(e^{j \Omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('f[Hz]')
plt.ylabel(r'$|H(f)|_{dB}$')
plt.grid(True)


## Armo HPF con fo = 6KHz


wo = 2*np.pi *6e3
numS,denS = sig.butter(2, wo,btype='highpass',analog = True)



# Aplico transformada bilineal
fs = 100e3

numZ,denZ = sig.bilinear(numS, denS,fs=fs)

wz, Hz = sig.freqz(numZ, denZ)

ws, Hs = sig.freqs(numS, denS, worN=fs*wz)

fig = plt.figure()
plt.title('HPF Fs= 100KHz')

plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hz).clip(1e-15)),
             label=r'$|H_z(e^{j \Omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('f[Hz]')
plt.ylabel(r'$|H(f)|_{dB}$')    
plt.grid(True)


#Baja fs a 10KHz

fs = 10e3

numZ,denZ = sig.bilinear(numS, denS,fs=fs)

wz, Hz = sig.freqz(numZ, denZ)

ws, Hs = sig.freqs(numS, denS, worN=fs*wz)

fig = plt.figure()
plt.title('HPF Fs= 10KHz')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hz).clip(1e-15)),
             label=r'$|H_z(e^{j \Omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(Hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('f[Hz]')
plt.ylabel(r'$|H(f)|_{dB}$')
plt.grid(True)


