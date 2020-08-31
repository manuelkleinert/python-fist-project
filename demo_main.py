from tkinter import *
from button import myButton

window = Tk()

window.title('Demo Window')
window.geometry('350x200')

btn1 = myButton(window, 'Test 123')
btn1.setName('Button new Name')

btn2 = myButton(window, 'Test 456')
btn2.setPosition(20, 50)

btn3 = myButton(window, 'Test 999', 20, 90)

window.mainloop()
