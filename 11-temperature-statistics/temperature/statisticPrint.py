from .db import Db
from tkinter import Canvas
from datetime import datetime
from collections import namedtuple


class StatisticPrint(Canvas):
    '''
    Statistic print canvas class
    '''
    
    def __init__(self, master, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'day'):
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
        
        Canvas.__init__(self, master, width=self.width, height=self.height)
        
        # Db
        self.db = Db()
        
        # Statistic border
        Border = namedtuple('Border', 'top bottom left right')
        self.border = Border(5, 50, 50, 5)
        
        # Statistic coordinations
        Statistic = namedtuple('Statistic', 'top left right bottom height width')
        self.statistic = Statistic(
            self.border.top,
            self.border.left,
            self.width - self.border.right,
            self.height - self.border.bottom,
            self.height - self.border.top - self.border.bottom, 
            self.width - self.border.left - self.border.right)
        
        self.pack(expand=1)
        
        self.set(dateFrom, dateTo, statisticType)
    
    def set(self, dateFrom = datetime.today(), dateTo = datetime.today(), statisticType = 'day'):
        self.statisticType = statisticType
        self.data = self.db.getData(dateFrom, dateTo)
        
        if self.data:
            self.delete('all')
            self.printStatistic()
            self.printBorder()
        else:
            print('Temperatures DB is empty')
        
    def printBorder(self):
        # Print statistic border method
        
        borderColor = '#666666'
        
        self.create_polygon([
            self.statistic.left, self.statistic.top,
            self.statistic.right, self.statistic.top,
            self.statistic.right, self.statistic.bottom,
            self.statistic.left, self.statistic.bottom,
            self.statistic.left, self.statistic.top
            ], fill = '', outline = borderColor, width = 2)
        
    def printStatistic(self):
        # Print raster method

        rasterColor = '#CCCCCC'
        textColor = '#666666'
        rasterWidth = 1
        
        # Horizontal (Temperatures)
        horizontalIndex = 1
        horizontalSpacing = self.statistic.height / (self.getMaxTemp() - self.getMinTemp())
        
        for temp in range(self.getMaxTemp(), self.getMinTemp(), -1):
            self.create_line(self.statistic.left, 
                             self.statistic.top + (horizontalSpacing*horizontalIndex), 
                             self.statistic.right, 
                             self.statistic.top + (horizontalSpacing*horizontalIndex), 
                             fill = rasterColor, 
                             width = rasterWidth)
            
            self.create_text(self.border.left / 2, self.statistic.top + (horizontalSpacing*horizontalIndex) , text=str(temp), fill=textColor)
            
            horizontalIndex += 1
    
        # Vertical lines (Date)
        if self.statisticType == 'year':
            dateMin = 1
            dateMax = self.data.dateTo.day
        elif self.statisticType == 'month':
            dateMin = 1
            dateMax = 12
        else:
            dateMin = 1
            dateMax = 24
          
        verticalIndex = 1  
        verticalSpacing = self.statistic.width  / (dateMax - dateMin)
        
        for i in range(dateMin, dateMax + 1):
            if i+1 < dateMax:
                self.create_line(self.statistic.left + (verticalSpacing*verticalIndex), 
                                self.statistic.top, 
                                self.statistic.left + (verticalSpacing*verticalIndex), 
                                self.statistic.bottom, 
                                fill = rasterColor, 
                                width = rasterWidth)
            
            self.create_text(verticalSpacing*verticalIndex, self.statistic.bottom + self.border.bottom/2 , text=str(i), fill=textColor)
            verticalIndex += 1
        
    #     # Print Temperature line
    #     linePoints = [self.border, self.statisticHeight]
    
    #     for temp in self.data['temperatures']:
    #         linePoints += self.calcTempPosition(temp['temperature'])
        
    #     self.create_polygon(linePoints, outline='green', fill='yellow', width=3)
    #     print(linePoints)
        
    # def calcTempPosition(self, temperature):
    #     print(temperature)
    #     return [100,200]
    
    def getMinTemp(self):
        return round(self.data.minTemp) - 1
    
    def getMaxTemp(self):
        return round(self.data.maxTemp) + 1