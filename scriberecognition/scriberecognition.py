#!/usr/bin/env python3

import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib, GObject
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import re
import queue
import json


class AudioProcessor(object):

    def __init__(self):
        self.pipeline = Gst.parse_launch("autoaudiosrc ! audio/x-raw,format=S16LE,channels=1,rate=16000 ! audioconvert ! audiorate ! appsink name=sink emit-signals=True")
        sink = self.pipeline.get_by_name("sink")
        sink.connect("new-sample", self.on_new_sample)
        self.load_model()

    def load_model(self, text="", language="en-us"):
        words = str(re.split("[.,;!?\-\n]", text.lower())).replace(" '", " \"").replace("',", "\",").replace("['", "[\"").replace("']", "\"]")
        model = Model(lang=language)
        if words != '[""]':
            self.rec = KaldiRecognizer(model, 16000, words)
        else:
            print("Unconstrained")
            self.rec = KaldiRecognizer(model, 16000)

    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)

    def pause(self):
        self.pipeline.set_state(Gst.State.PAUSED)

    def stop(self):
        self.pipeline.set_state(Gst.State.STOPPED)

    def on_new_sample(self, sink):
        sample = sink.emit("pull-sample")
        buf = sample.get_buffer()
        success, map_info = buf.map(Gst.MapFlags.READ)
        final = False
        if self.rec.AcceptWaveform(map_info.data):
            text = json.loads(self.rec.Result())['text']
            final = True
        else:
            text = json.loads(self.rec.PartialResult())['partial']
        if len(text) > 0:
            print(text)
        return Gst.FlowReturn.OK


if __name__ == "__main__":
    Gst.init(None)
    ap = AudioProcessor()
    ap.start()
    loop = GLib.MainLoop()
    loop.run()
