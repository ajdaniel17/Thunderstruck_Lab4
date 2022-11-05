import Music_Driver as MD
from mido import MidiFile
import numpy as np
from time import sleep
import atexit



Coil = MD.Music_Driver()
def kill_sounds():
    Coil.kill()
atexit.register(kill_sounds)
midi_file = MidiFile("MIDI/Married_Life.mid",clip = True)

Note_Frequencies = np.load('Note_Frequencies.npy')
row ,col = Note_Frequencies.shape
FRQ = 500


for msg in midi_file:
    print(msg) 
    if msg.type == 'note_off':
        # print("playing note", FRQ , "for", msg.time)
        Coil.playMidiNote(FRQ,msg.time)
        
    elif msg.type == 'note_on':
        for i in range(row):
            # print("Off Time",msg.time)
            if msg.note == int(Note_Frequencies[i][1]):
                FRQ = float(Note_Frequencies[i][2])
                break
        sleep(msg.time)
    
