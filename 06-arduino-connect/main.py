# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
import threading
import time

try:
    import serial
    import time
    import sys
    import serial.tools.list_ports
except ImportError:
    print('pip install pyserial')
    exit(1)


serPort = ''
setPortIndex = 0

lightStatus = False

app = Tk()

app.title('Home')
app.configure(background='DimGray')
app.geometry('600x600')
app.resizable(width=False, height=False)

ports = list(serial.tools.list_ports.comports())

for p in ports:
    while setPortIndex < 9:
        if 'CH340' in p[1]:
            serPort = 'COM' + str(setPortIndex)

        if 'CH340' in p[1] and serPort in p[1]:
            print('Found Arduino Uno on ' + serPort)
            setPortIndex = 9

        if setPortIndex == 8:
            print('UNO not found!')
            sys.exit()

        setPortIndex = setPortIndex + 1


arduino = serial.Serial(serPort, 9600, timeout=5)

text = Entry(app, width=300)
text.place(x = 0,y = 0)

def updateTemp():
    temp = arduino.readline()
    text.delete(0, END)
    text.insert(0, temp)
    time.sleep(1)
    updateTemp()

def lightOn():
    arduino.write(b'H')


def lightOff():
    arduino.write(b'L')


button = Button(app, text ="On", command = lightOn)
button.place(x = 50,y = 50)

button = Button(app, text ="Off", command = lightOff)
button.place(x = 100,y = 50)

thrTemp = threading.Thread(target=updateTemp)
thrTemp.start()


# while True:
#     print ('Writing: ',  commandToSend)
#     ser.write(str(commandToSend).encode())
#     time.sleep(1)
#     while True:
#         try:
#             print ('Attempt to Read')
#             readOut = ser.readline().decode('ascii')
#             time.sleep(1)
#             print ('Reading: ', readOut)
#             break
#         except:
#             pass
#     print ('Restart')
#     ser.flush() #flush the buffer
app.mainloop()
