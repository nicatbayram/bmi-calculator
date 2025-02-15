from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk ()
root.title ("BMI Calculator")
root.geometry ("470x580+300+200")
root.resizable (False, False)
root.configure (bg = "#f0f1f5")

def BMI ():
    h = float (Height.get ())
    w = float (Weight.get ())
    
    #convert height from cm to m
    m = h / 100
    bmi = round(float(w / (m * m)), 1)
    label1.config(text=bmi)
    
    if bmi < 18.5:
        label2.config(text="Underweight")
        label3.config(text="You should eat more")
    
    elif bmi >= 18.5 and bmi < 24.9:
        label2.config(text="Normal")
        label3.config(text="You are healthy")
    
    elif bmi >= 25 and bmi < 29.9:
        label2.config(text="Overweight")
        label3.config(text="You should exercise more")
    
    elif bmi >= 30:
        label2.config(text="Obese")
        label3.config(text="You should eat less and exercise more")   
        
# Icon

image_icon = PhotoImage (file = "Images/icon.png")
root.iconphoto (False, image_icon)

# Top

top = PhotoImage (file = "Images/top.png")
top_image = Label (root, image = top, background="#f0f1f5")
top_image.place (x = -10, y = -10, relwidth = 1)

# Bottom Box

Label(root, width=72, height=18, bg="#D4EBF8").pack(side=BOTTOM)

# Two Boxes

box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale

scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)


####################################Slider1############################################

current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open("Images/man.png"))
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2

#Command to change background color of scale
style = ttk.Style()
style.configure('TScale', background='white')
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal", style='TScale', command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

####################################Slider2############################################

current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#Command to change background color of scale
style2 = ttk.Style()
style2.configure('TScale', background='white')
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style='TScale', command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

################################################################################


#Entry Box

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, font=("arial", 50), width=5, bg="#fff", fg="#000", bd = 0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, font=("arial", 50), width=5, bg="#fff", fg="#000", bd = 0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

#Man Image

secondimage = Label (root, bg="lightblue")
secondimage.place(x=70, y=530)


Button(root, text="View Report", width = 20, height = 2, bg="#001A6E", font="arial 10 bold", fg="white", command=BMI).place(x=280, y=340)

label1 = Label(root, font=("arial ", 30, "bold"), bg="#D4EBF8", fg="#22223B")
label1.place(x=155, y=340)

label2 = Label(root, font=("arial ", 20, "bold"), bg="#D4EBF8", fg="#22223B")
label2.place(x=160, y=420)

label3 = Label(root, font=("arial  ", 11, "bold"), bg="#D4EBF8" , fg="#22223B")
label3.place(x=160, y=500)


root.mainloop ()


