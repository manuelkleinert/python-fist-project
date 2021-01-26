from .db import Db
from tkinter import Canvas
from datetime import datetime


class Statistics(Canvas):
    def __init__(self, master, dateFrom = datetime.today(), dateTo = datetime.today()):
        Canvas.__init__(self, master)
        
        self.width = 200
        self.height = 100
        self.pack()

        self.db = Db()
        
        print(self.db.getTemperatures(dateFrom, dateTo))
        
        self.printStatistic()
        
    def printStatistic(self):
        self.create_rectangle(50, 20, 150, 80, fill="#476042")
        self.create_rectangle(65, 35, 135, 65, fill="yellow")
        self.create_line(0, 0, 50, 20, fill="#476042", width=3)
        self.create_line(0, 100, 50, 80, fill="#476042", width=3)
        self.create_line(150,20, 200, 0, fill="#476042", width=3)
        self.create_line(150, 80, 200, 100, fill="#476042", width=3)