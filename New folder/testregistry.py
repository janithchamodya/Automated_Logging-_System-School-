from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root=Tk()
root.title("main")
root.geometry('380x640')# width,heigth


mainframe=tk.Frame(root)
mainframe.place(height=640,width=380)

def AdminRegi():
        global regiuser
        global regipassword
        global regispeacil
        global encrypted_message

        Label(mainframe,text="Admin Registration",font=("Monaco",18,"bold")) .place(x=80,y=10)
        Label(mainframe,text="Form",font=("Monaco",18,"bold")).place(x=180,y=40)

        class LimitedEntry(tk.Entry):
            def __init__(self, master=None, limit=10, **kwargs):
                super().__init__(master, **kwargs)

                self.limit = limit
                self['validate'] = 'key'
                self['validatecommand'] = (self.register(self.validate_text), '%P')
                
            def validate_text(self, new_text):
                return len(new_text) <= self.limit

        Label(mainframe,text="Enter Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=40,y=90)
        regiuser=LimitedEntry(mainframe,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10)
        regiuser.place(x=40,y=110,height=35,width=300)
        
        
        
        Label(mainframe,text="Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=40,y=170)
        regipassword=LimitedEntry(mainframe,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
        regipassword.place(x=40,y=190,height=35,width=300)
        

        
        

        Button(mainframe,text="Submit",font=('bold'),bg="Orange",width=40,border="0").place(x=40,y=310,height=35,width=300)
       
        Button(mainframe,text="Back",font=('bold'),bg="LightCoral",width=40,border="0",).place(x=150,y=360,height=35,width=100)
        
        
    
AdminRegi()
root.mainloop()