#!/usr/bin/python3

import tkinter as tk
from tkinter.messagebox import showinfo
import types
from tkinter import font

def initDrawOval(event):
    '''
    If clicked inside existing oval start rewriting its coordinates.
    Else create a new one and rewrite it instead.
    '''
    wid = event.widget
#    wid.cur = len(wid.ovals)
    wid.ovals.append(wid.create_oval(event.x, event.y, event.x, event.y, fill = 'red'))
    wid.cur = wid.ovals[-1]
    wid.bind('<Motion>', drawOval)
    wid.curPosHor = 0
    wid.curPosVer = 0

def drawOval(event):
    '''Draws an orange blob in self.canv where the mouse is.
    '''
    #r = 5   # Blob radius
    wid = event.widget
    #wid.create_oval(event.x-r, event.y-r,
    #    event.x+r, event.y+r, fill='orange')
    if wid.cur != -1:
#        wid.itemconfigure(wid.cur,)
        crds = list(wid.coords(wid.cur))    # []

        if crds[0] > event.x:
            #crds[2] = crds[0]
            wid.curPosHor = 1   # left
            crds[0] = event.x
        elif crds[2] < event.x:
            wid.curPosHor = 0   # right
            crds[2] = event.x
        else:
            if wid.curPosHor == 0:
                crds[2] = event.x
            else:
                crds[0] = event.x

        if crds[1] > event.y:
            #crds[2] = crds[0]
            wid.curPosVer = 1   # up
            crds[1] = event.y
        elif crds[3] < event.y:
            wid.curPosVer = 0   # bottom
            crds[3] = event.y
        else:
            if wid.curPosVer == 0:
                crds[3] = event.y
            else:
                crds[1] = event.y

        wid.coords(wid.cur, crds[0], crds[1], crds[2], crds[3])

def stopDrawOval(event):
    event.widget.cur = -1

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
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit, cursor = 'X_cursor')
        self.quitButton.grid(row = 1, column = 1, sticky = 'E')

        text_font = font.Font(family="Consolas", size=10, weight="normal")
        #text = "some text"
        #text_len = text_font.measure(text)
        self.textPart.textWidget = tk.Text(self.textPart, cursor = 'xterm', font = text_font, insertbackground = 'black', bg = 'white', fg = 'black')
        self.textPart.textWidget.grid(sticky = 'NEWS')

        self.graphicPart.canvasWidget = tk.Canvas(self.graphicPart)
        self.graphicPart.canvasWidget.grid(sticky = 'NEWS')
        self.graphicPart.canvasWidget.ovals = []
        self.graphicPart.canvasWidget.cur = -1
        self.graphicPart.canvasWidget.bind('<Button-1>', initDrawOval)
        #self.graphicPart.canvasWidget.bind('<Motion>', drawOval)
        #self.graphicPart.canvasWidget.bind('<ButtonRelease-1>', lambda e: e.widget.cur = -1)
        self.graphicPart.canvasWidget.bind('<ButtonRelease-1>', stopDrawOval)

app = Application(title="Painty")
app.mainloop()

