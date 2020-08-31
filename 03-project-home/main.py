from tkinter import *
from classes.taps import Taps

app = Tk()

app.title('Home')
app.configure(background='DimGray')
app.geometry('600x600')
app.resizable(width=False, height=False)

taps = Taps(app)

frame1 = taps.addFrame('test 1')
frame2 = taps.addFrame('test 2')

content = Label(frame1, text = 'test 1 content')
content.grid(column = 0, row = 0, padx = 30, pady = 30)

content2 = Label(frame2, text = 'test 2 content')
content2.grid(column = 0, row = 0, padx = 30, pady = 30)

app.mainloop()
