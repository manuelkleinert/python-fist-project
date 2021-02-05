try:
    from .db import Db
    from tkinter import Frame, messagebox
    from helper.form import Select
    from datetime import datetime, timedelta
    from .statisticPrint import StatisticPrint
    from tkcalendar import DateEntry
except ModuleNotFoundError as err:
    messagebox.showwarning(title = 'Module not installed or found', message = err)

class StatisticFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        
        # Db
        db = Db()
        
        # Datetime now
        now = datetime.now()
        
        # Station selectbox
        stationOptions = {}
        for station in db.getStations():
            stationOptions[station.name] = station.id
        self.stationSelect = Select(self, 'Station:', stationOptions)
        self.stationSelect.setEvent(self.updateStatistic)
           
        # Type selectbox
        self.statisticTypeSelect = Select(self, 'Type:', {'Day':'D', 'Month':'m', 'Year':'Y'})
        self.statisticTypeSelect.setEvent(self.updateStatistic)
        self.statisticTypeSelect.setValue('Day')
        
        # Date from calendar (7 Days before now)
        self.dateFromSelect = DateEntry(self, selectmode = 'day', date_pattern = 'dd.mm.y')
        self.dateFromSelect.set_date((now - timedelta(days=7)))
        self.dateFromSelect.bind("<<DateEntrySelected>>", self.updateStatistic)  
        self.dateFromSelect.pack()
        
        # Date to calendar
        self.dateToSelect = DateEntry(self, selectmode = 'day', date_pattern = 'dd.mm.y')
        self.dateToSelect.set_date(now)
        self.dateToSelect.bind("<<DateEntrySelected>>", self.updateStatistic)  
        self.dateToSelect.pack()
        
        # Statistic
        self.statistic = StatisticPrint(self, self.stationSelect.get(), self.dateFromSelect.get_date(), self.dateToSelect.get_date(), self.statisticTypeSelect.get())
        
    def updateStatistic(self, *args):
        self.statistic.set(self.stationSelect.get(), self.dateFromSelect.get_date(), self.dateToSelect.get_date(), self.statisticTypeSelect.get())