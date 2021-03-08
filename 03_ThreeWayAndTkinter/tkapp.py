#!/usr/bin/env python3
'''
Простой пример Tkinter
'''

import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky = tk.N + tk.E + tk.S + tk.W)
        self.createWidgets()

    def createWidgets(self):
        self.layout = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]

        self.newButton = tk.Button(self, text = 'New', command = self.reshuffle, cursor = 'gumby')
        self.newButton.grid(row = 0, column = 0, columnspan = 2)
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit, cursor = 'X_cursor')
        self.quitButton.grid(row = 0, column = 2, columnspan = 2)

        """
        +----+----+----+----+
        |uull|uul |uur |uurr|
        +----+----+----+----+
        |ull |ul  |ur  |urr |
        +----+----+----+----+
        |dll |dl  |dr  |drr |
        +----+----+----+----+
        |ddll|ddl |ddr |ddrr|
        +----+----+----+----+
        """

        self.uullButton = tk.Button(self, textvariable = self.layout[0], command = lambda : self.move(0))
#        self.uullButton.rowconfigure(0, weight = 1)
        self.uullButton.grid(row = 1, column = 0, sticky = 'SEWN')
        self.uulButton = tk.Button(self, textvariable = self.layout[1], command = lambda : self.move(1))
        self.uulButton.grid(row = 1, column = 1, sticky = 'SEWN')
        self.uurButton = tk.Button(self, textvariable = self.layout[2], command = lambda : self.move(2))
        self.uurButton.grid(row = 1, column = 2, sticky = 'SEWN')
        self.uurrButton = tk.Button(self, textvariable = self.layout[3], command = lambda : self.move(3))
        self.uurrButton.grid(row = 1, column = 3, sticky = 'SEWN')

        self.ullButton = tk.Button(self, textvariable = self.layout[4], command = lambda : self.move(4))
        self.ullButton.grid(row = 2, column = 0, sticky = 'SEWN')
        self.ulButton = tk.Button(self, textvariable = self.layout[5], command = lambda : self.move(5))
        self.ulButton.grid(row = 2, column = 1, sticky = 'SEWN')
        self.urButton = tk.Button(self, textvariable = self.layout[6], command = lambda : self.move(6))
        self.urButton.grid(row = 2, column = 2, sticky = 'SEWN')
        self.urrButton = tk.Button(self, textvariable = self.layout[7], command = lambda : self.move(7))
        self.urrButton.grid(row = 2, column = 3, sticky = 'SEWN')

        self.ddllButton = tk.Button(self, textvariable = self.layout[8], command = lambda : self.move(8))
        self.ddllButton.grid(row = 3, column = 0, sticky = 'SEWN')
        self.ddlButton = tk.Button(self, textvariable = self.layout[9], command = lambda : self.move(9))
        self.ddlButton.grid(row = 3, column = 1, sticky = 'SEWN')
        self.ddrButton = tk.Button(self, textvariable = self.layout[10], command = lambda : self.move(10))
        self.ddrButton.grid(row = 3, column = 2, sticky = 'SEWN')
        self.ddrrButton = tk.Button(self, textvariable = self.layout[11], command = lambda : self.move(11))
        self.ddrrButton.grid(row = 3, column = 3, sticky = 'SEWN')

        self.dllButton = tk.Button(self, textvariable = self.layout[12], command = lambda : self.move(12))
        self.dllButton.grid(row = 4, column = 0, sticky = 'SEWN')
        self.dlButton = tk.Button(self, textvariable = self.layout[13], command = lambda : self.move(13))
        self.dlButton.grid(row = 4, column = 1, sticky = 'SEWN')
        self.drButton = tk.Button(self, textvariable = self.layout[14], command = lambda : self.move(14))
        self.drButton.grid(row = 4, column = 2, sticky = 'SEWN')
        self.drrButton = tk.Button(self, textvariable = self.layout[15], command = lambda : self.move(15))
        self.drrButton.grid(row = 4, column = 3, sticky = 'SEWN')

    def reshuffle(self):
        pass

    def move(self, index):
        pass

app = Application()
app.master.title('15')
app.mainloop()
