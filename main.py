# IMPORTS
from tkinter import *
from tkinter.ttk import LabelFrame
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
import PIL
from PIL import Image,ImageDraw

# PAINT APP
class PaintApp:
    def __init__(self):
        # Variables
        self.canvas_color = 'white'
        self.brush_color = 'black'
        self.brush_size = 20
        
        # Canvas
        self.c = Canvas(root,bg=self.canvas_color,bd=4,relief=GROOVE,width=670,height=300)
        self.c.grid(row=0,column=3,sticky=N)
        self.c.bind('<B1-Motion>',self.paint)

        # Calling Functions
        self.brush_color_btn()
        self.bg_color_btn()
        self.eraser_btn()
        self.brush_size_btn()
        self.clear_btn()

    def paint(self,event):
        ''' This function is responsible for painting on canvas. '''
        from_x = event.x - 3
        from_y = event.y - 3
        to_x = event.x + 3
        to_y = event.y + 3

        self.c.create_oval(from_x,from_y,to_x,to_y,fill=self.brush_color,outline=self.brush_color,width=self.brush_size)

    # BUTTONS
    def brush_color_btn(self):
        ''' It displays a button that changes brush's colour. '''
        b = Button(root,text='Brush Colour',font='ariel 10 bold',width=14,command=self.brush_color_func,bg='#ff7ace')
        b.grid(row=0,column=0,pady=(0,320),sticky=W)

    def eraser_btn(self):
        ''' It displays an eraser button '''
        b = Button(root,text='Eraser',font='ariel 10 bold',width=14,command=self.eraser_func,bg='#20bebe')
        b.grid(row=0,column=0,pady=(0,110),sticky=W)

    def bg_color_btn(self):
        ''' It displays a button that changes the background colour. '''
        b = Button(root,text='Window Colour',font='ariel 10 bold',width=14,command=self.bg_color_func,bg='#ff7ace')
        b.grid(row=0,column=0,pady=(0,250),sticky=W)

    def brush_size_btn(self):
        ''' It displays a slider and a button that changes the brush's size. '''
        self.s = Scale(root,from_=30,to=3,bg='#ff5757')
        self.s.grid(row=0,column=0,pady=(130,0))

        b = Button(root,text='Change Brush Size',font='ariel 10 bold',width=14,command=self.brush_size_func,bg='#ff5757')
        b.grid(row=0,column=0,pady=(0,30))

    def clear_btn(self):
        ''' It displays a button to clear the screen. '''
        b = Button(root,text='Clear',font='ariel 10 bold',width=14,command=self.clear_func,bg='#20bebe')
        b.grid(row=0,column=0,pady=(0,180))


    # COMMANDS
    def brush_size_func(self):
        ''' It sets the brush size to the value of the Slider. '''
        self.brush_size = self.s.get()

    def eraser_func(self):
        ''' It sets the brush colour to the canvas' colour. '''
        self.brush_color = self.canvas_color

    def bg_color_func(self):
        ''' It asks the user for a colour and sets that colour as the background colour. '''
        c = askcolor()
        self.canvas_color = c[1]
        self.c['bg'] = self.canvas_color

    def brush_color_func(self):
        ''' It asks the user for a colour and sets that colour as the brush colour. '''
        c = askcolor()
        self.brush_color = c[1]

    def clear_func(self):
        ''' It clears the screen. '''
        self.c.delete('all')

# MAIN PROGRAM
if __name__ == '__main__':
    root = Tk()

    root.title('Paint App')
    root.geometry('820x310')
    root.wm_iconbitmap('paint.ico')

    PaintApp()

    root.mainloop()