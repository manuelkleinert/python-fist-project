import tkinter
from .db import Db
import numpy as np
from datetime import datetime
from collections import namedtuple

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt

class StatisticPrint():
    '''
    Statistic print canvas class
    '''
    
    def __init__(self, master, stationId, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'month'):
        '''
        Parameters
        ----------
        master : frame
            Frame where the canvas set
        dateFrom : datetime
            Statistic start date
        dateTo : datetime
            Statistic end date
        statisticType : string
            Set display type (day,month,year)
        '''
        
        # Statistic size
        self.width = 1000
        self.height = 800
        
        # Db
        self.db = Db()
        
        years = mdates.YearLocator()    # every year
        months = mdates.MonthLocator()  # every month
        days = mdates.DayLocator()      # every days
        hours = mdates.HourLocator()    # every hours
        
        years_fmt = mdates.DateFormatter('%Y')
        months_fmt = mdates.DateFormatter('%m')
        days_fmt = mdates.DateFormatter('%m')

        fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(fig, master)
        
        self.set(stationId, dateFrom, dateTo, statisticType)
        
        self.ax.set_ylabel('temperature')
        
        if self.statisticType == 'Y':
            # format the ticks year
            self.ax.xaxis.set_major_locator(years)
            self.ax.xaxis.set_major_formatter(years_fmt)
            self.ax.xaxis.set_minor_locator(months)
            self.ax.set_xlabel('Date Years')
        elif self.statisticType == 'm':
            # format the ticks month
            self.ax.xaxis.set_major_locator(months)
            self.ax.xaxis.set_major_formatter(months_fmt)
            self.ax.xaxis.set_minor_locator(months)
            self.ax.set_xlabel('Date Months')
        else:
            # format the ticks day
            self.ax.xaxis.set_major_locator(days)
            self.ax.xaxis.set_major_formatter(days_fmt)
            self.ax.xaxis.set_minor_locator(hours)
            self.ax.set_xlabel('Date Days')


        # round to nearest date.
        datemin = np.datetime64(dateFrom, statisticType)
        datemax = np.datetime64(dateTo, statisticType)
        self.ax.set_xlim(datemin, datemax)

        # format the coords message box
        self.ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        self.ax.format_ydata = lambda x: '$%1.2f' % x  # format the temperature.
        
        self.ax.grid(True)

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate()
        
        # Print matplotlib statistic to canvas
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
        
        self.set(stationId, dateFrom, dateTo, statisticType)
    
    def set(self, stationId, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'day'):
        self.stationId = stationId
        self.statisticType = statisticType
        self.data = self.db.getData(stationId, dateFrom, dateTo, statisticType)
        
        dateArray = []
        tempArray = []
        for key, tempList in self.data.temperatures.items():
            if tempList:
                for temp in tempList:
                    dateArray.append(temp.date)
                    tempArray.append(temp.temperature)
                    
        self.line = self.ax.plot(dateArray, tempArray)
        
        # self.line.set_xdata(dateArray)
        # self.line.set_ydata(tempArray)
        
        self.canvas.draw()
        self.canvas.flush_events()
