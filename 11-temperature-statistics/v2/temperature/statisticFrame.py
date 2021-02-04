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
        
        # Date from calendar
        self.dateFromSelect = DateEntry(self, selectmode = 'day', date_pattern = 'dd.mm.y')
        self.dateFromSelect.set_date(self.firstDayOfMonth(now))
        self.dateFromSelect.bind("<<DateEntrySelected>>", self.updateStatistic)  
        self.dateFromSelect.pack()
        
        # Date to calendar
        self.dateToSelect = DateEntry(self, selectmode = 'day', date_pattern = 'dd.mm.y')
        self.dateToSelect.set_date(self.lastDayOfMonth(now))
        self.dateToSelect.bind("<<DateEntrySelected>>", self.updateStatistic)  
        self.dateToSelect.pack()
        
        # Update statistic
        self.updateStatistic()
    
    def updateStatistic(self, *args):
        StatisticPrint(self, self.stationSelect.get(), self.dateFromSelect.get_date(), self.dateToSelect.get_date(), self.statisticTypeSelect.get())
 
    def firstDayOfMonth(self, d):
        return d.replace(day = 1, hour = 0, minute = 0, second = 0, microsecond = 0)
    
    def lastDayOfMonth(self, d):
        if d.month == 12:
            return d.replace(day = 31)
        return d.replace(month = d.month + 1, day = 1) - timedelta(days = 1)