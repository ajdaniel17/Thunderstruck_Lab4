import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

data = read('hi.wav')
thing = np.array(data[0],dtype=float)
data_fft = np.fft.fft(thing)
plt.plot(np.abs(data_fft))
plt.show()