from signal_generator import *
from scipy import fft
from numpy import arange
import matplotlib.pyplot as plt

sampleRate = 1000
tVector, signalWoNoise, signal = signalGenerator(sampleRate, 100, 200)

lengthSignal = signal.shape[0]
signalFFT = fft.fft(signal)
signalFFT = signalFFT[0:int(lengthSignal/2) + 1]
freq = arange(0, sampleRate / 2, sampleRate / lengthSignal)

plt.subplot(2, 1, 1)
plt.title('Sinyal')
plt.plot(tVector, signal)
plt.xlabel('Zaman (s)')

plt.subplot(2, 1, 2)
plt.title('Genlik Spektrumu')
plt.plot(freq, 2 * abs(signalFFT/ lengthSignal))
plt.xlabel('Frekans (Hz)')
plt.grid()
plt.show()