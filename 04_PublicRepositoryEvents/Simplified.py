#!/usr/bin/env python3
'''
Решение первой задачи из README
'''

import time
import tkinter as tk
from tkinter.messagebox import showinfo
import types

def construct(obj, attr):
    '''
    __getattr__ для вспомогательного класса, чтобы подвязывался правильный self
    '''
    return lambda what, geo, **args: obj.constructField(attr, what, geo, **args)

class Application(tk.Frame):
    def __init__(self, mast=None, **args):
        super().__init__(mast)
        if 'title' in args:
            self.master.title(args['title'])

        # initial setup to make everything dynamic
        self.grid(sticky = 'NEWS')

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

        # else the window will be empty
        self.createWidgets()
    
    def __getattr__(self, attr):
        return lambda what, geo, **args: self.constructField(attr, what, geo, **args)

    def constructField(self, attr, what, geo, **args):
        '''
        Создать новое поле-виджет, поддерживающее возможность 
        создавать новые поля таким же образом
        '''
        setattr(self, attr, type(what.__name__ + 'Intermediate', (what,),\
                {'__getattr__' : construct, 'constructField' : Application.constructField})(self, **args))
        tmp = geo.split('/')
        if len(tmp) == 1:
            # no gravity
            grab = 'NEWS'
            tmp = geo
        else:
            grab = tmp[1]
            tmp = tmp[0]
        tmp = tmp.split(':')
        rowchar = tmp[0].split('+')
        colchar = tmp[1].split('+')

        if len(rowchar) == 1:
            # no height
            height = 0
        else:
            height = int(rowchar[1])
        rowchar = rowchar[0].split('.')
        if len(rowchar) == 1:
            # no rowweight
            rowweight = 1
        else:
            rowweight = int(rowchar[1])
        rown = int(rowchar[0])

        if len(colchar) == 1:
            # no height
            width  = 0
        else:
            width  = int(colchar[1])
        colchar = colchar[0].split('.')
        if len(colchar) == 1:
            # no colweight
            colweight = 1
        else:
            colweight = int(colchar[1])
        coln = int(colchar[0])

        self.rowconfigure(rown, weight = rowweight)
        self.columnconfigure(coln, weight = colweight)

        getattr(self, attr).grid(row = rown, rowspan = height + 1, column = coln, columnspan = width + 1, sticky = grab)
        tmp = getattr(self, attr)
        tmp.constructField = types.MethodType(Application.constructField, tmp)

    def createWidgets(self):
        pass

class App(Application):
    def createWidgets(self):
        self.message = "Congratulations!\nYou've found a sercet level!"
        self.F1(tk.LabelFrame, "1:0", text="Frame 1")
        self.F1.B1(tk.Button, "0:0/NW", text="1")
        self.F1.B2(tk.Button, "0:1/NE", text="2")
        self.F1.B3(tk.Button, "1:0+1/SEW", text="3")
        self.F2(tk.LabelFrame, "1:1", text="Frame 2")
        self.F2.B1(tk.Button, "0:0/N", text="4")
        self.F2.B2(tk.Button, "0+1:1/SEN", text="5")
        self.F2.B3(tk.Button, "1:0/S", text="6")
        self.Q(tk.Button, "2.0:1.2/SE", text="Quit", command=self.quit)
        self.F1.B3.bind("<Any-Key>", lambda event: showinfo(self.message.split()[0], self.message))

app = App(title="Sample application")
app.mainloop()
