# import threading
import numpy as np
import time
from scipy.io.wavfile import read

class FFT_Driver():
    State = False
    def __init__(self):
        print("bingus")
        # threading.Thread.__init__(self)

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
            if abs(FFT[i]) > high: #and frequencies[i] > 600:
                high = frequencies[i]
                PowerHigh = abs(FFT[i])
        self.State = False
        print(high , PowerHigh)
        if PowerHigh < 400:
            high = 0
        return high
    
    def getState(self):
        return self.State

# sr , d = read("1.wav")
# Test = FFT_Driver()
# print(Test.FFT(sr,d))