from scipy.io.wavfile import read
import numpy as np
import time 
import matplotlib.pyplot as plt
import scipy.io

start = time.time()
samplerate , data = read("output.wav")
print(f"number of channels = {data.shape}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(data)
print(samplerate)
Time_arary = np.arange(0, length, 1.0/samplerate)

data = np.array(data,dtype=float)
print(Time_arary)
print("Amount of time to load " , time.time()-start)
# print(thing)
plt.figure(1)
print(Time_arary.shape)
print(data.shape)
plt.plot(Time_arary,data, label="Left channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")


# start = time.time()
FFT = np.fft.fft(data)/len(data)
FFT = FFT[range(int(len(data)/2))] # Exclude sampling frequency




tpCount = len(data)
values = np.arange(int(tpCount/2))
timePeriod = tpCount/samplerate
frequencies = values/timePeriod
high = 0
for i in range(len(FFT)):
    if abs(FFT[i]) > high:
        high = frequencies[i]
print("Highest Freq: ", high)
# print("Amount of time to FFT " , time.time()-start)
plt.figure(2)
plt.plot(frequencies,abs(FFT))
plt.show()