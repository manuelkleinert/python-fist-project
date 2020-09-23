from tkinter import *
from tkinter import ttk

class Taps:
    def __init__(self, app):
        self.app = app
        self.note = ttk.Notebook(app)
        self.note.pack(expand = 1, fill ="both")

    def addFrame(self, name = ''):
        frame = ttk.Frame(self.note)
        self.note.add(frame, text = name)
        self.note.pack(expand = 1, fill = 'both')
        return frame
