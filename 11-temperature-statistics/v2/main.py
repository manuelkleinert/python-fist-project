from tkinter import Tk, Frame, Label
from helper.taps import Taps
from temperature.db import Db
from temperature.statisticFrame import StatisticFrame

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        
        master.title('Temperature Statistics')
        
        # Tutorial Add a new Temperature
        self.db = Db()
        
        # self.db.addStation('Garten')
        # self.db.addTemperature(1, 21.88657)
        
        tabs = Taps(self)
        
        tabs.addTap('Temperature Statistics', StatisticFrame())
        
        tapHome = tabs.addTap('Home Controlls')
        homeText = Label(tapHome, text="Home Content")
        homeText.pack()


app = Application(Tk())
app.mainloop()
