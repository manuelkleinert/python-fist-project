# -*- coding: utf-8 -*-
from tkinter import *

app = Tk()

app.title('Home')
app.configure(background='DimGray')
app.geometry('600x600')
app.resizable(width=False, height=False)

taps = Taps(app)
