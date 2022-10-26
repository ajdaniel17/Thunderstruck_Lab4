import FFT_Driver as FD
import Music_Recording_Driver as MRD
import pysine as py
from scipy.io.wavfile import read
from time import sleep


FFT_Driver = FD.FFT_Driver()
Music_Driver = MRD.Music_Recording_Driver()
Music_Driver.setStream(1)
State = 1
filename = "bit8w.wav"
sr , d = read(filename)
print(sr)
#44100
start = 0
end = 4410
incriment = 4410
d0 = d[:, 0] 
print(f"number of channels = {d0.shape}")
print(d0.shape)
while True:
    # Music_Driver.Record()
    FRQ = FFT_Driver.FFT(sr,d0[start:end])
    py.sine(FRQ,.1)
    start += incriment
    end += incriment
    # sleep(.01)

    # if State == 1:
    #     Music_Driver.Record()
    #     State = 2
    #     sleep(.001)
    #     # print("Recording")
    # elif State == 2 and not Music_Driver.getState():
    #     sr , d = read(filename)
    #     FRQ = FFT_Driver.FFT(sr,d)
    #     # print("Do the FFT")
    #     State = 3
    #     sleep(.001)
    # elif State == 3 and not FFT_Driver.getState():
    #     # print("Play the FRQ")
    #     py.sine(FRQ,.2)
    #     sleep(.2)
    #     FRQ = 0
    #     State = 1
        