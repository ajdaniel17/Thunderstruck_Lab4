#import RPi.GPIO as GPIO
from time import sleep
import threading
import numpy as np

from Lookuptable import Note_Frequencies

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

class Music_Driver (threading.Thread):
    port = 0
    BPM = 0

    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port = port
        #NOTE: ALL VALUES IN ARRAY ARE ALL STRINGS, TYPE CONVERT WHEN NEEDED
        self.Note_Frequencies = np.load('Note_Frequencies.npy')
        # GPIO.setup(self.port,GPIO.OUT)

    def setBPM(self,BPM):
        self.BPM = BPM

    def getBPM(self):
        return self.BPM

    

Test = Music_Driver(2)



