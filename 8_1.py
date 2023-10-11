import time
from scipy.fftpack import fft
import adi
import matplotlib.pyplot as plt
import numpy as np


# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2437000000

# Collect data
for r in range(10):
    rx = sdr.rx()
    plt.clf()
    #plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)
    print(rx.real)
    print(rx.imag)
    N=2048 # количество точек ДПФ
    X = fft(rx.real, N)/N
    X1 = fft(rx.imag, N)/N
    print(X)
    print("###################################")
    print(X1)
    plt.figure(777)
    plt.plot(X1)
#plt.figu
plt.show()

#N=256 # количество точек ДПФ
#X = fft(rx.real,N)/N
#print(X)
#plt.figure(2)
#k = np.arange(0, N)
#plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
#plt.xlabel('k')
#plt.ylabel('$x[k]$') 
