#!/usr/bin/env python3

import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib, GObject
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import re
import json
import asyncio
import websockets
import threading
import textwrap
from display import Display


class AudioProcessor(object):

    def __init__(self):
        self.pipeline = Gst.parse_launch("autoaudiosrc ! level post-messages=true ! audio/x-raw,format=S16LE,channels=1,rate=16000 ! audioconvert ! audiorate ! appsink name=sink emit-signals=True")
        sink = self.pipeline.get_by_name("sink")
        sink.connect("new-sample", self.on_new_sample)
        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message::element', self.on_message)
        self.load_model()
        self.lines = [""]
        self.display = Display()
        self.rms = 0

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
            text = re.sub(r'(\b)i(\b)', '\1I\2', text)
            self.lines[-1] = text
            self.display.show_text(" ".join(self.lines))
            if final:
                self.lines.append("")
                if len(self.lines) > 6:
                    self.lines.pop(0)
        return Gst.FlowReturn.OK

    def on_message(self, bus, message):
        s = message.get_structure()
        if s.get_name() == 'level':
            self.rms = s['rms'][-1]

    def websocket_worker(self):
        async def text_handler(ws, path):
            while True:
                text = " ".join(self.lines)
                lines = textwrap.wrap(text, 16)
                text = " ".join(lines[-5:])
                await ws.send(text)
                await asyncio.sleep(0.3)

        async def rms_handler(ws, path):
            while True:
                await ws.send(str(self.rms))
                await asyncio.sleep(0.3)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        text_server = websockets.serve(text_handler, "localhost", 31130)
        loop.run_until_complete(text_server)
        rms_server = websockets.serve(rms_handler, "localhost", 31131)
        loop.run_until_complete(rms_server)
        loop.run_forever()


if __name__ == "__main__":
    Gst.init(None)
    ap = AudioProcessor()
    ap.start()
    threading.Thread(target=ap.websocket_worker, daemon=True).start()
    loop = GLib.MainLoop()
    loop.run()
