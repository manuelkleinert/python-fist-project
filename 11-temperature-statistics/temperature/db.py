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
        self.connection=sqlite3.connect(self.fullPath)
        self.createTable()
        
    def createTable(self):
        # Create Table if not exist
        cursor=self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS temperatures(date DATETIME, temperature DECIMAL(5,2))''')
        self.connection.commit()
        
    def addTemperature(self,temperature):
        # Add teperature to db
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO temperatures VALUES(?,?)''', (datetime.datetime.now(), temperature))
        self.connection.commit()
        return True
    
    def getTemperatures(self, dateFrom=datetime.datetime.today(), dateTo=datetime.datetime.today()):
        # Get termperatres from db
        cursor = self.connection.cursor()
        cursor.execute('''SELECT date,temperature FROM temperatures WHERE date >= ? AND date <= ?''',(dateFrom, dateTo))
        return cursor.fetchall()
