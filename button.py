from tkinter import *

class myButton:
    def __init__(self, window, name = '', x = 0, y = 0):
        self.window = window
        self.name = StringVar()
        self.setName(name)
        self.button = Button(window, textvariable = self.name)
        self.button.pack()
        self.setPosition(x, y)

    def getButton(self):
        return self.button

    def setName(self, name):
        self.name.set(name)

    def setPosition(self,x,y):
        self.button.place(x = x, y = y)
