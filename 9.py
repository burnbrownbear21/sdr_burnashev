import adi
import numpy as np
import matplotlib.pyplot as plt
import time

table_number = 21
sdr = adi.Pluto("ip:192.168.2.1")
fc = 2400000000 + 2000000 * table_number
sdr.rx_lo = fc
sdr.tx_lo = fc
sample_rate = 1e6
sdr.sample_rate = sample_rate

# t = np.arange(0, 1, 0.001)
# fm = 300000
# Am = 2**2
# sig = Am * np.sin(2 * np.pi * fm * t)

# sdr.tx_cyclic_buffer = True # Enable cyclic buffers
# tx = sdr.tx(sig)
# rx = sdr.rx()
# plt.plot(rx.real)
# plt.draw()

# Create a sinewave waveform
fc = 100000
ts = 1/float(sample_rate)
t = np.arange(0, fc*ts, ts)
i = np.sin(2*np.pi*t*fc) * 2**14
q = np.cos(2*np.pi*t*fc) * 2**14
samples = i + 1j*q

# Start the transmitter
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples)

rx = sdr.rx()
plt.plot(rx.real)
plt.show()