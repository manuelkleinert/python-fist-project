from tkinter import *
from tkinter.ttk import *

app = Tk()

app.title('Home')
app.configure(background='DimGray')
app.geometry('600x600')
app.resizable(width=False, height=False)

note = Notebook(app)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)

note.add(tab1, text ='Tab 1')
note.add(tab2, text ='Tab 2')
note.add(tab3, text ='Tab 3')
note.pack(expand = 1, fill ="both")

content1 = Label(tab1, text = "Tab 1 to \ GeeksForGeeks")
content1.grid(column = 0, row = 0, padx = 30, pady = 30)

content2 = Label(tab2, text = "Tab 2 to \ GeeksForGeeks")
content2.grid(column = 0, row = 0, padx = 30, pady = 30)

app.mainloop()
