import FFT_Driver as FD
import Music_Recording_Driver as MRD
import pysine as py
from scipy.io.wavfile import read
from time import sleep


FFT_Driver = FD.FFT_Driver()
Music_Driver = MRD.Music_Recording_Driver()
Music_Driver.setStream(2)
State = 1
filename = "output.wav"
while True:
    if State == 1:
        Music_Driver.Record()
        State = 2
        print("Recording")
    elif State == 2 and not Music_Driver.getState():
        sr , d = read(filename)
        FRQ = FFT_Driver.FFT(sr,d)
        print("Do the FFT")
        State = 3
    elif State == 3 and not FFT_Driver.getState():
        print("Play the FRQ")
        py.sine(FRQ,.1)
        sleep(.1)
        State = 1
        