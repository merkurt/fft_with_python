import numpy as np

def signalGenerator(sampleRate, cosHz, sinHz):
    """
    timeVector, finalSignalWoNoise, finalSignal = signalGenerator(sampleRate, cosHz, sinHz)
    """
    Fs = sampleRate   # sample rate
    timeVector = np.arange(0, 1 - (1/Fs), (1/Fs))   # time vector   
    signal1 = np.cos(2 * np.pi * cosHz * timeVector)  # 100 Hz cos signal
    signal2 = np.sin(2 * np.pi * sinHz * timeVector)  # 150 Hz sin signal
    noise = np.random.randn(timeVector.shape[0])  # some noise
    finalSignalWoNoise = signal1 + signal2  # final signal without noise
    finalSignal = finalSignalWoNoise + noise    # final signal with noise
    return timeVector, finalSignalWoNoise, finalSignal


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    tVector, fSignalWoNoise, fSignal = signalGenerator(1000, 100, 150)

    plt.plot(tVector, fSignal)
    plt.legend('show')
    plt.show()
