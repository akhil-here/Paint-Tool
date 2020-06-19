from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox

root=Tk()
root.title("Paint")
root.geometry("1000x1000")

brush_color="black"

#Paint function
def paint(e):
    b_width="%0.0f" % float(my_scale.get())
    b_color=brush_color
    b_type=brush_type.get()
    x1 = e.x - 1
    y1 = e.y - 1
    x2 = e.x + 1
    y2 = e.y + 1
    my_canvas.create_line(x1,y1,x2,y2,fill=b_color,width=b_width,capstyle=b_type,smooth=True)

#Paint2 function
def paint2(e):
    b_width="%0.0f" % float(my_scale.get())
    b_color="white"
    b_type="round"
    x1 = e.x - 1
    y1 = e.y - 1
    x2 = e.x + 1
    y2 = e.y + 1
    my_canvas.create_line(x1,y1,x2,y2,fill=b_color,width=b_width,capstyle=b_type,smooth=True)

#Changing the slider label
def change_width(e):
    my_scale_label.config(text="%0.0f" % float(my_scale.get()))

#Changing the eraser label:
def change_eraser_width(e):
    e_scale_label.config(text="%0.0f" % float(e_scale.get()))

def erase():
    my_canvas.bind('<B1-Motion>',paint2)

#Changing the brush color
def change_brush_color():
    global brush_color
    brush_color="black"
    brush_color=colorchooser.askcolor(color=brush_color)[1] 
    my_canvas.bind('<B1-Motion>',paint)

#Changing the canvas color
def change_canvas_color():
    global canvas_color
    canvas_color="black"
    canvas_color=colorchooser.askcolor(color=canvas_color)[1] 
    my_canvas.config(bg=canvas_color)
    my_canvas.bind('<B1-Motion>',paint)

#CLear screen
def clear():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

#Saving the image
def save():
    result=filedialog.asksaveasfilename(initialdir='D:/OLD_DATA\1\Desktop/akhil files/akhil_tkinter/new-tkinter/new_images',filetypes=(("PNG Files","*.png"),("All Files","*.*")))
    
    if result.endswith('.png'):
        pass
    else:
        result=result+".png"
    
    if result:
        x=root.winfo_rootx()+my_canvas.winfo_x()
        y=root.winfo_rooty()+my_canvas.winfo_y()
        x1=x+my_canvas.winfo_width()
        y1=y+my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)

        messagebox.showinfo("Image Saved","Image has been successfully saved!!!!")

w=650
h=450

#Canvas
my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>',paint)

#Main brush frame
brush_frame=Frame(root)
brush_frame.pack(pady=20)

#Brush size frame
brush_size_frame=LabelFrame(brush_frame,text="Brush Width")
brush_size_frame.grid(row=0,column=0,padx=50)
my_scale=ttk.Scale(brush_size_frame,from_=1,to=100,value=10,orient=VERTICAL,command=change_width)
my_scale.pack(padx=10,pady=10)
my_scale_label=Label(brush_size_frame,text=my_scale.get())
my_scale_label.pack(pady=5)

#Eraser frame
eraser_frame=LabelFrame(brush_frame,text="Eraser Width")
eraser_frame.grid(row=0,column=1,padx=50)
e_scale=ttk.Scale(eraser_frame,from_=1,to=100,value=10,orient=VERTICAL,command=change_eraser_width)
e_scale.pack(padx=10,pady=10)
e_scale_label=Label(eraser_frame,text=e_scale.get())
e_scale_label.pack(pady=5)

#Brush type frame
brush_type_frame=LabelFrame(brush_frame,text="Brush Type")
brush_type_frame.grid(row=0,column=2,padx=50)
brush_type=StringVar()
brush_type.set("round")
b1=Radiobutton(brush_type_frame,text="Round",variable=brush_type,value="round")
b2=Radiobutton(brush_type_frame,text="Diamond",variable=brush_type,value="projecting")
b3=Radiobutton(brush_type_frame,text="Slash",variable=brush_type,value="butt")
b1.pack(anchor=W)
b2.pack(anchor=W)
b3.pack(anchor=W)

#Color frame
brush_color_frame=LabelFrame(brush_frame,text=" Change Color")
brush_color_frame.grid(row=0,column=3,padx=50)
brush_color_button=Button(brush_color_frame,text="Brush Color",command=change_brush_color)
brush_color_button.pack(padx=5,pady=10)
canvas_color_button=Button(brush_color_frame,text="Canvas Color",command=change_canvas_color)
canvas_color_button.pack(padx=5,pady=10)
eraser_button=Button(brush_color_frame,text="Eraser",command=erase)
eraser_button.pack(padx=5,pady=10)

#Options frame
options_frame=LabelFrame(brush_frame,text="Options")
options_frame.grid(row=0,column=4)
clear_button=Button(options_frame,text="Clear Screen",command=clear)
clear_button.pack(padx=10,pady=10)
save_button=Button(options_frame,text="Save as PNG",command=save)
save_button.pack(padx=10,pady=10)

root.mainloop()
