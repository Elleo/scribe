#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import re
import sounddevice as sd
import queue

q = queue.Queue()
device_info = sd.query_devices(0, 'input')

def callback(indata, frames, time, status):
    if status:
        q.put(bytes(indata))

tf = open(sys.argv[2], "r")
text = tf.read()

words = str(re.split("[.,;!?\-\n]", text.lower())).replace(" '", " \"").replace("',", "\",").replace("['", "[\"").replace("']", "\"]")

model = Model(lang="en-us")

rec = KaldiRecognizer(model, 16000, words)

with sd.RawInputStream(samplerate=16000, blocksize = 8000, device=1, dtype='int16', channels=1, callback=callback):
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
