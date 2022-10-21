from pickle import GLOBAL #importing pickle module for searilising and desearilising objects.
import tkinter as tk #importing tkinter for using graphical user interface in python.
from PIL import ImageTk,Image #imported ImageTk and Image for adding images in tkinter window.
win=tk.Tk() #Creating a new window in tkinter
win.title("Welcome") #set title of window as Welcome
win.geometry("980x600") #setting geometry of the Window
path="Hotel.jpg" #set the path of image
image=Image.open(path) #opening image from path
image=image.resize((980,600),Image.ANTIALIAS) #setting size of image
img=ImageTk.PhotoImage(image)
pic=tk.Label(win,image=img,bg="black")
pic.grid(row=1,column=0,columnspan=2,rowspan=2,sticky=tk.E,padx=5,pady=5)
win.configure(bg="black")
Bill_label=tk.Label(win,text="WELCOME TO HOTEL NSR",bg="black",fg="Snow",font=("Algerian",55))
Bill_label.grid(row=0,column=0,sticky="NSWE")
rn = 100
rntype=''

def start(): #function that starts the whole program system. 
    app=tk.Tk()
    app.title("Services")
    app.geometry("+450+350")
    app.configure(bg="black")
    def Cd():
        app.destroy()
        win=tk.Tk()
        win.title("Customer Data")
        win.geometry("1190x420")
        win.configure(bg="black")
        Cd_label=tk.Label(win,text="Enter your name",font=("Comic Sans MS",15))
        Cd_label.grid(row=0,column=0,sticky=tk.W)
        Cd_var=tk.StringVar()
        Cd_entry=tk.Entry(win,width=50,textvariable=Cd_var)
        Cd_entry.grid(row=0,column=1)
        Add_label=tk.Label(win,text="Enter Address(City)",font=("Comic Sans MS",15))
        Add_label.grid(row=1,column=0,sticky=tk.W)
        Add_var=tk.StringVar()
    
win.mainloop()
