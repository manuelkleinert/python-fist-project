import sqlite3
import datetime
from tkinter import messagebox
from os.path import dirname, isfile, getsize, abspath
from collections import namedtuple, OrderedDict

class Db:
    '''
    DB Class to save and load temperature data
    '''
    def __init__(self):
        # DB path and name
        self.fullPath = dirname(abspath(__file__)) + "/temperature.db"
        
        # Create Table
        self.createTables()
    
    def openConnection(self):
        # Open DB connection and return cursor
        self.connection = sqlite3.connect(self.fullPath, detect_types = sqlite3.PARSE_DECLTYPES)
        return self.connection.cursor()
        
    def createTables(self):
        # Create Table if not exist
        if isfile(self.fullPath) and not getsize(self.fullPath) < 100:
            return False
            
        cursor = self.openConnection()
        cursor.execute('''
            CREATE TABLE 
                IF NOT EXISTS 
                Stations(
                    id INTEGER NOT NULL,
                    name VARCHAR(255) NOT NULL UNIQUE,
                    comment TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
                )''')
        
        cursor.execute('''
            CREATE TABLE 
                IF NOT EXISTS 
                Temperatures(
                    id INTEGER NOT NULL,
                    stationId INTEGER NOT NULL, 
                    date TIMESTAMP NOT NULL, 
                    temperature DECIMAL(5,2) NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT),
                    FOREIGN KEY (stationId) REFERENCES Stations(id)
                )
        ''')
        self.connection.commit()
        self.connection.close()
        
        return True
    
    def addStation(self, stationName, comment = ''):
        # Add new Station to db
        try:
            cursor = self.openConnection()
            cursor.execute('''INSERT INTO Stations(name, comment) VALUES(?, ?)''', (stationName, comment))
            self.connection.commit()
            self.connection.close()
            return True
        except sqlite3.IntegrityError as err:
            messagebox.showerror(title = 'Add Station', message = str(err))
            return False
    
    def getStations(self):
        # Get all Stations
        StationsCollection = namedtuple('StationsCollection', 'id, name, comment')
        cursor = self.openConnection()
        cursor.execute('''SELECT id, name, comment FROM Stations''')
        stationsRequest = list(map(StationsCollection._make, cursor.fetchall()))
        self.connection.close()
        return stationsRequest
        
    def addTemperature(self, stationId, temperature, date = datetime.datetime.now()):
        # Add teperature to db
        try:
            cursor = self.openConnection()
            cursor.execute('''INSERT INTO 
                Temperatures(stationId, date, temperature) 
                VALUES(?, ?, ?)''', (stationId, date, round(temperature, 2)))
            self.connection.commit()
            self.connection.close()
            return True
        except sqlite3.IntegrityError as err:
            messagebox.showerror(title = 'Add Temperature', message = str(err))
            return False
    
    def getData(self, stationId, dateFrom = datetime.datetime.today(), dateTo = datetime.datetime.today(), statisticType = 'day'):
        # Create collection types
        DataCollection = namedtuple('DataCollection', 'temperatures minTemp maxTemp dateFrom dateTo')
        TemperatureCollection = namedtuple('TemperatureCollection', 'id stationId date temperature')
        
        # Get termperatres from db
        cursor = self.openConnection()
        cursor.execute('''SELECT 
                id,
                stationId,
                date, 
                temperature
            FROM Temperatures 
            WHERE stationId = ? AND date >= ? AND date <= ? 
            ORDER BY date ASC''', 
            (stationId, dateFrom, dateTo))
        tempRequest = cursor.fetchall()
        self.connection.close()
        
        if tempRequest:
            temperatureData = OrderedDict()
            for id, stationId, date, temperature in tempRequest:
                # Group by day, month or year
                if statisticType == 'year':
                    key = date.year
                elif statisticType == 'month':
                    key = date.month
                else:
                    key = date.day
                
                if key in temperatureData:
                    temperatureData[key].append(TemperatureCollection(id, stationId, date, temperature))
                else:
                    temperatureData[key] = [TemperatureCollection(id, stationId, date, temperature)]

            # Get min and max temperature
            minData = min(tempRequest, key=lambda x: x[3])
            maxData = max(tempRequest, key=lambda x: x[3])

            return DataCollection(
                temperatureData,
                TemperatureCollection(minData[0], minData[1], minData[2], minData[3]),
                TemperatureCollection(maxData[0], maxData[1], maxData[2], maxData[3]),
                dateFrom,
                dateTo)
     
        return []
