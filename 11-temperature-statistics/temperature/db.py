import sqlite3
import os.path
import datetime

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
        cursor.execute('''CREATE TABLE IF NOT EXISTS temperatures(id INTEGER PRIMARY KEY, date TIMESTAMP NOT NULL, temperature DECIMAL(5,2) NOT NULL)''')
        self.connection.commit()
        self.connection.close()
        
    def addTemperature(self, temperature, date=datetime.datetime.now()):
        # Add teperature to db
        self.openConnection()
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO temperatures(date,temperature) VALUES(?,?)''', (date, temperature))
        self.connection.commit()
        self.connection.close()
        return True
    
    def getTemperatures(self, dateFrom=datetime.datetime.today(), dateTo=datetime.datetime.today()):
        # Get termperatres from db
        self.openConnection()
        cursor = self.connection.cursor()
        cursor.execute('''SELECT id, date, temperature FROM temperatures WHERE date >= ? AND date <= ? ORDER BY date ASC''',(dateFrom, dateTo))
        data = cursor.fetchall()
        self.connection.close()
        return 
