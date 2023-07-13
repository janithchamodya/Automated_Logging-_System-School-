from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root=Tk()
root.title("main")
root.geometry('380x620')# width,heigth


mainframe=tk.Frame(root)
mainframe.place(height=620,width=380)

def login():

    topi=Label(root,text    ="Bus Ticketing ",font=("Monaco",18,"bold"),)
    topi.place(x=100,y=20)
    topi1=Label(root,text="System",font=("Monaco",18,"bold"))
    topi1.place(x=140,y=50)

    img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((380,100)))
    lable1=Label(mainframe,image=img)
    Label.img=img
    lable1.place(height=100,width=380,x=0,y=0)


    #---------------------------------this registry form--------------------------
    Label(mainframe,bg="white",text="Enter User Name").place(x=100,y=90)
    euser=Entry(mainframe,border="0",bg="Gainsboro",justify=tk.CENTER,)
    euser.place(x=20,y=110,height=35,width=300)

    Label(mainframe,bg="white",text="Enter Password").place(x=100,y=145)
    epassword=Entry(mainframe,border="0",bg="Gainsboro",justify=tk.CENTER,show="*")
    epassword.place(x=20,y=165,height=35,width=300)
        

    btnlogin=Button(mainframe,bg="Orange",text="Login",border="0",font=('bold')  )
    btnlogin.place(x=20,y=230,height=35,width=300,)

    Label(mainframe,bg="white",text="OR",font=("verdana" ,10,"bold")).place(x=200,y=277)
        

    btnRgi=Button(mainframe,bg="Cyan",text="Register" ,command=Adminregi,border="0",font=('bold'))
    btnRgi.place(x=20,y=310,height=35,width=300)
    btnRgiback=Button(mainframe,text="Back",bg="LightCoral" ,border="0",font=('bold'))
    btnRgiback.place(x=100,y=360,height=35,width=100)

    def Adminregi():
        #global regiuser
        #global regipassword
            
        mainframe2=tk.Frame(mainframe)
        mainframe2.place(height=620,width=380)

        Label(mainframe2,text="Admin Registration",font=("Monaco",18,"bold")) .place(x=80,y=10)
        Label(mainframe2,text="Form",font=("Monaco",18,"bold")).place(x=180,y=40)

        class LimitedEntry(tk.Entry):
            def __init__(self, master=None, limit=10, **kwargs):
                super().__init__(master, **kwargs)

                self.limit = limit
                self['validate'] = 'key'
                self['validatecommand'] = (self.register(self.validate_text), '%P')
                    
            def validate_text(self, new_text):
                return len(new_text) <= self.limit

        Label(mainframe2,text="Enter Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=40,y=90)
        regiuser=LimitedEntry(mainframe2,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10)
        regiuser.place(x=40,y=110,height=35,width=300)
            
            
            
        Label(mainframe2,text="Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=40,y=170)
        regipassword=LimitedEntry(mainframe2,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
        regipassword.place(x=40,y=190,height=35,width=300)
            

            
            

        Button(mainframe2,text="Submit",font=('bold'),bg="Orange",width=40,border="0").place(x=40,y=310,height=35,width=300)
        
        Button(mainframe2,text="Back",font=('bold'),bg="LightCoral",width=40,border="0",command=login).place(x=150,y=360,height=35,width=100)
            

    






login()
root.mainloop()    
