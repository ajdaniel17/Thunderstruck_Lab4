from mido import MidiFile
import numpy as np
import time
import pysine as py
import threading

midi_file = MidiFile("MIDI/Married_Life.mid",clip = True)
# for track in midi_file.tracks:
#     print(track)
Note_Frequencies = np.load('Note_Frequencies.npy')
row ,col = Note_Frequencies.shape

for msg in midi_file:
    
    print(msg) 
    if msg.type == 'note_off':
        # print("playing note", FRQ , "for", msg.time)
      
        py.sine(FRQ,msg.time)
        
    elif msg.type == 'note_on':
        for i in range(row):
            # print("Off Time",msg.time)
            if msg.note == int(Note_Frequencies[i][1]):
                FRQ = float(Note_Frequencies[i][2])
                break
        py.sine(0,msg.time)
    
        
    
        