from tkinter import *
from temperature.statistics import Statistics

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        master.title('Temperature Statistics')
        Statistics()

root = Tk()
app=Application(root)
app.mainloop()
