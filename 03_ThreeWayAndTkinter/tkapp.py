#!/usr/bin/env python3
'''
Простой пример Tkinter
'''

import time
import tkinter as tk
import random
import tkinter.messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky = tk.N + tk.E + tk.S + tk.W)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.createWidgets()

    def createWidgets(self):
        """
        +----+----+----+----+
        |0   |1   |2   |3   |
        +----+----+----+----+
        |4   |5   |6   |7   |
        +----+----+----+----+
        |8   |9   |10  |11  |
        +----+----+----+----+
        |12  |13  |14  |15  |
        +----+----+----+----+
        """
        self.layout = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]
        for i in range(len(self.layout)):
            self.layout[i] = tk.StringVar(value = self.layout[i])
        self.neighbours = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7],
                           [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11],
                           [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15],
                           [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]
        self.reshuffle()

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

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

        self.uullButton = tk.Button(self, textvariable = self.layout[0], command = lambda: self.move(0))
        self.uullButton.grid(row = 1, column = 0, sticky = 'SEWN')
        self.uulButton = tk.Button(self, textvariable = self.layout[1], command = lambda: self.move(1))
        self.uulButton.grid(row = 1, column = 1, sticky = 'SEWN')
        self.uurButton = tk.Button(self, textvariable = self.layout[2], command = lambda: self.move(2))
        self.uurButton.grid(row = 1, column = 2, sticky = 'SEWN')
        self.uurrButton = tk.Button(self, textvariable = self.layout[3], command = lambda: self.move(3))
        self.uurrButton.grid(row = 1, column = 3, sticky = 'SEWN')

        self.ullButton = tk.Button(self, textvariable = self.layout[4], command = lambda: self.move(4))
        self.ullButton.grid(row = 2, column = 0, sticky = 'SEWN')
        self.ulButton = tk.Button(self, textvariable = self.layout[5], command = lambda: self.move(5))
        self.ulButton.grid(row = 2, column = 1, sticky = 'SEWN')
        self.urButton = tk.Button(self, textvariable = self.layout[6], command = lambda: self.move(6))
        self.urButton.grid(row = 2, column = 2, sticky = 'SEWN')
        self.urrButton = tk.Button(self, textvariable = self.layout[7], command = lambda: self.move(7))
        self.urrButton.grid(row = 2, column = 3, sticky = 'SEWN')

        self.ddllButton = tk.Button(self, textvariable = self.layout[8], command = lambda: self.move(8))
        self.ddllButton.grid(row = 3, column = 0, sticky = 'SEWN')
        self.ddlButton = tk.Button(self, textvariable = self.layout[9], command = lambda: self.move(9))
        self.ddlButton.grid(row = 3, column = 1, sticky = 'SEWN')
        self.ddrButton = tk.Button(self, textvariable = self.layout[10], command = lambda: self.move(10))
        self.ddrButton.grid(row = 3, column = 2, sticky = 'SEWN')
        self.ddrrButton = tk.Button(self, textvariable = self.layout[11], command = lambda: self.move(11))
        self.ddrrButton.grid(row = 3, column = 3, sticky = 'SEWN')

        self.dllButton = tk.Button(self, textvariable = self.layout[12], command = lambda: self.move(12))
        self.dllButton.grid(row = 4, column = 0, sticky = 'SEWN')
        self.dlButton = tk.Button(self, textvariable = self.layout[13], command = lambda: self.move(13))
        self.dlButton.grid(row = 4, column = 1, sticky = 'SEWN')
        self.drButton = tk.Button(self, textvariable = self.layout[14], command = lambda: self.move(14))
        self.drButton.grid(row = 4, column = 2, sticky = 'SEWN')
        self.drrButton = tk.Button(self, textvariable = self.layout[15], command = lambda: self.move(15))
        self.drrButton.grid(row = 4, column = 3, sticky = 'SEWN')

    def reshuffle(self):
        random.shuffle(self.layout)
        while not self.finishable():
            random.shuffle(self.layout)

    def move(self, index):
        i = -1
        for idx in self.neighbours[index]:
            if self.layout[idx].get() == '':
                i = idx
                break
        if i != -1:
            tmp = self.layout[i].get()
            self.layout[i].set(self.layout[index].get())
            self.layout[index].set(tmp)
        if self.finished():
            self.finish()

    def finishable(self):
        s = 0
        e = 0
        for i in range(len(self.layout)):
            if self.layout[i].get() == '':
                e = i // 4 + 1
                continue
            c = int(self.layout[i].get())
            for j in range(i + 1, len(self.layout)):
                if self.layout[j].get() != '' and int(self.layout[j].get()) < c:
                    s += 1
        return (s + e) % 2 == 0

    def finished(self):
        if self.layout[-1].get() != '':
            return False
        for i in range(len(self.layout) - 2):
            if int(self.layout[i].get()) > int(self.layout[i + 1].get()):
                return False
        return True

    def finish(self):
        tk.messagebox.showinfo('Victory!', 'You are victorious!!!')
        self.createWidgets()


app = Application()
app.master.title('15')
app.mainloop()
