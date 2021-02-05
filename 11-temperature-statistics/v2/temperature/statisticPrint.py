try:
    import tkinter
    import numpy as np
    from .db import Db
    from datetime import datetime
    from tkinter import messagebox
    from collections import namedtuple
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
except ModuleNotFoundError as err:
    
    messagebox.showwarning(title = 'Module not installed or found', message = err)

class StatisticPrint():
    '''
    Statistic print canvas class
    '''
    
    def __init__(self, master, stationId, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'D'):
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
            Set display type (D,m,Y)
        '''
        
        # Db
        self.db = Db()

        # Canvas element
        fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(fig, master)
        
        # Print matplotlib statistic to canvas
        self.canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
        
        # Print first statistic
        self.set(stationId, dateFrom, dateTo, statisticType)
    
    def set(self, stationId, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'D'):
        self.stationId = stationId
        self.statisticType = statisticType
        self.data = self.db.getData(stationId, dateFrom, dateTo, statisticType)
        
        # Clear statistic
        self.ax.clear()
        
        # Set label left
        self.ax.set_ylabel('temperature')
    
        # Set min max date
        datemin = np.datetime64(dateFrom, statisticType)
        datemax = np.datetime64(dateTo, statisticType)
        self.ax.set_xlim(datemin, datemax)
        
        # Enable grid
        self.ax.grid(True)
        
        # Set horizontal grid and labels
        years = mdates.YearLocator()    # every year
        months = mdates.MonthLocator()  # every month
        days = mdates.DayLocator()      # every days
        hours = mdates.HourLocator()    # every hours
        
        if self.statisticType == 'Y':
            # format the ticks year
            self.ax.xaxis.set_major_locator(years)
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
            self.ax.xaxis.set_minor_locator(months)
            self.ax.set_xlabel('Date Years')
        elif self.statisticType == 'm':
            # format the ticks month
            self.ax.xaxis.set_major_locator(months)
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))
            self.ax.xaxis.set_minor_locator(months)
            self.ax.set_xlabel('Date Months')
        else:
            # format the ticks day
            self.ax.xaxis.set_major_locator(days)
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
            self.ax.xaxis.set_minor_locator(hours)
            self.ax.set_xlabel('Date Days')
        
        # Print Temperatures
        if self.data:
            dateArray = []
            tempArray = []
            for key, tempList in self.data.temperatures.items():
                if tempList:
                    for temp in tempList:
                        dateArray.append(temp.date)
                        tempArray.append(temp.temperature)
                        
            self.ax.plot(dateArray, tempArray)
        
        self.canvas.draw()
        self.ax.clear()