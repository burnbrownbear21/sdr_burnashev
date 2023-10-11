import numpy as np
import matplotlib.pyplot as plt
U = 1
tau = 1e-3

f = 2*np.pi/tau
f = np.linspace(-6/tau,6/tau,1000)
S = np.zeros(1000)
S[0] = U/tau
S = U*tau*(np.sin(2*np.pi*f*tau/2)/(2*np.pi*f*tau/2))
plt.figure(1)
nn = np.arange(0,10)
plt.plot(f*2*np.pi, S, label='linear')
plt.plot(f*2*np.pi, S*2, label='cubic')
plt.xlabel('Frequency, rad/s')
plt.ylabel('$S(j/omega)$')
plt.grid(axis = 'both')
plt.show()