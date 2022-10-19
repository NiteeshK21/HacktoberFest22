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
    def Cd(): #function to accept customer data to allocate rooms. 
        app.destroy()
        win=tk.Tk()
        win.title("Customer Data") #title bar for room allocation. 
        win.geometry("1190x420") #setting geometry for windows. 
        win.configure(bg="black")
        Cd_label=tk.Label(win,text="Enter your name",font=("Comic Sans MS",15)) #label to accept name. 
        Cd_label.grid(row=0,column=0,sticky=tk.W)
        Cd_var=tk.StringVar()
        Cd_entry=tk.Entry(win,width=50,textvariable=Cd_var)
        Cd_entry.grid(row=0,column=1)
        Add_label=tk.Label(win,text="Enter Address(City)",font=("Comic Sans MS",15))
        Add_label.grid(row=1,column=0,sticky=tk.W)
        Add_var=tk.StringVar()
        Add_entry=tk.Entry(win,width=50,textvariable=Add_var)
        Add_entry.grid(row=1,column=1)
        In_label=tk.Label(win,text="Enter Checkin Date",font=("Comic Sans MS",15))
        In_label.grid(row=2,column=0,sticky=tk.W)
        In_var=tk.StringVar()
        In_entry=tk.Entry(win,width=50,textvariable=In_var)
        In_entry.grid(row=2,column=1)
        Out_label=tk.Label(win,text="Enter CheckOut Date",font=("Comic Sans MS",15))
        Out_label.grid(row=3,column=0,sticky=tk.W)
        Out_var=tk.StringVar()
        Out_entry=tk.Entry(win,width=50,textvariable=Out_var)
        Out_entry.grid(row=3,column=1)
        Room_label=tk.Label(win,text="We have the following Rooms for you,Choose one:-",font=("Comic Sans MS",25),bg="black",fg="white")
        Room_label.grid(row=4,column=1,sticky=tk.W)
        def newrn(): #reading data from database. 
            global rn
            try:
                with open("Customer Data.csv", "r") as f:
                    rn=int(f.readlines()[-1].split('Room No.-')[1][:-1])+1
            except:
                rn=100
        def RoomA():
            win=tk.Tk()
            win.title("Room")
            win.config(bg="White")
            newrn()
            A_label=tk.Label(win,text=f"YOUR ROOM NUMBER IS {rn}-A\n                                 thank you.",bg="White",fg="Black",font=("Algerian",30))
            A_label.grid(row=0,column=0,sticky=tk.W)
            def Okay():
                global rntype
                rntype='A'
                win.destroy()
            Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=1,column=1)
        A_button=tk.Button(win,text="Room Type A COSTS RS.6000 PN\-",font=("Comic Sans MS",13),command=RoomA)
        A_button.grid(row=5,column=1)
        def RoomB():
            win=tk.Tk()
            win.title("Room")
            win.configure(bg="white")
            newrn()
            A_label=tk.Label(win,text=f"YOUR ROOM NUMBER IS {rn}-B\n                                 thank you.",bg="White",fg="Black",font=("Algerian",30))
            A_label.grid(row=0,column=0,sticky=tk.W)
            def Okay():
                global rntype
                rntype='B'
                win.destroy()
            Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=1,column=1)
        B_button=tk.Button(win,text="Room Type B COSTS RS.5000 PN\-",font=("Comic Sans MS",13),command=RoomB)
        B_button.grid(row=6,column=1)
        def RoomC():
            win=tk.Tk()
            win.title("Room")
            win.configure(bg="white")
            newrn()
            C_label=tk.Label(win,text=f"YOUR ROOM NUMBER IS {rn}-C\n                                 thank you.",bg="white",fg="Black",font=("Algerian",30))
            C_label.grid(row=0,column=0,sticky=tk.W)
            def Okay():
                global rntype
                rntype='C'
                win.destroy()
            Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=1,column=1)
        C_button=tk.Button(win,text="Room Type C COSTS RS.4000 PN\-",font=("Comic Sans MS",13),command=RoomC)
        C_button.grid(row=7,column=1)
        def RoomD():
            win=tk.Tk()
            win.title("Room")
            win.configure(bg="white")
            newrn()
            D_label=tk.Label(win,text=f"YOUR ROOM NUMBER IS {rn}-D\n                                 thank you.",bg="White",fg="Black",font=("Algerian",30))
            D_label.grid(row=0,column=0,sticky=tk.W)
            def Okay():
                global rntype
                rntype='D'
                win.destroy()
            Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=1,column=1)
        D_button=tk.Button(win,text="Room Type D COSTS RS.3000 PN\-",font=("Comic Sans MS",13),command=RoomD)
        D_button.grid(row=8,column=1)
        x1=int(input("enter x1 : "))

        x2=int(input("enter x2 : "))

        y1=int(input("enter y1 : "))

        y2=int(input("enter y2 : "))

        result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

        print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)
        def Okay():
            win.destroy()
        Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
        Okay_button.grid(row=9,column=2)
        def OK():
            text ="\n"+"Name of Customer-"+Cd_entry.get() +"  City-"+Add_entry.get() +"  In date-"+In_entry.get() +"  Out Date-"+Out_entry.get()+"  Room No.-"+str(rn)+rntype
            with open("Customer Data.csv", "a") as f:
                f.write(text)
        Ok_button=tk.Button(win,text="Ok✓",bg="Lightgreen",font=("Algerian",15),command=OK)
        Ok_button.grid(row=9,column=1)
    Cd_button=tk.Button(app,text="           GET A ROOM             ",font=("Algerian",25),bg="black",fg="magenta2",command=Cd)
    Cd_button.grid(row=2,column=0)
    def Rt():
        app.destroy()
        win=tk.Tk()
        win.title("Calculating Roomrent")
        win.configure(bg="black")
        Rt_label=tk.Label(win,text="Select your RoomType:-",font=("Comic Sans MS",30),bg="black",fg="white")
        Rt_label.grid(row=0,column=0,sticky=tk.W)
        def Ra():
            win=tk.Tk()
            win.title("Room A")
            Nights_label=tk.Label(win,text="For how many nights did you stay",font=("Comic Sans MS",22))
            Nights_label.grid(row=0,column=0,sticky=tk.W)
            Nights_var=tk.StringVar()
            Nights_entry=tk.Entry(win,width=20,textvariable=Nights_var)
            Nights_entry.grid(row=0,column=1)
            def Roomrent():
                try:
                    win=tk.Tk()
                    win.title("Roomrent")
                    win.configure(bg="white")
                    Nights=int(Nights_entry.get())*6000
                    Nights1="Your","total","RoomRent","is","Rs.", Nights,"/-"
                    A_label=tk.Label(win,text=Nights1,bg="white",fg="Black",font=("Algerian",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    def Okay():
                        win.destroy()
                    Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
                    Okay_button.grid(row=1,column=1)
                except:
                    A_label=tk.Label(win,text="Please enter a correct value.",bg="black",fg="white",font=("Times New Roman",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    A_label.after(1000,A_label.destroy)
                    win.after(1000,win.destroy)
            Cr_button=tk.Button(win,text="Find Roomrent",bg="Lightgreen",font=("Comic Sans MS",15),command=Roomrent)
            Cr_button.grid(row=2,column=1)
            def Okay():
                win.destroy()
            Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=3,column=2)
        Ra_button=tk.Button(win,text="RoomType A: Rs.6000/night",font=("Comic Sans MS",13),command=Ra)
        Ra_button.grid(row=2,column=0)
        def Rb():
            win=tk.Tk()
            win.title("Room B")
            Nights_label=tk.Label(win,text="For how many nights did you stay",font=("Comic Sans MS",22))
            Nights_label.grid(row=0,column=0,sticky=tk.W)
            Nights_var=tk.StringVar()
            Nights_entry=tk.Entry(win,width=20,textvariable=Nights_var)
            Nights_entry.grid(row=0,column=1)
            def Roomrentb():
                try:
                    win=tk.Tk()
                    win.title("Roomrent")
                    win.configure(bg="white")
                    Nights=int(Nights_entry.get())*5000
                    Nights1="Your","total","RoomRent","is","Rs.",Nights,"/-"
                    A_label=tk.Label(win,text=Nights1,bg="white",fg="Black",font=("Algerian",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    def Okay():
                        win.destroy()
                    Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
                    Okay_button.grid(row=1,column=1)
                except:
                    A_label=tk.Label(win,text="Please enter a correct value.",bg="black",fg="white",font=("Times New Roman",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    A_label.after(1000,A_label.destroy)
                    win.after(1000,win.destroy)
            Cr_button=tk.Button(win,text="Find Roomrent",bg="Lightgreen",font=("Comic Sans MS",15),command=Roomrentb)
            Cr_button.grid(row=2,column=1)
            def Okay():
                win.destroy()
            Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=3,column=2)
        Rb_button=tk.Button(win,text="RoomType B: Rs.5000/night",font=("Comic Sans MS",13),command=Rb)
        Rb_button.grid(row=3,column=0)
        def Rc():
            win=tk.Tk()
            win.title("Room C")
            Nights_label=tk.Label(win,text="For how many nights did you stay",font=("Comic Sans MS",22))
            Nights_label.grid(row=0,column=0,sticky=tk.W)
            Nights_var=tk.StringVar()
            Nights_entry=tk.Entry(win,width=20,textvariable=Nights_var)
            Nights_entry.grid(row=0,column=1)
            def Roomrentc():
                try:
                    win=tk.Tk()
                    win.title("Roomrent")
                    win.configure(bg="white")
                    Nights=int(Nights_entry.get())*4000
                    Nights1="Your","total","RoomRent","is","Rs.",Nights,"/-"
                    A_label=tk.Label(win,text=Nights1,bg="white",fg="Black",font=("Algerian",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    def Okay():
                        win.destroy()
                    Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
                    Okay_button.grid(row=1,column=1)
                except:
                    A_label=tk.Label(win,text="Please enter a correct value.",bg="black",fg="white",font=("Times New Roman",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    A_label.after(1000,A_label.destroy)
                    win.after(1000,win.destroy)
            Cr_button=tk.Button(win,text="Find Roomrent",bg="Lightgreen",font=("Comic Sans MS",15),command=Roomrentc)
            Cr_button.grid(row=2,column=1)
            def Okay():
                win.destroy()
            Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=3,column=2)
        Rc_button=tk.Button(win,text="RoomType C: Rs.4000/night",font=("Comic Sans MS",13),command=Rc)
        Rc_button.grid(row=4,column=0)
        def Rd():
            win=tk.Tk()
            win.title("Room D")
            Nights_label=tk.Label(win,text="For how many nights did you stay",font=("Comic Sans MS",22))
            Nights_label.grid(row=0,column=0,sticky=tk.W)
            Nights_var=tk.StringVar()
            Nights_entry=tk.Entry(win,width=20,textvariable=Nights_var)
            Nights_entry.grid(row=0,column=1)
            def Roomrentd():
                try:
                    win=tk.Tk()
                    win.title("Roomrent")
                    win.configure(bg="white")
                    Nights=int(Nights_entry.get())*3000
                    Nights1="Your","total","RoomRent","is","Rs.",Nights,"/-"
                    A_label=tk.Label(win,text=Nights1,bg="white",fg="Black",font=("Algerian",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    def Okay():
                        win.destroy()
                    Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
                    Okay_button.grid(row=1,column=1)
                except:
                    A_label=tk.Label(win,text="Please enter a correct value.",bg="black",fg="white",font=("Times New Roman",30))
                    A_label.grid(row=0,column=0,sticky=tk.W)
                    A_label.after(1000,A_label.destroy)
                    win.after(1000,win.destroy)

            Cr_button=tk.Button(win,text="Find Roomrent",bg="Lightgreen",font=("Comic Sans MS",15),command=Roomrentd)
            Cr_button.grid(row=2,column=1)
            def Okay():
                win.destroy()
            Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
            Okay_button.grid(row=3,column=2)
        def Okay():
            win.destroy()
        Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
        Okay_button.grid(row=7,column=1)
        Rd_button=tk.Button(win,text="RoomType D: Rs.3000/night",font=("Comic Sans MS",13),command=Rd)
        Rd_button.grid(row=5,column=0)
    Rt_button=tk.Button(app,text="   CALCULATE  ROOMRENT   ",font=("Algerian",25),bg="black",fg="Darkgoldenrod2",command=Rt)
    Rt_button.grid(row=4,column=0)
    def Bill():
        app.destroy()
        text = " "
        with open("Restauant Bill.csv", "w") as Bi:
            Bi.write(text)
        win=tk.Tk()
        win.title("Restaurant bill")
        win.configure(bg="Black")
        Bill_label=tk.Label(win,text="WELCOME TO NSR FOODS ",bg="Black",fg="white",font=("Algerian",25))
        Bill_label.grid(row=0,column=0,sticky="NSWE",padx=(10, 10), pady=(7.5, 0))
        def Water():
            W_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            W_label.grid(row=1,column=1,sticky=tk.W)
            W_var=tk.IntVar()
            W_var.set(0)
            W_entry=tk.Entry(win,width=10,textvariable=W_var)
            W_entry.grid(row=1,column=2)
            def Cw():
                try:
                    tezt = "\n"+str(int(W_entry.get())*10)
                    with open("Restauant Bill.csv", "a") as w:
                        w.write(tezt)
                    global Cw
                    Cw=int(W_entry.get())*10
                    Cw1=("Rs.",(Cw))
                    Cw_label=tk.Label(win,text=Cw1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=1,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=1,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Cw_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Cw)
            Cw_button.grid(row=1,column=3)
        W_button=tk.Button(win,text="Water(500ML)@Rs.10",bg="LightBlue",font=("Comic Sans MS",15),command=Water)
        W_button.grid(row=1,column=0)
        def Tea():
            T_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            T_label.grid(row=2,column=1,sticky=tk.W)
            T_var=tk.IntVar()
            T_var.set(0)
            T_entry=tk.Entry(win,width=10,textvariable=T_var)
            T_entry.grid(row=2,column=2)
            def Ct():
                try:
                    tezt = "\n"+str(int(T_entry.get())*10)
                    with open("Restauant Bill.csv", "a") as t:
                        t.write(tezt)
                    Ct=int(T_entry.get())*10
                    Ct1=("Rs.",(Ct))
                    Ct_label=tk.Label(win,text=Ct1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Ct_label.grid(row=2,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=2,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Ct_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Ct)
            Ct_button.grid(row=2,column=3)
        T_button=tk.Button(win,text="    Tea(1Cup)@Rs.10    ",bg="LightBlue",font=("Comic Sans MS",15),command=Tea)
        T_button.grid(row=2,column=0)
        def Snacks():
            S_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            S_label.grid(row=3,column=1,sticky=tk.W)
            S_var=tk.IntVar()
            S_var.set(0)
            S_entry=tk.Entry(win,width=10,textvariable=S_var)
            S_entry.grid(row=3,column=2)
            def Cs():
                try:
                    tezt = "\n"+str(int(S_entry.get())*20)
                    with open("Restauant Bill.csv", "a") as s:
                        s.write(tezt)
                    global Cs
                    Cs=int(S_entry.get())*20
                    Cs1=("Rs.",(Cs))
                    Cs_label=tk.Label(win,text=Cs1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Cs_label.grid(row=3,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=3,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Cs_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Cs)
            Cs_button.grid(row=3,column=3)
        T_button=tk.Button(win,text="      Snacks@Rs.10      ",bg="LightBlue",font=("Comic Sans MS",15),command=Snacks)
        T_button.grid(row=3,column=0)

        def Breakfast_Combo():
            B_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            B_label.grid(row=4,column=1,sticky=tk.W)
            B_var=tk.IntVar()
            B_var.set(0)
            B_entry=tk.Entry(win,width=10,textvariable=B_var)
            B_entry.grid(row=4,column=2)
            def Cb():
                try:
                    tezt = "\n"+str(int(B_entry.get())*90)
                    with open("Restauant Bill.csvF", "a") as b:
                        b.write(tezt)
                    global Cb
                    Cb=int(B_entry.get())*90
                    Cb1=("Rs.",Cb)
                    Cb_label=tk.Label(win,text=Cb1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Cb_label.grid(row=4,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=4,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Cb_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Cb)
            Cb_button.grid(row=4,column=3)
        B_button=tk.Button(win,text="   Breakfast@Rs.90   ",bg="LightBlue",font=("Comic Sans MS",15),command=Breakfast_Combo)
        B_button.grid(row=4,column=0)
        def Lunch():
            L_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            L_label.grid(row=5,column=1,sticky=tk.W)
            L_var=tk.IntVar()
            L_var.set(0)
            L_entry=tk.Entry(win,width=10,textvariable=L_var)
            L_entry.grid(row=5,column=2)
            def Cl():
                try:
                    tezt = "\n"+str(int(L_entry.get())*110)
                    with open("Restauant Bill.csv", "a") as l:
                        l.write(tezt)
                    global Cl
                    Cl=int(L_entry.get())*110
                    Cl1=("Rs.",(Cl))
                    Cl_label=tk.Label(win,text=Cl1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Cl_label.grid(row=5,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=5,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Cl_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Cl)
            Cl_button.grid(row=5,column=3)
        L_button=tk.Button(win,text="      Lunch@Rs.110      ",bg="LightBlue",font=("Comic Sans MS",15),command=Lunch)
        L_button.grid(row=5,column=0)
        def Dinner():
            D_label=tk.Label(win,text="Enter Quantity",font=("Comic Sans MS",15),bg="black",fg="white")
            D_label.grid(row=6,column=1,sticky=tk.W)
            D_var=tk.IntVar()
            D_var.set(0)
            D_entry=tk.Entry(win,width=10,textvariable=D_var)
            D_entry.grid(row=6,column=2)
            def Cd():
                try:
                    tezt = "\n"+str(int(D_entry.get())*150)
                    with open("Restauant Bill.csv", "a") as d:
                        d.write(tezt)
                    global Cd
                    Cd=int(D_entry.get())*150
                    Cd1=("Rs.",(Cd))
                    Cd_label=tk.Label(win,text=Cd1,font=("Comic Sans MS",15),bg="black",fg="white")
                    Cd_label.grid(row=6,column=4,sticky=tk.W)
                except:
                    Cw_label=tk.Label(win,text="Please enter a number",font=("Comic Sans MS",15),bg="black",fg="white")
                    Cw_label.grid(row=6,column=4,sticky=tk.W)
                    Cw_label.after(950,Cw_label.destroy)
            Cd_button=tk.Button(win,text="Go",font=("Comic Sans MS",11),command=Cd)
            Cd_button.grid(row=6,column=3)
        D_button=tk.Button(win,text="     Dinner@Rs.150     ",bg="LightBlue",font=("Comic Sans MS",15),command=Dinner)
        D_button.grid(row=6,column=0)
        def Total():
            with open("Restauant Bill.csv", "r") as Bill:
                Sum0=Bill.readlines()
                Len=len(Sum0)
                Sum1=0
                for i in range(1,Len):
                    Sum1=Sum1+int(Sum0[i])
                Sum="Your","Restaurant","Bill","is","of","Rs.",Sum1,"/-"
                win=tk.Tk()
                win.title("Restaurant Bill")
                Total_label=tk.Label(win,text=Sum,font=("Comic Sans MS",25))
                Total_label.grid(row=0,column=0,sticky=tk.W)
                def Okay():
                    win.destroy()
                Okay_button=tk.Button(win,text="OK✓",bg="Lightgreen",font=("Algerian",15),command=Okay)
                Okay_button.grid(row=1,column=1)
        T_button=tk.Button(win,text="Total",bg="Lightgreen",font=("Algerian",15),command=Total)
        T_button.grid(row=7,column=1) #sample data
        def Okay():
            win.destroy()
        Okay_button=tk.Button(win,text="Close",bg="Red",fg="white",font=("Algerian",15),command=Okay)
        Okay_button.grid(row=9,column=3)
    Bill_button=tk.Button(app,text="    MOVE TO RESTAURANT    ",font=("Algerian",25),bg="black",fg="magenta2",command=Bill)
    Bill_button.grid(row=5,column=0)

    x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)
Title_button=tk.Button(win,text="Tap to view services",bg="LightGreen",font=("Algerian",18),command=start)
Title_button.grid(row=1,column=0)
win.mainloop()
