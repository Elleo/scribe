#!/usr/bin/env python3
import textwrap
try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
    MATRIX_SUPPORTED = True
except:
    print("Warning: rgbmatrix module not found, only websocket output will be available.")
    MATRIX_SUPPORTED = False

class Display(object):

    def __init__(self, *args, **kwargs):
        if MATRIX_SUPPORTED:
            options = RGBMatrixOptions()
            options.hardware_mapping = "adafruit-hat"
            options.rows = 32
            options.cols = 64
            options.gpio_slowdown = 5
            options.brightness = 50
            self.matrix = RGBMatrix(options = options)
            self.font = graphics.Font()
            self.font.LoadFont("fonts/tom-thumb.bdf")
            self.color = graphics.Color(0, 0, 255)

    def show_text(self, text):
        if MATRIX_SUPPORTED:
            self.matrix.Clear()
            lines = textwrap.wrap(text, 16)
            line_num = 1
            for line in lines[-5:]:
                graphics.DrawText(self.matrix, self.font, 0, line_num * 6, self.color, line)
                line_num += 1


if __name__ == "__main__":
    d = Display()
    d.show_text("Hello, this is a test! Words should wrap automatically. :)")
    while True:
        pass
