#!/usr/bin/env python3
'''
'''

import time
import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

    def createWidgets(self):
        pass

app = Application(title="Sample application")
app.mainloop()
