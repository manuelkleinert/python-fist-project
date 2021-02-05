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
        
        # Template add new Station
        # self.db.addStation('Garten')
        
        # Template add temperature
        # self.db.addTemperature(1, 28.88657)
        
        # Create new Tapbar
        tabs = Taps(self)
        
        # Add home Tap
        tapHome = tabs.addTap('Home Controlls')
        homeText = Label(tapHome, text="Home Content")
        homeText.pack()
        
        # Add Temperature Tap
        tabs.addTap('Temperature Statistics', StatisticFrame())

app = Application(Tk())
app.mainloop()
