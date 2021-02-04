from tkinter import Frame, Label, StringVar, OptionMenu, W

class Select(Frame):
    def __init__(self, master = None, labelText = '', options = [], width = 30):
        Frame.__init__(self, master)
        
        self.pack()
        
        self.options = options
        
        self.label = Label(self, anchor = W, text = labelText, width = width)
        self.label.pack(side = 'left')
        
        self.var = StringVar()
        self.var.set(list(self.options.keys())[0])
        self.select = OptionMenu(self, self.var, *self.options.keys())
        self.select.pack(side='right')
    
    def setEvent(self, event):
        self.var.trace("w", event)
        
    def get(self):
        return self.options[self.var.get()]
    
    def setValue(self, value):
        self.var.set(value)