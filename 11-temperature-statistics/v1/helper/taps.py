from tkinter import ttk
from tkinter.ttk import Notebook

class Taps(Notebook):
    '''
    Taps classe inherit tk notebook
    '''
    def __init__(self, *args):
        Notebook.__init__(self, *args)
        self.pack(expand = 1, fill ="both")

    def addTap(self, title, tapFrame = None):
        if not tapFrame:
            tapFrame = ttk.Frame(self)
            tapFrame.pack(side = 'left')
            
        self.add(tapFrame, text=title)
        return tapFrame