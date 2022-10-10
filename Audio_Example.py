import pyaudio
import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm

NumBar = 1000
BarWidth = 10
Data = np.arange(20,20000,BarWidth,dtype = int)


fig = plt.figure()
bars = plt.bar(Data, Data,width=BarWidth, facecolor='green', alpha=0.75)
plt.show()

#FUck this, doesnt matter right NOW
