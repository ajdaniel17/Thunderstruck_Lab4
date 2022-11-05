from rpi_hardware_pwm import HardwarePWM
from time import sleep
import threading
import numpy as np
import time


class Music_Driver (threading.Thread):

    BPM = 120
    SampleRate = 10
    #NOTE: for port, 0 is GPIO 18, 1 is GPIO 19. Also, they cant have different FRQ
    def __init__(self):
        threading.Thread.__init__(self)
   
        #NOTE: ALL VALUES IN ARRAY ARE ALL STRINGS, TYPE CONVERT WHEN NEEDED
        self.Note_Frequencies = np.load('Note_Frequencies.npy')
        self.row ,self.col = self.Note_Frequencies.shape
        self.pwm = HardwarePWM(pwm_channel=0, hz=100)
        self.pwm.start(10)


    def playNote(self,Note,timing):
        Duration = self.getDuration(timing)
        for i in range(self.row):
            if self.Note_Frequencies[i][0] == Note:
                FRQ = self.Note_Frequencies[i][2]
                break
        self.pwm.change_frequency(float(FRQ))
        self.pwm.change_duty_cycle(10)        
        sleep(Duration)
        self.pwm.change_duty_cycle(0) 

    def playFRQ(self,FRQ):
        Duration  = 1.0 / self.SampleRate
        self.pwm.change_frequency(FRQ)
        self.pwm.change_duty_cycle(10)        
        sleep(Duration)
        self.pwm.change_duty_cycle(0)    

    def playMidiNote(self,FRQ,Duration):
        self.pwm.change_frequency(float(FRQ))
        self.pwm.change_duty_cycle(10)        
        sleep(Duration)
        self.pwm.change_duty_cycle(0)  

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

    def kill(self):
        self.pwm.change_duty_cycle(0)

    def setBPM(self,BPM):
        self.BPM = BPM

    def getBPM(self):
        return self.BPM

    def setFRQ(self,FRQ):
        self.EigenFrq = FRQ

    def getFRQ(self):
        return self.EigenFrq

    def setSample(self,s):
        self.SampleRate = s

    def getSample(self):
        return self.SampleRate


# Test = Music_Driver()
# while True:
#     # Test.playNote("C1",1)
#     Test.playFRQ(500)
#     sleep(.5)



