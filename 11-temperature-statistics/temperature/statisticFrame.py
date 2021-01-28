from tkinter import Frame
from helper.form import Select
from .statisticPrint import StatisticPrint
from datetime import datetime

class StatisticFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        
        now = datetime.now()
        dateTimeStart = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        dateTimeEnd = now.replace(day=31, hour=23, minute=59, second=59)
        
        statisticTypeSelect = Select(self, 'Type:', {'Day':'day', 'Month':'month', 'Year':'year'})
        
        statisticPrint = StatisticPrint(self, dateTimeStart, dateTimeEnd, statisticTypeSelect.get())
        
        # Update statistic
        statisticTypeSelect.setEvent(lambda *args: statisticPrint.set(dateTimeStart, dateTimeEnd, statisticTypeSelect.get()))