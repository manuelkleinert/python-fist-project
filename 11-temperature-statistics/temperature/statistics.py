from .db import Db
import datetime

class Statistics:
    def __init__(self):
        self.db = Db()
        # self.db.addTemperature(21.8)
        
        print(self.db.getTemperatures(datetime.datetime(2021,1,15,0,0,0),datetime.datetime.today()))