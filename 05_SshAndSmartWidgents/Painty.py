#!/usr/bin/python3

import tkinter as tk
from tkinter.messagebox import showinfo
import types
from tkinter import font
from matplotlib.colors import is_color_like
import re
HEX_COLORS = re.compile(r'^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{9})$')


def is_hex_color(s):
    return HEX_COLORS.search(s)

def isPointInsideEllipse(x, y, x1, y1, x2, y2):
    h = (x1 + x2) // 2
    k = (y1 + y2) // 2
    rx = abs(x2 - x1) // 2
    ry = abs(y2 - y1) // 2
    if rx == 0 or ry == 0:
        return x1 <= x <= x2 and y1 <= y <= y2
    return ((x - h)/rx)**2 + ((y - k)/ry)**2 <= 1

def initDrawOval(event):
    '''
    If clicked inside existing oval start rewriting its coordinates.
    Else create a new one and rewrite it instead.
    '''
    wid = event.widget
#    wid.cur = len(wid.ovals)
    for i in wid.ovals:
        crds = wid.coords(i)
        if isPointInsideEllipse(event.x, event.y, crds[0], crds[1], crds[2], crds[3]):
            wid.cur = i
            wid.prev_x = event.x
            wid.prev_y = event.y
            wid.bind('<Motion>', moveOval)
            return

    wid.ovals.append(wid.create_oval(event.x, event.y, event.x, event.y, fill = '#F00', outline = '#000'))
    wid.cur = wid.ovals[-1]
    wid.bind('<Motion>', drawOval)
    wid.curPosHor = 0
    wid.curPosVer = 0

def moveOval(event):
    wid = event.widget
    if wid.cur != -1:
        wid.move(wid.cur, event.x - wid.prev_x, event.y - wid.prev_y)
        wid.prev_x = event.x
        wid.prev_y = event.y

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
        self.quitButton.grid(row = 1, column = 2, sticky = 'W')

        text_font = font.Font(family="Consolas", size=10, weight="normal")
        #text = "some text"
        #text_len = text_font.measure(text)
        self.textPart.textWidget = tk.Text(self.textPart, cursor = 'xterm', font = text_font, insertbackground = 'black', bg = 'white', fg = 'black')
        self.textPart.textWidget.grid(sticky = 'NEWS')
        self.textPart.textWidget.tag_config('errorTag', background = '#f00')

        self.graphicPart.canvasWidget = tk.Canvas(self.graphicPart)
        self.graphicPart.canvasWidget.grid(sticky = 'NEWS')
        self.graphicPart.canvasWidget.ovals = []
        self.graphicPart.canvasWidget.cur = -1
        self.graphicPart.canvasWidget.bind('<Button-1>', initDrawOval)
        #self.graphicPart.canvasWidget.bind('<Motion>', drawOval)
        #self.graphicPart.canvasWidget.bind('<ButtonRelease-1>', lambda e: e.widget.cur = -1)
        self.graphicPart.canvasWidget.bind('<ButtonRelease-1>', stopDrawOval)

        self.updateTextButton = tk.Button(self, text = 'Update', command = self.updateText)
        self.updateTextButton.grid(row = 1, column = 0, sticky = 'WE')
        self.updateGraphicButton = tk.Button(self, text = 'Update', command = self.updateGraphic)
        self.updateGraphicButton.grid(row = 1, column = 1, sticky = 'WE')

    def updateText(self):
        wid = self.graphicPart.canvasWidget
        self.textPart.textWidget.delete('0.0', 'end')
        txt =  'x1,y1,x2,y2,width,outline,fill\n'
        for i in self.graphicPart.canvasWidget.ovals:
            crds = wid.coords(i)
            opts = wid.itemconfigure(i)
            txt += '{},{},{},{},{},{},{}\n'.format(int(crds[0]), int(crds[1]), int(crds[2]), int(crds[3]), opts['width'][-1], opts['outline'][-1], opts['fill'][-1])
        self.textPart.textWidget.insert('0.0', txt)

    def updateGraphic(self):
        wid = self.graphicPart.canvasWidget
        txtwid = self.textPart.textWidget
        txtwid.tag_remove('errorTag', '0.0', 'end')
        txt = self.textPart.textWidget.get('0.0', 'end').split('\n')
        errored = False
        for i in wid.ovals:
            wid.delete(i)
        wid.ovals = []
        for i, line in enumerate(txt[1:-2], start = 2):
            tmp = line.split(',')
            if len(tmp) != 7:
                txtwid.tag_add('errorTag', '{}.0'.format(i), '{}.end'.format(i))
                errored = True
                continue
            try:
                x1 = int(tmp[0])
                y1 = int(tmp[1])
                x2 = int(tmp[2])
                y2 = int(tmp[3])
                w = float(tmp[4])
            except:
                txtwid.tag_add('errorTag', '{}.0'.format(i), '{}.end'.format(i))
                errored = True
                continue
            #if is_color_like(tmp[5]) == False or is_color_like(tmp[6]) == False:
            if is_hex_color(tmp[5]) == False or is_hex_color(tmp[6]) == False:
                txtwid.tag_add('errorTag', '{}.0'.format(i), '{}.end'.format(i))
                errored = True
                continue
            wid.ovals.append(wid.create_oval(x1, y1, x2, y2, fill = tmp[6], outline = tmp[5], width = w))

app = Application(title="Painty")
app.mainloop()

