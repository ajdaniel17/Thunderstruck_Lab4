import threading
import numpy as np
import time
from scipy.io.wavfile import read

class FFT_Driver(threading.Thread):
    State = False
    def __init__(self):
        threading.Thread.__init__(self)

    def FFT(self,samplerate,data):
        self.State = True
        length = data.shape[0] / samplerate
        # print(f"number of channels = {data.shape}")
        # print(f"length = {length}s")
        FFT = np.fft.fft(data)/len(data)
        FFT = FFT[range(int(len(data)/2))]
        tpCount = len(data)
        values = np.arange(int(tpCount/2))
        timePeriod = tpCount/samplerate
        frequencies = values/timePeriod
        high = 0
        for i in range(len(FFT)):
            if abs(FFT[i]) > high:
                high = frequencies[i]
        self.State = False
        print(high)
        return high
    
    def getState(self):
        return self.State

# sr , d = read("1.wav")
# Test = FFT_Driver()
# print(Test.FFT(sr,d))