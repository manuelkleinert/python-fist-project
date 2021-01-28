import sqlite3
import os.path
import datetime
from collections import namedtuple

class Db:
    '''
    DB Class to save temperature
    '''
    
    def __init__(self):
        # Open DB connect
        self.fullPath = os.path.dirname(os.path.abspath(__file__))+"/temperature.db"
        self.createTable()
    
    def openConnection(self):
        self.connection = sqlite3.connect(self.fullPath, detect_types = sqlite3.PARSE_DECLTYPES)
        # self.connection.row_factory = sqlite3.Row
    
    def createTable(self):
        # Create Table if not exist
        self.openConnection()
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE 
                       IF NOT EXISTS 
                       temperatures(
                           id INTEGER PRIMARY KEY, 
                           date TIMESTAMP NOT NULL, 
                           temperature DECIMAL(5,2) NOT NULL)''')
        self.connection.commit()
        self.connection.close()
        
    def addTemperature(self, temperature, date = datetime.datetime.now()):
        # Add teperature to db
        self.openConnection()
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO 
                       temperatures(date,temperature) 
                       VALUES(?,?)''', (date, temperature))
        self.connection.commit()
        self.connection.close()
        return True
    
    def getData(self, dateFrom = datetime.datetime.today(), dateTo = datetime.datetime.today()):
        # Get termperatres from db
        
        temperatureData = []
                
        self.openConnection()
        cursor = self.connection.cursor()
        cursor.execute('''SELECT 
                       id, 
                       date, 
                       temperature
                       FROM temperatures 
                       WHERE date >= ? AND date <= ? ORDER BY date ASC''', 
                       (dateFrom, dateTo))
        tempRequest = cursor.fetchall()
        
        for temperature in tempRequest:
            temperatureData.append(dict(zip([c[0] for c in cursor.description], temperature)))
            
            # tempData = dict(zip([c[0] for c in cursor.description], temperature))
            # date = tempData['date']
            
            # print(tempData)
            
            # if date.year not in temperatureData:
            #     temperatureData[date.year] = {date.month:{}}
                
            #     if date.month not in temperatureData[date.year]:
            #         temperatureData[date.year][date.month] = {date.year:{}}
                
            #         if date.day not in temperatureData[date.year][date.month]:
            #             temperatureData[date.year][date.month][date.day] = []
            
            # temperatureData[date.year][date.month][date.day].append(tempData)
           
            # tempDate = tempData['date']
            
            # if temperatureData[tempDate.day] != []
            #     temperatureData[tempDate.day] = []
            
            # print(type(temperatureData[tempDate.day]))
            
            # temperatureData
            #     temperatureData[tempDate.day] = []
            #     print('ini')
            
            # temperatureData[tempDate.day].append(tempData)
        print(temperatureData)
            
        cursor = self.connection.cursor()
        cursor.execute('''SELECT 
                       MIN(temperature) AS min, 
                       MAX(temperature) AS max 
                       FROM temperatures 
                       WHERE date >= ? AND date <= ? ORDER BY date ASC''', 
                       (dateFrom, dateTo))
        minMaxRequest = cursor.fetchone()
        self.connection.close()
        
        DataCollection = namedtuple('DataCollection', 'temperatures minTemp maxTemp dateFrom dateTo')
        
        return DataCollection(
            temperatureData,
            minMaxRequest[0],
            minMaxRequest[1],
            dateFrom,
            dateTo)
