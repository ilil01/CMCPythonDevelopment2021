#!/usr/bin/python3

import tkinter as tk
from tkinter.messagebox import showinfo
import types

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

        # else the window will be empty
        self.createWidgets()

    def createWidgets(self):
        self.textPart = tk.LabelFrame(self, text = 'Text description')
        self.textPart.grid(row = 0, column = 0, sticky = 'NEWS')
        self.graphicPart = tk.LabelFrame(self, text = 'Graphic view')
        self.graphicPart.grid(row = 0, column = 1, sticky = 'NEWS')

app = Application(title="Painty")
app.mainloop()

