# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3,8,0):
    print('You need python 3.8 or later to run this script')
    print(sys.version + ' > 3')
    exit(1)

from tkinter import *
from helper.taps import Taps
from helper.config import Config

class main:
    def __init__(self):
        config = Config(__file__)
        self.data = config.get()
        self.app = Tk()

        self.setWindow()
        self.setTaps()
        self.app.mainloop()

    def setWindow(self):
        self.app.title('Home')
        self.app.configure(background='DimGray')
        self.app.geometry('600x600')
        self.app.resizable(width=False, height=False)


    def setTaps(self):
        self.taps = Taps(self.app)

        for floor in self.data['floors']:
            frame = self.taps.addFrame(floor['tag'])
            content = Label(frame, text = 'Test Content ' + floor['title'])
            content.grid(column = 0, row = 0, padx = 30, pady = 30)

main()
