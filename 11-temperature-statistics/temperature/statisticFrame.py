from .db import Db
from tkinter import Frame
from helper.form import Select
from .statisticPrint import StatisticPrint
from datetime import datetime

class StatisticFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        
        # Db
        db = Db()
        now = datetime.now()
        dateTimeStart = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        dateTimeEnd = now.replace(day=31, hour=23, minute=59, second=59)
        
        # Station selectbox
        stationOptions = {}
        for station in db.getStations():
            stationOptions[station.name] = station.id
        stationSelect = Select(self, 'Station:',stationOptions)
           
        
        # Type selectbox
        statisticTypeSelect = Select(self, 'Type:', {'Day':'day', 'Month':'month', 'Year':'year'})
        
        statisticPrint = StatisticPrint(self, stationSelect.get(), dateTimeStart, dateTimeEnd, statisticTypeSelect.get())
        
        # Update statistic
        statisticTypeSelect.setEvent(lambda *args: statisticPrint.set(stationSelect.get(), dateTimeStart, dateTimeEnd, statisticTypeSelect.get()))