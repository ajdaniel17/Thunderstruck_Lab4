import pysine as py
from time import sleep
import threading


class soundplayer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def playsound(self,time,FRQ):
        py.sine(FRQ,time)

test = soundplayer()

test.playsound(5,1000)
sleep(2)
test.playsound(0,1000)

