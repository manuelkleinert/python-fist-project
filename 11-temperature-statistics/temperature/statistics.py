from .db import Db
from tkinter import Canvas
from datetime import datetime


class Statistics(Canvas):
    '''
    Statistic print canvas class
    '''
    
    def __init__(self, master, dateFrom = datetime.today(), dateTo = datetime.today()):
        '''
        Parameters
        ----------
        master : frame
            Frame where the canvas set
        dateFrom : datetime
            Statistic start date
        dateTo : datetime
            Statistic end date
        '''
        self.width = 1000
        self.height = 800
        
        Canvas.__init__(self, master, width=self.width, height=self.height)
        
        self.width = 1000
        self.height = 800
        self.border = 50
        
        self.statisticWidth = self.width - self.border
        self.statisticHeight = self.height - self.border
        
        self.pack(expand=1)

        self.db = Db()
        self.data = self.db.getTemperatures(dateFrom, dateTo)
        
        self.printStatistic()
        
    def printStatistic(self):
        # Start print staic method
        self.printRaster()
        self.printBorder()
        
    def printBorder(self):
        # Print statistic border method
        
        borderColor = '#666666'
        
        self.create_line(self.border, self.border, self.statisticWidth, self.border, fill=borderColor, width=3)
        self.create_line(self.border, self.border, self.border, self.statisticHeight, fill=borderColor, width=3)
        
        self.create_line(self.border, self.statisticHeight, self.statisticWidth, self.statisticHeight, fill=borderColor, width=3)
        self.create_line(self.statisticWidth, self.border, self.statisticWidth, self.statisticHeight, fill=borderColor, width=3)
        
    def printRaster(self):
        # Print raster method
        
        rasterColor = '#CCCCCC'
        textColor = '#666666'
        rasterWidth = 1
        rasterVertical = 24
        rasterHorizontal = 10
    
        # Vertical lines
        countVertical = (self.statisticWidth - self.border)  / rasterVertical
        for i in range(1, rasterVertical):
            self.create_line(self.border + (countVertical*i), self.border, self.border + (countVertical*i), self.statisticHeight, fill=rasterColor, width=rasterWidth)
            self.create_text(self.border + (countVertical*i), self.statisticHeight + self.border/2 , text=str(i), fill=textColor)
            
        # Horizontal
        countHorizontal = (self.statisticHeight - self.border) / rasterHorizontal
        for i in range(1, rasterHorizontal):
            self.create_line(self.border, self.border + (countHorizontal*i), self.statisticWidth, self.border + (countHorizontal*i), fill=rasterColor, width=rasterWidth)
            self.create_text(self.border / 2, self.border + (countHorizontal*i) , text=str(i), fill=textColor)
        