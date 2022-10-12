#import RPi.GPIO as GPIO
from time import sleep
import threading
import numpy as np
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

class Music_Driver (threading.Thread):
    port = 0
    BPM = 120
    EigenDuration = 1.0/141000.0
    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port = port
        #NOTE: ALL VALUES IN ARRAY ARE ALL STRINGS, TYPE CONVERT WHEN NEEDED
        self.Note_Frequencies = np.load('Note_Frequencies.npy')
        self.row ,self.col = self.Note_Frequencies.shape
        # GPIO.setup(self.port,GPIO.OUT)
        # GPIO.output(self.port,GPIO.LOW)

    def playNote(self,Note,timing):
        Duration = self.getDuration(timing)
        for i in range(self.row):
            if self.Note_Frequencies[i][0] == Note:
                FRQ = self.Note_Frequencies[i][1]
                break
        NoteCycleDuration = 1.0 / FRQ
        NoteStart = time.time()
        NoteCycle = True
        EigenCycle = True
        
        while ((time.time() - NoteStart) < Duration):
            NoteCycletime = time.time()
            while ((time.time() - NoteCycletime) < NoteCycleDuration):
                if(NoteCycle):
                    print("HIGH")
                    # EigenStart = time.time()
                    # while((time.time() - EigenStart) < self.EigenDuration):
                    #     if(EigenCycle):
                    #         # GPIO.output(self.port,GPIO.HIGH)
                    #         print("HIGH")
                    #     else:
                    #         # GPIO.output(self.port,GPIO.LOW)
                    #         print("LOW")
                    # EigenCycle = not EigenCycle
                else:
                    print("LOW")
                    # GPIO.output(self.port,GPIO.LOW)
            NoteCycle = not NoteCycle








    def getDuration(self,timing):
        if(timing == 1): #Half Note
            return 120.0/self.BPM
        elif(timing == 2): #Quarter Note
            return 60.0/self.BPM
        elif(timing == 3): #Eighth Note
            return 30.0/self.BPM
        elif(timing == 4): #Sixteenth Note
            return 15.0/self.BPM
        elif(timing == 5): #Dotted-quarter Note
            return 90.0/self.BPM
        elif(timing == 6): #Dotted-eighth Note
            return 45.0/self.BPM
        elif(timing == 7): #Dotted-sixteenth Note
            return 22.5/self.BPM
        elif(timing == 8): #Triplet-quarter Note
            return 40.0/self.BPM
        elif(timing == 9): #Triplet-eighth Note
            return 20.0/self.BPM
        elif(timing == 10): #Triplet-sixteenth Note
            return 10.0/self.BPM


    def setBPM(self,BPM):
        self.BPM = BPM

    def getBPM(self):
        return self.BPM

    def setFRQ(self,FRQ):
        self.EigenFrq = FRQ

    def getFRQ(self):
        return self.EigenFrq



Test = Music_Driver(2)
Test.playNote("C1",1)



