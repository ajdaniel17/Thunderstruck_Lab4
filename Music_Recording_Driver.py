import pyaudio
import wave
# import threading


class Music_Recording_Driver():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 0.1
    WAVE_OUTPUT_FILENAME = "output.wav"
    Recording = False
    def __init__(self):
        # threading.Thread.__init__(self)
        self.p = pyaudio.PyAudio()

    def getAudioIndex(self):
        for i in range(self.p.get_device_count()):
            print(self.p.get_device_info_by_index(i))

    def setStream(self,index):
        self.stream = self.p.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                input = True,
                input_device_index = index,
                frames_per_buffer = self.CHUNK)

    def closeStream(self):
        self.stream.close()

    def Record(self):
        self.Recording = True
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            frames.append(data)

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.Recording = False

    def getState(self):
        return self.Recording

# Test = Music_Recording_Driver()
# Test.getAudioIndex()
# Test.setStream(5)
# Test.Record()

    
