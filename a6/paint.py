from tkinter import *
import os
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from tkinter import ttk, colorchooser
import PIL
from PIL import ImageTk, Image, ImageDraw
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    fileName = "image1"

    def __init__(self):
        self.root = Tk()
        
        self.color_bg = 'white'
        
        self.open_button=Button(self.root,text="Open Image", command = self.open_img) 
        self.open_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=15, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)
        
        self.bgcolor_button = Button(self.root, text='bgcolor', command=self.change_bg)
        self.bgcolor_button.grid(row=0, column=5)
        
        self.save_button = Button(text="Save image", command=self.save)
        self.save_button.grid(row=0, column=6)
        
        self.c = Canvas(self.root, bg='white', width=700, height=700)
        self.c.grid(row=1, columnspan=8)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.brush_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
        
    def change_bg(self):   
        self.c.create_rectangle(0, 0, 701, 701, fill=askcolor(color=self.color)[1])

    def reset(self, event):
        self.old_x, self.old_y = None, None
        
    def open_img(self):
        self.fileName = askopenfilename()
        self.img = Image.open(self.fileName)
        self.c.image = ImageTk.PhotoImage(self.img)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')
        
    def save(self):
    	self.c.postscript(file = self.fileName + '.png')  
    	img = Image.open(self.fileName + '.png') 
    	img.save(self.fileName + '.png', 'png')   
   
if __name__ == '__main__':
	Paint()
    
    
