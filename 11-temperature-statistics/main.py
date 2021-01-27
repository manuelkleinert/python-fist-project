from tkinter import *
from helper.taps import Taps
from datetime import datetime
from temperature.db import Db
from temperature.statistics import Statistics


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        
        master.title('Temperature Statistics')
        
        self.db = Db()
        self.db.addTemperature(21.5)
        
        self.tabs = Taps(master)
        tapHome = self.tabs.addTap('Home Controlls')
        tapTemperature = self.tabs.addTap('Temperature Statistics')
        
        now = datetime.now()
        dateTimeStart = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        dateTimeEnd = now.replace(day=31, hour=23, minute=59, second=59)
        
        Statistics(tapTemperature, dateTimeStart, dateTimeEnd)

root = Tk()
app=Application(root)
app.mainloop()
