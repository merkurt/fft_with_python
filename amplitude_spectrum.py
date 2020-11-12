from signal_generator import *
from numpy import arange, fft
import matplotlib.pyplot as plt

sampleRate = 1000
tVector, signalWoNoise, signal = signalGenerator(sampleRate, 100, 200)

lengthSignal = signal.shape[0]
signalFFT = fft.fft(signal)
signalFFT = signalFFT[0:int(lengthSignal/2) + 1]
freq = arange(0, sampleRate / 2, sampleRate / lengthSignal)

plt.subplot(2, 1, 1)
plt.title('Signal (cos:100Hz, sin:200Hz)')
plt.plot(tVector, signal)
plt.xlabel('Time')

plt.subplot(2, 1, 2)
plt.title('Amplitude spectrum')
plt.plot(freq, 2 * abs(signalFFT/ lengthSignal))
plt.xlabel('Frequency (Hz)')
plt.grid()
plt.show()