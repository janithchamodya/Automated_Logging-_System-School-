from curses import window
from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import window_height
import cv2
import qrcode
import os
import io
from io import BytesIO
from notifypy import Notify
from tkinter import messagebox
import pickle
import numpy as np
from PIL import Image
import pickle
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from pyzbar.pyzbar import decode

#to get Email service and sent image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.utils import COMMASPACE
from email import encoders
from email.mime.image import MIMEImage

#get date and time in local computer
import time
import datetime
from datetime import datetime

import keyboard

#to gee this play music when wrog person log to the system
import pygame

# connect to server
import mysql.connector
from mysql.connector import Error
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="JANITHchamodya",
  database="MyProject"
)



root= tk.Tk()
root.title("Main Window")
root.geometry('500x400')
root.minsize(500, 400) # minimum size of 500x400 pixels
root.maxsize(500, 400) # maximum size of 500x400 pixels
#root.geometry('widthxheight')
#root.eval('tk::PlaceWindow.center')

mycursor = mydb.cursor()



def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    print(screen_height)
    print(screen_width)

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

center_window(root, 500, 400)

#strat page
def loginmain():
    
    

    mainframe=tk.Frame(root)
    mainframe.place(height=400,width=500)
    
    img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((500,500)))
    lable1=Label(mainframe,image=img)
    Label.img=img
    lable1.place(height=400,width=500) 

    mainframe1=Frame(mainframe)
    mainframe1.place(x=40,y=90,height=220,width=420)

    lbllogin=Label(mainframe,text="Atomated ",font=("Monaco",20,"bold"))
    lbllogin.place(y=110,x=180)
    Label().pack()
    lbllogin=Label(mainframe,text="Logging System",font=("Monaco",20,"bold"))
    lbllogin.place(y=140,x=130)


    btnAdmin=Button(mainframe,text="Admin",command=MainFrame,bg="DeepSkyBlue")
    btnAdmin.place(y=220,x=50,height=30,width=100)

    btnStudent=Button(mainframe,text="Student",bg="LightGray",command=student)
    btnStudent.place(y=220,x=200,height=30,width=100)

    btnTeacher=Button(mainframe,text="Teacher",bg="LightGray",command=teacher)
    btnTeacher.place(y=220,x=350,height=30,width=100)


#----------------choose admin or super admin----------
def MainFrame():
  mainAdmin=tk.Frame(root)
  mainAdmin.place(height=400,width=500)
    
  img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((500,500)))
  lable1=Label(mainAdmin,image=img)
  Label.img=img
  lable1.place(height=400,width=500)

   

  mainframe=Frame(mainAdmin)
  mainframe.place(x=40,y=90,height=220,width=420)
  
  Button(mainAdmin,text="Admin",bg="DeepSkyBlue",command=Adminfrom ).place(y=185,x=113,height=30,width=100)
  Button(mainAdmin,text="Supper Admin",command=superlogging,bg="DeepSkyBlue").place(y=185,x=286,height=30,width=100)
  Button(mainAdmin,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=loginmain).place(x=200,y=360,height=35,width=100)

def superlogging():
  global sname
  global spw
  
  superlog=tk.Frame(root,bg="white")
  superlog.place(height=400,width=500)

  Label(superlog,bg="white",text="Enter User Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=50)
  sname=Entry(superlog,border="0",bg="Gainsboro",justify=tk.CENTER)
  sname.place(x=100,y=70,height=35,width=300)

  Label(superlog,bg="white",text="Enter Password",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=130)
  spw=Entry(superlog,border="0",bg="Gainsboro",justify=tk.CENTER,show="*")
  spw.place(x=100,y=150,height=35,width=300)

  btnSlogin=Button(superlog,bg="Orange",text="Login",border="0",font=('bold') ,command=SuperFrame )
  btnSlogin.place(x=100,y=200,height=35,width=300,)

  btnSback=Button(superlog,text="Back",bg="LightCoral" ,border="0",command=MainFrame,font=('bold'))
  btnSback.place(x=200,y=360,height=35,width=100)

def SuperFrame():

  if((sname.get()!="")and(spw!="")):
    query1 = "SELECT name,password FROM SuperAdminRegi WHERE name=%s and password=%s"
        
    mycursor.execute(query1,(sname.get(),spw.get()))
    result = mycursor.fetchall()

    # -------------------------------------------------------start the Super Admin performance area-----------------------------------------------------

    if result:
      #-------------SUPER ADMIN NOTIFICATION-----------

      mycursor.execute("SELECT COUNT(id) FROM TempAdminRegi")
      row_count = mycursor.fetchone()[0]

      # Check if the row count are zero
      if row_count != 0:
    
        notification = Notify()
        notification.title = "Super Admin "
        notification.message = "Now, You Have New " +str(row_count) + " Registers ."
        notification.icon="Image\\icon.png"
        notification.send()
      
      superF=tk.Frame(root)
      superF.place(height=400,width=500)

      superFBack=tk.Frame(root)
      superFBack.place(height=50,width=500,x=0,y=350)

      #create notification bar
      supernotification=tk.Frame(superF)
      supernotification.place(height=50,width=500,x=0,y=0)

      Label(supernotification,bg="Orange").place(x=0,y=0,width=500,height=50)
      Button(supernotification,bg="DeepSkyBlue",text="Drop Admin",command=SDrop).place(x=60,y=10,width=120,height=30)
      Button(supernotification,bg="DeepSkyBlue",text="Notification",command=SNotification).place(x=200,y=10,width=120,height=30)
      Button(supernotification,bg="DeepSkyBlue",text="Register",command=SRegister).place(x=340,y=10,width=120,height=30)

      btnSback=Button(superFBack,text="Back",bg="LightCoral" ,border="0",command=superlogging,font=('bold'))
      btnSback.place(x=200,y=10,height=35,width=100)
    else:
      messagebox.showinfo("Invalid","Check Again Password And username")

def SDrop():
  
    global DropAdmin
    global DeactiveAdmin

    DeleteAdmin=tk.Frame(root)
    DeleteAdmin.place(height=400,width=500)
    Button(DeleteAdmin,text="Drop Admin",bg="Crimson",border="0",command=DropAdminMethode).place(x=75,y=50,height=35,width=200)
    Button(DeleteAdmin,text="De-Activate",bg="Crimson",border="0",command=DeactiveAdminMethod).place(x=75,y=100,height=35,width=200)

    DropAdmin=Entry(DeleteAdmin,border="1",bg="Gainsboro",justify=tk.CENTER)
    DropAdmin.place(x=300,y=50,height=35,width=70)

    DeactiveAdmin=Entry(DeleteAdmin,border="1",bg="Gainsboro",justify=tk.CENTER)
    DeactiveAdmin.place(x=300,y=100,height=35,width=70)

    #්------------admin Deatils View to super admin-------------------
    
    Label(DeleteAdmin,text="View Data Admnin",font=("Monaco",18,"bold")).place(x=130,y=150)
    
    ViewDataAdmin=ttk.Frame(DeleteAdmin)
    ViewDataAdmin.place(height=150,x=180,y=200)

    scrollbar = ttk.Scrollbar(ViewDataAdmin)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    mycursor.execute("SELECT name,position FROM adminregister ")
                                
    recordAdmin = mycursor.fetchall()

                                
     # Add the student records to a Tkinter listbox in the frame
    listbox = tk.Listbox(ViewDataAdmin,justify="center",bg="white",yscrollcommand=scrollbar.set)
    for record in recordAdmin:
        listbox.insert(tk.END, "Name/Position Is :")
        listbox.insert(tk.END, record)
        listbox.insert(tk.END," ")
        listbox.insert(tk.END," ")
        
        
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)


    scrollbar.config(command=listbox.yview)




    btnSback=Button(DeleteAdmin,text="Back",bg="LightCoral" ,border="0",command=SuperFrame,font=('bold'))
    btnSback.place(x=200,y=360,height=35,width=100)

def DropAdminMethode():
        if (DropAdmin.get() !=""):
            sql = "SELECT * FROM adminregister WHERE name=%s"
            mycursor.execute(sql, (DropAdmin.get(),))
            result = mycursor.fetchall()
            if result:
                 

                SQL="DELETE FROM adminregister  WHERE name=%s"
                mycursor.execute(SQL,(DropAdmin.get(),))
                mydb.commit()  
                messagebox.showinfo("Message Box","Drop Task Sucessfully")
            else:
                 messagebox.showinfo("Message Box", "Nothing this person data in here")
                     
        else:
            messagebox.showinfo("Message Box", "Can't Perform Task")
        DropAdmin.delete(0, tk.END)       

def DeactiveAdminMethod():
        
        if(DeactiveAdmin.get() !=""):
            sql = "SELECT * FROM adminregister WHERE name=%s"
            mycursor.execute(sql, (DeactiveAdmin.get(),))
            result = mycursor.fetchall()
            if result:

                sql = "SELECT * FROM adminregister WHERE name=%s"
                mycursor.execute(sql, (DeactiveAdmin.get(),))
                result = mycursor.fetchall()
                for row in result:
                    sql = "INSERT INTO TempAdminRegi (name, position, password) VALUES (%s, %s, %s)"
                    mycursor.execute(sql, (row[1], row[2], row[3]))
                    mydb.commit() 

                SQL = "DELETE FROM adminregister WHERE name=%s"
                mycursor.execute(SQL, (DeactiveAdmin.get(),))
                mydb.commit()
                messagebox.showinfo("Message Box","De-Activate Task Sucessfully")

            else:
                 messagebox.showinfo("Message Box", "Nothing this person data in here")
                 

        else:
            messagebox.showinfo("Message Box", "Can't Perform Task")
        DeactiveAdmin.delete(0, tk.END)    
    
   


def SNotification():
  
    global   result
    Tableframe=tk.Frame(root)
    Tableframe.place(height=400,width=500)
    sql="select * from TempAdminRegi"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    len=0
    
   
    for row in result:
        len=len+40
        Label(Tableframe,text="Name is:"+row[1]+"Position is :"+row[2],bg="red").place(width=300,height=30,x=0,y=len)
        
    

     
    #first row 
    Button(Tableframe,text="Activate",bg="#2ecc71",command=ACTIVATE1).place(height=30,width=70,x=340,y=40)
    
    Button(Tableframe,text="Delete",bg="#bdc3c7",command=DELETEBTN1).place(height=30,width=70,x=420,y=40)
   

    #second row
    Button(Tableframe,text="Activate",bg="#2ecc71",command=ACTIVATE2).place(height=30,width=70,x=340,y=80)
    
    Button(Tableframe,text="Delete",bg="#bdc3c7",command=DELETEBTN2).place(height=30,width=70,x=420,y=80)
    
    
    #third row
    Button(Tableframe,text="Activate",bg="#2ecc71",command=ACTIVATE3).place(height=30,width=70,x=340,y=120)
  
    Button(Tableframe,text="Delete",bg="#bdc3c7",command=DELETEBTN3).place(height=30,width=70,x=420,y=120)
   
    
    #fourth row
    Button(Tableframe,text="Activate",bg="#2ecc71",command=ACTIVATE4).place(height=30,width=70,x=340,y=160)
    
    Button(Tableframe,text="Delete",bg="#bdc3c7",command=DELETEBTN4).place(height=30,width=70,x=420,y=160)
    
    
    #fifth row
    Button(Tableframe,text="Activate",bg="#2ecc71",command=ACTIVATE5).place(height=30,width=70,x=340,y=200)

    Button(Tableframe,text="Delete",bg="#bdc3c7",command=DELETEBTN5).place(height=30,width=70,x=420,y=200)

    btnSback=Button(Tableframe,text="Back",bg="LightCoral" ,border="0",command=SuperFrame,font=('bold'))
    btnSback.place(x=200,y=360,height=35,width=100)
#--------------------------------------------------------- delete the admin from tempory table--------------------------   
def DELETEBTN1():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        first_row = result[0]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(first_row [0] ),))
        mydb.commit()    

def DELETEBTN2():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        second_row = result[1]
        print(second_row[0])
        SQL = "DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL, (int(second_row[0]),)) 

        
        mydb.commit() 

def DELETEBTN3():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        third_row = result[2]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(third_row[0] ),))
        mydb.commit()      

def DELETEBTN4():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        forth_row = result[3]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(forth_row[0] ),))
        mydb.commit()      

def DELETEBTN5():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        fifth_row = result[4]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(fifth_row[0] ),))
        mydb.commit()                 

#-----------------------------------------------------activate admin-------------------------------
def ACTIVATE1():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        row= result[0]
        sql = "INSERT INTO adminregister (name, position,password) VALUES (%s, %s,%s)"
        mycursor.execute(sql,(row[1],row[2],row[3]))
        mydb.commit()   
        
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        first_row = result[0]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(first_row [0] ),))
        mydb.commit()    


     

def ACTIVATE2():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        row= result[1]
        sql = "INSERT INTO adminregister (name, position,password) VALUES (%s, %s,%s)"
        mycursor.execute(sql,(row[1],row[2],row[3]))
        mydb.commit()   
        
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        second_row = result[1]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(second_row [0] ),))
        mydb.commit()   

def ACTIVATE3():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        row= result[2]
        sql = "INSERT INTO adminregister (name, position,password) VALUES (%s, %s,%s)"
        mycursor.execute(sql,(row[1],row[2],row[3]))
        mydb.commit()   
        
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        third_row = result[2]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(third_row [0] ),))
        mydb.commit()   

def ACTIVATE4():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        row= result[3]
        sql = "INSERT INTO adminregister (name, position,password) VALUES (%s, %s,%s)"
        mycursor.execute(sql,(row[1],row[2],row[3]))
        mydb.commit()   
        
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        forth_row = result[3]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(forth_row [0] ),))
        mydb.commit()   


def ACTIVATE5():
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        row= result[4]
        sql = "INSERT INTO adminregister (name, position,password) VALUES (%s, %s,%s)"
        mycursor.execute(sql,(row[1],row[2],row[3]))
        mydb.commit()   
        
    sql = "SELECT * FROM TempAdminRegi"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if len(result) > 0:
        fifth_row = result[4]
        SQL="DELETE FROM TempAdminRegi WHERE id=%s"
        mycursor.execute(SQL,(int(fifth_row [0] ),))
        mydb.commit()   


    
    

    

       
  
  
def SRegister():
  global SuperName
  global SuperPW1
  global SuperPW2

  
  #create notification and register perfrom frame
  SuperRegi=tk.Frame(root)
  SuperRegi.place(height=350,width=500,x=0,y=50)

  class LimitedEntry(tk.Entry):
            def __init__(self, master=None, limit=10, **kwargs):
                super().__init__(master, **kwargs)

                self.limit = limit
                self['validate'] = 'key'
                self['validatecommand'] = (self.register(self.validate_text), '%P')
                
            def validate_text(self, new_text):
                return len(new_text) <= self.limit

  Label(SuperRegi,text="Enter Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=40)
  SuperName=Entry(SuperRegi,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
  SuperName.place(x=100,y=60,height=35,width=300)
        
        
        
  Label(SuperRegi,text="Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=95)
  SuperPW1=LimitedEntry(SuperRegi,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
  SuperPW1.place(x=100,y=115,height=35,width=300)

  Label(SuperRegi,text="Re Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=150)
  SuperPW2=LimitedEntry(SuperRegi,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
  SuperPW2.place(x=100,y=170,height=35,width=300)
          

  Button(SuperRegi,text="Submit",font=('bold'),bg="Orange",width=20,border="0",command=SuperRegiFrame).place(x=100,y=220,height=35,width=300)
  Button(SuperRegi,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=SuperFrame).place(x=200,y=310,height=35,width=100)



def SuperRegiFrame():
    if ((SuperName.get()!= "")and(SuperPW1.get()!="")and(SuperPW2.get()!="")):

      if(SuperPW1.get()!=SuperPW2.get()):
        messagebox.showinfo("Message Box", "Invalide Password Re Enter It Again")
        SuperPW1.delete(0,tk.END)
        SuperPW2.delete(0,tk.END)
      else:  
        sql = "INSERT INTO SuperAdminRegi (name,password) VALUES (%s, %s)"
        mycursor.execute(sql,(SuperName.get(), SuperPW1.get()))
        mydb.commit()
        messagebox.showinfo("Message Box", "Insert Data Sucessfully")
        SuperName.delete(0,tk.END)
        SuperPW1.delete(0,tk.END)
        SuperPW2.delete(0,tk.END)

        #SQL="DELETE FROM SuperAdminRegi WHERE id=1"
        #mycursor.execute(SQL)
        #mydb.commit()
    else:
       messagebox.showinfo("Message Box", "Not Data Add Sucessfully")

  






#create Admin Loginframe
def Adminfrom():
    global euser
    global  epassword
    
    global decrypted_message
    
    Adminframe=Frame(root,bg="white")
    Adminframe.place(height=400,width=500)
    

    Adminlogin=Label(Adminframe,text="Login Form For",bg="white",font=("Monaco",18,"bold")).place(x=140,y=10)
    Adminlogin=Label(Adminframe,text=" Admin",bg="white",font=("Monaco",18,"bold")).place(x=200,y=40)
    class LimitedEntry(tk.Entry):
        def __init__(self, master=None, limit=10, **kwargs):
            super().__init__(master, **kwargs)

            self.limit = limit
            self['validate'] = 'key'
            self['validatecommand'] = (self.register(self.validate_text), '%P')
            
        def validate_text(self, new_text):
            return len(new_text) <= self.limit


    Label(Adminframe,bg="white",text="Enter User Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=90)
    euser=LimitedEntry(Adminframe,border="0",bg="Gainsboro",justify=tk.CENTER,limit=10)
    euser.place(x=100,y=110,height=35,width=300)

    Label(Adminframe,bg="white",text="Enter Password",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=145)
    epassword=Entry(Adminframe,border="0",bg="Gainsboro",justify=tk.CENTER,show="*")
    epassword.place(x=100,y=165,height=35,width=300)

    
    
    

   
    

    btnlogin=Button(Adminframe,bg="Orange",text="Login",border="0",command=Loginbtn,font=('bold')  )
    btnlogin.place(x=100,y=260,height=35,width=300,)

    
    

    btnRgi=Button(Adminframe,bg="Cyan",text="Register" ,border="0",command=AdminRgiForm,font=('bold'))
    btnRgi.place(x=100,y=310,height=35,width=300)
    btnRgiback=Button(Adminframe,text="Back",bg="LightCoral" ,border="0",command=MainFrame,font=('bold'))
    btnRgiback.place(x=200,y=360,height=35,width=100)
    
STvar = StringVar()
#set Admin login Button
def Loginbtn():
     
        
        query1 = "SELECT name,password FROM AdminRegister WHERE name=%s and password=%s"
        
        mycursor.execute(query1,(euser.get(),epassword.get()))
        result = mycursor.fetchall()

    # -------------------------------------------------------start the admin performance area-----------------------------------------------------

        if result: 
            AframemM=Frame(root)
            AframemM.place(height=400,width=500)






            #Create Admin Login Interface
            def AdminGUI():

            
                global  Esid
                global Etid
                global date_string
                

                img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((500,500)))
                lable1=Label(AframemM,image=img)
                Label.img=img
                lable1.place(height=400,width=500)

                Adminframem1=Frame(AframemM,bg="white",border="0")
                Adminframem1.place(height=230,width=350,x=75,y=100)
                    

                Button(Adminframem1,text="User Register ",font=("bold"),bg="Aqua",border="0",command=UserRegi).place(x=105,y=10,height=50,width=150)
                    


                Button(Adminframem1,text="Delete Student ID",bg="Crimson",border="0",command=DeleteSid).place(x=25,y=75,height=35,width=200)
                Button(Adminframem1,text="Delete Teacher ID",bg="Crimson",border="0",command=DeleteTid).place(x=25,y=115,height=35,width=200)
                
                Esid=Entry(Adminframem1,border="1",bg="Gainsboro",justify=tk.CENTER)
                Esid.place(x=255,y=75,height=35,width=70)
                Etid=Entry(Adminframem1,border="1",bg="Gainsboro",justify=tk.CENTER)
                Etid.place(x=255,y=115,height=35,width=70)
                Button(Adminframem1,text="Show Tables",bg="orange",border="0",command=newframe).place(x=25,y=160,height=35,width=80)
                Button(Adminframem1,text="Report",bg="orange",border="0",command=Report).place(x=135,y=160,height=35,width=80)
                Button(Adminframem1,text="Sent Mail",bg="orange",border="0",command=SentEmailStudent).place(x=245,y=160,height=35,width=80)

                

                
                Button(AframemM,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=loginmain).place(x=200,y=360,height=35,width=100)


            #admin can delete student id

            def DeleteSid():
                if(Esid.get()!=""):
                    #get student table name to comfirm to delete data
                    query = "SELECT name FROM student WHERE idnum = %s"
                    mycursor.execute(query, (Esid.get(),))
                    row =  mycursor.fetchone()
                    result = messagebox.askyesno("Alart", "Are You Sure !,Delete This Row"+" Student Name Is: "+row[0])

                    # check the user's response
                    if result == True:
                        query="SELECT * FROM student WHERE idnum = %s "
                        mycursor.execute(query, (Esid.get(),))
                        data = mycursor.fetchall()

                        for row in data:
                            sqlboth = "INSERT INTO  DeleteStudentRecord (name,idnum,email,qrcode) VALUES (%s, %s,%s,%s)"
                            val = (row[1],row[2],row[3],row[4])
                            mycursor.execute(sqlboth, val)
                            mydb.commit()
                        # define the SQL statement to delete a row
                        sql = "DELETE FROM student WHERE idnum= %s"


                        # specify the value to be deleted
                        val = ( str(Esid.get()),)
                    

                        # execute the SQL statement
                        mycursor.execute(sql,val)

                        # commit the changes to the database
                        mydb.commit()
                        if mycursor.rowcount > 0:
                            messagebox.showinfo("Message Box", "Delete Data Row Sucessfully")
                        


                    else:
                        messagebox.showinfo("Message Box", "Can't Perform Task")
                        
                    
                    Esid.delete(0, tk.END)
                    
                else:
                    messagebox.showinfo("Message Box", "Can't Perform Task")


            #admin can delete teacher id

            def DeleteTid():
                if(Etid.get()!=""):
                    query = "SELECT name FROM teacher WHERE idnum = %s"
                    mycursor.execute(query, (Etid.get(),))
                    row =  mycursor.fetchone()

                    result = messagebox.askyesno("Alart", "Are You Sure !,Delete This Row"+" Teacher Name Is: "+row[0])

                    
                    if result == True:
                        query="SELECT * FROM teacher WHERE idnum = %s "
                        mycursor.execute(query, (Etid.get(),))
                        data = mycursor.fetchall()

                        for row in data:
                            sqlboth = "INSERT INTO  DeleteTeacherRecord (name,idnum,email,qrcode) VALUES (%s, %s,%s,%s)"
                            val = (row[1],row[2],row[3],row[4])
                            mycursor.execute(sqlboth, val)
                            mydb.commit()

                    
                        
                        sql = "DELETE FROM teacher WHERE idnum= %s"
 
                        val = ( str(Etid.get()),)
                        mycursor.execute(sql,val)
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            messagebox.showinfo("Message Box", "Delete Data Row Sucessfully")

                    else:
                        messagebox.showinfo("Message Box", "Can't Perform Task")
                        Etid.delete(0, tk.END)
                
                else:
                    messagebox.showinfo("Message Box", "Can't Perform Task")       








                

            #show data base table it contain student and teacher register data
            def newframe():
                newframe=Frame(AframemM)
                newframe.place(height=400,width=500)
                Label(newframe,text="Student Table",font=("Monaco",18,"bold")).pack()
                mycursor.execute("SELECT id,name,idnum,email FROM student")
                records = mycursor.fetchall()

                
                # Add the records to a Tkinter listbox in the frame
                listbox = tk.Listbox(newframe,width=200)
                for record in records:
                    listbox.insert(tk.END, record)
                listbox.pack()

                Label(newframe,text="Teacher Table",font=("Monaco",18,"bold")).pack()
                mycursor.execute("SELECT id,name,idnum,email FROM teacher")
                records = mycursor.fetchall()

                
                # Add the records to a Tkinter listbox in the frame
                listbox = tk.Listbox(newframe,width=200)
                for record in records:
                    listbox.insert(tk.END, record)
                listbox.pack()

                Button(newframe,text="Back",bg="LightCoral" ,border="0",command=AdminGUI,font=('bold')).place(x=200,y=360,height=35,width=100)
            
            #sent Email to principle including report of teacher and student(Report Both)

            #---------------------------this aREA FOR REPOT FRAME----------------------------

            def Report():
                
                global temp1
                global date_picker
                
                ReportFrame=tk.Frame(AframemM)
                ReportFrame.place(height=400,width=500)
                

                Label(ReportFrame,text="Report",font=("Monaco",20,"bold")).place(x=200,y=10)
            

                        
                
                Label(ReportFrame,text="Selectd A Day You Want To Get Report").place(x=50,y=50)
                date_picker = DateEntry(ReportFrame , width=12, background='darkblue',foreground='white', borderwidth=2)
                date_picker.place(x=150,y=70)
                selected_date = date_picker.get_date()
                date_string = selected_date.strftime('%Y-%m-%d')
                print(date_string)

                Label(ReportFrame,text="Select Type").place(x=50,y=100)
                R1 = Radiobutton(ReportFrame, text="Teacher", variable=STvar, value="teacher",font=("Helvetica (sans-serif)",10,"bold")).place(x=150,y=120)
                R1  =Radiobutton(ReportFrame, text="Student", variable=STvar, value="student",font=("Helvetica (sans-serif)",10,"bold")).place(x=150,y=140)
                # ----GET VALUES--
                
                
                tk.Button(ReportFrame, text="View Data",bg="Cyan",command=ViewDataFrame).place(x=200,y=260,width=100,height=35)

                tk.Button(ReportFrame, text="Get Email",bg="Cyan",command=reportprinciple).place(x=200,y=300,width=100,height=35)

                btnSback=Button(ReportFrame,text="Back",bg="LightCoral" ,border="0",font=('bold'),command=AdminGUI)
                btnSback.place(x=200,y=360,height=35,width=100)


            def ViewDataFrame():
                selected_date = date_picker.get_date()
                date_string = selected_date.strftime('%Y-%m-%d')
                print(date_string)
                temp1=str(STvar.get())
                ViewData=Frame(AframemM)
                ViewData.place(height=400,width=500)
                if temp1=='student':              
                    print(date_string)
                    Label(ViewData,text="View Data",font=("Monaco",18,"bold")).pack()
                    data="SELECT * FROM userLog WHERE dateoflog = %s and keyname='Student'"
                    mycursor.execute(data, (date_string,))
                                
                    recordstudent = mycursor.fetchall()

                                
                    # Add the student records to a Tkinter listbox in the frame
                    listbox = tk.Listbox(ViewData,width=200)
                    for record in recordstudent:
                        listbox.insert(tk.END, record)
                    listbox.place(x=0,y=50)
                else:
                    print(date_string)
                    Label(ViewData,text="View Data",font=("Monaco",18,"bold")).pack()
                    data = "SELECT * FROM userLog WHERE dateoflog = %s and keyname='Teacher' "
                    mycursor.execute(data, (date_string,))
                    recordteacher = mycursor.fetchall()

                                
                    # Add the teacher records to a Tkinter listbox in the frame
                    listbox = tk.Listbox(ViewData,width=200)
                    for record in recordteacher:
                        listbox.insert(tk.END, record)
                    listbox.place(x=0,y=50)

                Button(ViewData,text="Back",bg="LightCoral" ,border="0",command=Report,font=('bold')).place(x=200,y=360,height=35,width=100)
                            
                



                



            #we can choose your Admin or Supper Aadmin by this Frame
            def reportprinciple():
                    selected_date = date_picker.get_date()
                    date_string = selected_date.strftime('%Y-%m-%d')
                    temp1=str(STvar.get())

                # Set up the email message
                    msg = MIMEMultipart()
                    msg['From'] = 'myproject19990416@gmail.com'
                    msg['To'] = 'janithchamodya99@gmail.com'
                    msg['Subject'] = 'Today Report of Teachers And Students'

                # Add text to the message
                    body = 'This is a Report of Today Our School.'
                    msg.attach(MIMEText(body, 'plain'))

                    #report generated for student
                    if (temp1=='student'):
                    
                        query = "SELECT * FROM userLog WHERE dateoflog = %s and keyname='Student' "
                        mycursor.execute(query, (date_string,))
                        rows = mycursor.fetchall()
                        # Format te report as a string
                        reportStudent = "Id\tName\tIdnum\t\tEmail\t\t\t\tDate\t\tTime\n"
                        for row in rows:
                            reportStudent += f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n"

                        # Add the report of student as a plain text attachment
                        attachment = MIMEText(reportStudent)
                        attachment.add_header('Content-Disposition', 'attachment', filename='reportStudent.txt')
                        msg.attach(attachment)
                            
                    else:
                        #report generated for teacher
                        query = "SELECT * FROM userLog WHERE dateoflog = %s and keyname='Teacher' "
                        mycursor.execute(query, (date_string,))
                        rows = mycursor.fetchall()

                        # Format te report as a string
                        reportTeacher = "Id\tName\tIdnum\t\tEmail\t\t\t\tDate\t\tTime\n"
                        for row in rows:
                            reportTeacher += f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n"         
                                        
                        # Add the report of teacher as a plain text attachment
                        attachment = MIMEText(reportTeacher)
                        attachment.add_header('Content-Disposition', 'attachment', filename='reportTeacher.txt')
                        msg.attach(attachment)

                    # Connect to the SMTP server and send the message
                    smtp_server = 'smtp.gmail.com'
                    smtp_port = 587
                    username = 'myproject19990416@gmail.com'
                    password = 'cyyoxhlppzwwapkj'
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(username, password)
                        server.sendmail(username, 'janithchamodya99@gmail.com', msg.as_string())
                



            #sent email to not particaipate student to school
            def SentEmailStudent():
                
                # Create a SQL query to join the tables and filter the rows
                query = "SELECT student.email FROM student LEFT JOIN studentlog ON student.idnum = studentlog.idnum WHERE studentlog.idnum IS NULL"

                # Execute the query
                mycursor.execute(query)

                # Fetch the results
                results = mycursor.fetchall()

                for result in results:
                    email = result[0] 
                    print(email)
                    # Set up the email message
                    msg = MIMEMultipart()
                    msg['From'] = 'myproject19990416@gmail.com'
                    msg['To'] = email
                    msg['Subject'] = 'Today You Not Participate To School'

                    # Add text to the message
                    body = 'This is a Alert for you.'
                    msg.attach(MIMEText(body, 'plain'))

                        

                    # Connect to the SMTP server and send the message
                    smtp_server = 'smtp.gmail.com'
                    smtp_port = 587
                    username = 'myproject19990416@gmail.com'
                    password = 'cyyoxhlppzwwapkj'
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(username, password)
                        server.sendmail(username, email, msg.as_string())


        
            def UserRegi():
                Both=Frame(AframemM)
                Both.place(height=400,width=500)
                var = StringVar()


                def InsertBoth():
                    global img

                    temp=str(var.get())
                    if(temp=="student"):
                        
                    
                        if((Bothuser.get()!= "")and(Bothid.get()!="")and(Bothemail.get()!="")):
                            data = Bothid.get()
                            qr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=4,)
                            qr.add_data(data)
                            qr.make(fit=True)
                            img = qr.make_image(fill_color="black", back_color="white")
                            width, height = img.size
                            
                            buffer = io.BytesIO()
                            
                            #when image saving in python we need to it  convert as byte code (use ----ByteIo class---)
                            #and get it value 
                            #           ByteIo.getvalue()
                            img.save(buffer, format="PNG")
                            #getvalue() funtion take value from buffer as a string
                            qr_code_data = buffer.getvalue()
                            #img.show()


                            
                            
#cam start----------------------------------------------------------------------------------------------------------------------------------
                            
                            cam = cv2.VideoCapture(0)
                            cam.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
                            cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
                            while True:
                                ret, frame = cam.read()

                                if not ret:
                                    print("Error capturing the frame")
                                    break

                                cv2.imshow("Hey!Buddies Smile...", frame)

                                key = cv2.waitKey(1)
                                if key == 27:  # Press ESC to exit
                                    break
                                elif key == 32:  # Press SPACE to capture and insert the image
                                    img_name = "1.jpg"
                                    cv2.imwrite(img_name, frame)

                                    # Read the captured image as binary data
                                    with open(img_name, "rb") as img_file:
                                        image_data = img_file.read()

                                    result = messagebox.askyesno("Alart", "Are You Sure !,Add This Photo")
                                    if result:
                                        
                                        sqlboth = "INSERT INTO  student (name,idnum,email,qrcode,image) VALUES (%s, %s,%s,%s,%s)"
                                        val = (Bothuser.get(), Bothid.get(),Bothemail.get(),qr_code_data,image_data)
                                        mycursor.execute(sqlboth, val)
                                        mydb.commit()
                                        
                                        folder_name = Bothuser.get()
                                        folder_path = os.path.join("C:\\project\\images", folder_name)

                                        # Create the folder
                                        os.makedirs(folder_path, exist_ok=True)

                                        # Assuming you have the frame variable containing the image frame

                                        image_path = os.path.join(folder_path, "1.jpg")

                                        # Save the image
                                        cv2.imwrite(image_path, frame)

                                        print("Image inserted successfully.")
                                        messagebox.showinfo("Message Box", "Insert Data Sucessfully")
                                    else:
                                        messagebox.showinfo("Take Another Photo")    

                           
                            cam.release()
                            cv2.destroyAllWindows()

                            
#cam stop---------------------------------------------------------------------------------------------------------------------------------------
                            
                            

                            
                        else: 
                            messagebox.showinfo("Message Box", "Not Data Add Sucessfully")

                    else:
                        if((Bothuser.get()!= "")and(Bothid.get()!="")and(Bothemail.get()!="")):
                            data = Bothid.get()
                            qr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=4,)
                            qr.add_data(data)
                            qr.make(fit=True)
                            img = qr.make_image(fill_color="black", back_color="white")
                            width, height = img.size
                            
                            buffer = io.BytesIO()
                            img.save(buffer, format="PNG")
                            qr_code_data = buffer.getvalue()
                            #img.show()

#cam start----------------------------------------------------------------------------------------------------------------------------------
                            
                            
                            cam = cv2.VideoCapture(0)
                            cam.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
                            cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
                           
                            
                            while True:
                                ret, frame = cam.read()
                                


                                if not ret:
                                    print("Error capturing the frame")
                                    break

                                cv2.imshow("Hey!Buddies Smile...", frame)

                                key = cv2.waitKey(1)
                                if key == 27:  # Press ESC to exit
                                    break
                                elif key == 32:  # Press SPACE to capture and insert the image
                                    img_name = "1.jpg"
                                    cv2.imwrite(img_name, frame)

                                    # Read the captured image as binary data
                                    with open(img_name, "rb") as img_file:
                                        image_data = img_file.read()

                                    result = messagebox.askyesno("Alart", "Are You Sure !,Add This Photo")
                                    if result:
                                        
                                        sqlboth = "INSERT INTO  teacher (name,idnum,email,qrcode,image) VALUES (%s, %s,%s,%s,%s)"
                                        val = (Bothuser.get(), Bothid.get(),Bothemail.get(),qr_code_data,image_data)
                                        mycursor.execute(sqlboth, val)
                                        mydb.commit()

                                        folder_name = Bothuser.get()
                                        folder_path = os.path.join("C:\\project\\images", folder_name)

                                        # Create the folder
                                        os.makedirs(folder_path, exist_ok=True)

                                        # Assuming you have the frame variable containing the image frame

                                        image_path = os.path.join(folder_path)

                                        # Save the image
                                        cv2.imwrite(image_path, frame)

                                        print("Image inserted successfully.")
                                        messagebox.showinfo("Message Box", "Insert Data Sucessfully")
                                    else:
                                        messagebox.showinfo("Take Another Photo")    

                           
                            cam.release()
                            cv2.destroyAllWindows()

                            
#cam stop---------------------------------------------------------------------------------------------------------------------------------------
                        else: 
                            messagebox.showinfo("Message Box", "Not Data Add Sucessfully")
                        

                
                


                #Student Teacher register
                def BothRegi():
                    global Bothuser
                    global Bothid
                    global Bothemail
                    global R1
                    

                    Label(Both,text="User Register",font=("Monaco",20,"bold")).place(x=150,y=10)
                    
                    R1 = Radiobutton(Both, text="Teacher", variable=var, value="teacher",font=("Helvetica (sans-serif)",10,"bold"))
                    R1.place(x=200,y=40)

                    R1 = Radiobutton(Both, text="Student", variable=var, value="student",font=("Helvetica (sans-serif)",10,"bold"))
                    R1.place(x=200,y=60)
                    
                    
                    

                    Label(Both,text="Enter Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=90)
                    Bothuser=tk.Entry(Both,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
                    Bothuser.place(x=100,y=110,height=35,width=300)
                    

                    Label(Both,text="Enter ID num*",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=145,)
                    Bothid=Entry(Both,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
                    Bothid.place(x=100,y=165,height=35,width=300)
                    
                
                    Label(Both,text="Enter Email",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=200)
                    Bothemail=Entry(Both,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
                    Bothemail.place(x=100,y=220,height=35,width=300)
                    

                    

                    Button(Both,text="Sumbit",font=('bold'),bg="Orange",width=20,border="0",command=InsertBoth).place(x=100,y=280,height=35,width=300) 
                    
                    
                    Button(Both,text="Get QR",font=('bold'),bg="Orange",width=20,border="0",command=getQR).place(x=100,y=320,height=35,width=300)
                    Button(Both,text="Back",bg="LightCoral" ,border="0",command=AdminGUI,font=('bold')).place(x=200,y=360,height=35,width=100)




                #generate qr code
                def getQR():


                    # Set up the email message
                    msg = MIMEMultipart()
                    msg['From'] = 'myproject19990416@gmail.com'
                    msg['To'] = Bothemail.get()
                    msg['Subject'] = 'QR Code'

                    # Add text to the message
                    body = 'This your QR Code,thank you got our services '+Bothuser.get()
                    msg.attach(MIMEText(body, 'plain'))

                    # Add an image to the message
                    qr_buf = BytesIO()
                    img.save(qr_buf, format='PNG')
                    qr_attachment = MIMEBase('application', 'octet-stream')
                    qr_attachment.set_payload(qr_buf.getvalue())
                    encoders.encode_base64(qr_attachment)
                    qr_attachment.add_header('Content-Disposition', f'attachment; filename="qrcode.png"')
                    msg.attach(qr_attachment)

                    #Connect to server
                    smtp_server = 'smtp.gmail.com'
                    smtp_port = 587
                    username = 'myproject19990416@gmail.com'
                    password = 'cyyoxhlppzwwapkj'
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(username, password)
                        server.sendmail(username, Bothemail.get(), msg.as_string())

                    Bothid.delete(0, tk.END)
                    Bothemail.delete(0, tk.END)
                    Bothuser.delete(0, tk.END)



                BothRegi()                 
            UserRegi()        
            
            AdminGUI()
            
        else:
            messagebox.showinfo("Invalid","Check Again Password And username")
            
        
    
   

    



#---------------------------------------------------------create Admin Registration Form------------------------------------------------------
#enter user name,enter password ,enter spacial password this lable we can see in this 

def AdminRgiForm():
    
    regiFrame=Frame(root)
    regiFrame.place(height=400,width=500)





    #Admin Register Data Sent database
    def regiinsert():
        if(regipassword1.get()!=regipassword2.get()):
            messagebox.showinfo("Message Box", "Invalide Password Re Enter It Again")
        else:
            
            if ((regiuser.get()!= "")and(regipassword2.get()!="")and(regipassword1.get()!="")and( regiposition.get()!="")):


                sql = "INSERT INTO TempAdminRegi (name, position,password) VALUES (%s, %s,%s)"
                
                mycursor.execute(sql,(regiuser.get(), regiposition.get(),regipassword2.get()))
                mydb.commit()


                

                
                
                messagebox.showinfo("Message Box", "Insert Data Sucessfully")
                regiuser.delete(0, tk.END)
                regipassword1.delete(0, tk.END)
                regipassword2.delete(0, tk.END)
                regiposition.delete(0,tk.END)

                
            else:
                messagebox.showinfo("Message Box", "Not Data Add Sucessfully")
                regiuser.delete(0, tk.END)
                regipassword1.delete(0, tk.END)
                regipassword2.delete(0, tk.END)
                regiposition.delete(0,tk.END)
           
            
        



    #Admin Rgister Form     
    def AdminRegi():
        global  regiuser
        global  regiposition
        global  regipassword1
        global  regipassword2
        
        global encrypted_message

        Label(regiFrame,text="Admin Registration",font=("Monaco",18,"bold")) .place(x=120,y=10)
        Label(regiFrame,text="Form",font=("Monaco",18,"bold")).place(x=220,y=40)

        class LimitedEntry(tk.Entry):
            def __init__(self, master=None, limit=10, **kwargs):
                super().__init__(master, **kwargs)

                self.limit = limit
                self['validate'] = 'key'
                self['validatecommand'] = (self.register(self.validate_text), '%P')
                
            def validate_text(self, new_text):
                return len(new_text) <= self.limit

        Label(regiFrame,text="Enter Name",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=90)
        regiuser=Entry(regiFrame,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
        regiuser.place(x=100,y=110,height=35,width=300)
        
        Label(regiFrame,text="Enter Position Her/Him",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=145)
        regiposition=Entry(regiFrame,bg="Gainsboro",border="0",width=30,justify=tk.CENTER)
        regiposition.place(x=100,y=165,height=35,width=300)
        
        Label(regiFrame,text="Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=200)
        regipassword1=LimitedEntry(regiFrame,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
        regipassword1.place(x=100,y=220,height=35,width=300)

        Label(regiFrame,text="RE Enter Paswword",font=("Helvetica (sans-serif)",10,"bold")).place(x=100,y=255)
        regipassword2=LimitedEntry(regiFrame,bg="Gainsboro",border="0",width=30,justify=tk.CENTER,limit=10,show="*")
        regipassword2.place(x=100,y=275,height=35,width=300)
        

        
        

        Button(regiFrame,command=regiinsert,text="Submit",font=('bold'),bg="Orange",width=20,border="0").place(x=100,y=320,height=35,width=300)
       
        Button(regiFrame,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=Adminfrom).place(x=200,y=360,height=35,width=100)
        
        
    
    AdminRegi()
    
#-------------------------------------------------------start student performance area ---------------------------------------------------------    
 #student can use qr scanner or face recognizer to log

def student():
    StdRecognizer=Frame(root)
    StdRecognizer.place(height=400,width=500)

    #get current date
    date_obj= datetime.today().strftime('%Y-%m-%d')



    #Create Student Recognizer
    def StdentRecognizer():
    
        img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((500,500)))
        lable1=Label(StdRecognizer,image=img)
        Label.img=img
        lable1.place(height=400,width=500)

        StdRecognizermini=Frame(StdRecognizer,bg="white",border="0")
        StdRecognizermini.place(height=200,width=350,x=75,y=100)

        jj=Label(StdRecognizermini,text="Student Recognizer",font=("bold"),bg="Aqua",border="0").place(x=100,y=10,height=50,width=150)

        Button(StdRecognizermini,text="Face",bg="Crimson",border="0",font=("verdana",10,"bold"),command=facescan).place(x=75,y=75,height=35,width=200)
        Button(StdRecognizermini,text="QR Code",bg="Crimson",border="0",font=("verdana",10,"bold"),command=qrcode).place(x=75,y=125,height=35,width=200)

        Button(StdRecognizer,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=loginmain).place(x=200,y=360,height=35,width=100)
#face recognzier
    def facescan():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("jpg") or file.endswith("png"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                    #print(label, path)
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    #print(label_ids)
                    #y_labels.append(label) # some number
                    #x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
                    pil_image = Image.open(path).convert("L") # grayscale
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.Resampling.LANCZOS)
                    image_array = np.array(final_image , "uint8")
                    #print(image_array)
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for (x,y,w,h) in faces:
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)


        #print(y_labels)
        #print(x_train)

        with open("face-labels.pickle", 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("face-trainner.yml")

        #face cam start
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
        smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face-trainner.yml")

        labels = {"person_name": 1}
        with open("face-labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}   

            
            
        # Capture video from webcam
        cap = cv2.VideoCapture(0)

        while (True):
            # Read the frame
            ret, frame = cap.read()

            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # Draw rectangle around each face
            for (x, y, w, h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray)  
                
                if conf>= 4 and conf<=85:
                    #print(id_)
                    #print(labels[id_])
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color =(255,255,255)
                    stroke = 2
                    cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

                #create image by web cam
                #img_item = "5.png"
                #cv2.imwrite(img_item, roi_color)
            
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                #detct smile

                #smile = smile_cascade.detectMultiScale(roi_gray)
                #for (sx,sy,sw,sh) in smile:
                # cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(255,255,255),2)
                
                
                #detct eyes

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)

                    



            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Exit if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture
        cap.release()     

#qr code scan
    def qrcode():
        global valname
        
        
        
        #get current time
        current_time = time.strftime("%H:%M:%S")

        cap = cv2.VideoCapture(0)
        

        # Decode the QR code
        
        while True:
            ret, frame = cap.read()
            if ret:
                for i in decode(frame):
                    qr_data = i.data.decode()
                    
                    
                        
                    query = "SELECT name,idnum,email FROM student WHERE idnum = %s "
                    mycursor.execute(query, (qr_data,))
                    result = mycursor.fetchone()
                        
                            #Check the data(if this user are student or not) to add studentlog data table
                    if  result:
                        current_time = time.strftime("%H:%M:%S")
                        queryget="SELECT idnum FROM studentlog WHERE idnum=%s"
                        mycursor.execute(queryget,(qr_data,))
                        resultget=mycursor.fetchone()
                        if resultget:
                                messagebox.showinfo("Message","All Ready Scan The This QR CODE")
                        else:
                            messagebox.showinfo("Message","Confirm QR Code")
                            sql = "INSERT INTO studentLog (name,idnum,email,dateoflog,timeoflog) VALUES (%s, %s,%s,%s,%s)"
                            val = ( result[0],result[1],result[2],date_obj, current_time )
                            mycursor.execute(sql, val)
                            mydb.commit()

                                #add data to userlog table for when delete the data from studentlog daily ,we can get past/old
                                # data any time .creating this userlog table
                            sql = "INSERT INTO userLog (name,idnum,email,dateoflog,timeoflog,keyname) VALUES (%s, %s,%s,%s,%s,%s)"
                            val = ( result[0],result[1],result[2],date_obj, current_time,"Student" )
                            mycursor.execute(sql, val)
                            mydb.commit() 
                        


                            

                         

                    else:
                            pygame.init()
                                
                            alert_sound = pygame.mixer.Sound('C:\project\Alert\mixkit-classic-short-alarm-993.wav')
                            alert_sound.set_volume(0.5)
                            alert_sound.play()
                            time.sleep(5)
                            alert_sound.stop()
                            pygame.quit()

                    #except:
                            #messagebox.showinfo("Error"," But It Duplicate entry  for key 'studentlog.PRIMARY")    
                    

                        

                
                #cv2.waitKey(5)
            if keyboard.is_pressed("q"):
                break  

        cap.release()
        cv2.destroyAllWindows()  

    
    



    StdentRecognizer() 


 #-------------------------------------------------------start teacher performance area ---------------------------------------------------------    
 #teacher can use qr scanner or face recognizer to log 

def teacher():
    TeaRecognizer=Frame(root)
    TeaRecognizer.place(height=400,width=500)


    #Create Student Recognizer
    def TeacherRecognizer():
    
    

        img = ImageTk.PhotoImage(Image.open('image\\1.jpg').resize((500,500)))
        lable1=Label(TeaRecognizer,image=img)
        Label.img=img
        lable1.place(height=400,width=500)

        TeaRecognizermini=Frame(TeaRecognizer,bg="white",border="0")
        TeaRecognizermini.place(height=200,width=350,x=75,y=100)

        Label(TeaRecognizermini,text="Teachers Recognizer",font=("bold"),bg="Aqua",border="0").place(x=100,y=10,height=50,width=150)

        Button(TeaRecognizermini,text="Face",bg="Crimson",border="0",font=("verdana",10,"bold"),command=facescan).place(x=75,y=75,height=35,width=200)
        Button(TeaRecognizermini,text="QR Code",bg="Crimson",border="0",font=("verdana",10,"bold"),command=qrcode).place(x=75,y=125,height=35,width=200)

        Button( TeaRecognizer,text="Back",font=('bold'),bg="LightCoral",width=20,border="0",command=loginmain).place(x=200,y=360,height=35,width=100)

    def facescan():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("jpg") or file.endswith("png"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                    #print(label, path)
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    #print(label_ids)
                    #y_labels.append(label) # some number
                    #x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
                    pil_image = Image.open(path).convert("L") # grayscale
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.Resampling.LANCZOS)
                    image_array = np.array(final_image , "uint8")
                    #print(image_array)
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for (x,y,w,h) in faces:
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)


        #print(y_labels)
        #print(x_train)

        with open("face-labels.pickle", 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("face-trainner.yml")

        #face cam start
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
        smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face-trainner.yml")

        labels = {"person_name": 1}
        with open("face-labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}   

            
            
        # Capture video from webcam
        cap = cv2.VideoCapture(0)

        while (True):
            # Read the frame
            ret, frame = cap.read()

            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # Draw rectangle around each face
            for (x, y, w, h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray)  
                
                if conf>= 4 and conf<=85:
                    #print(id_)
                    #print(labels[id_])
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color =(255,255,255)
                    stroke = 2
                    cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

                #create image by web cam
                #img_item = "5.png"
                #cv2.imwrite(img_item, roi_color)
            
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                #detct smile

                #smile = smile_cascade.detectMultiScale(roi_gray)
                #for (sx,sy,sw,sh) in smile:
                # cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(255,255,255),2)
                
                
                #detct eyes

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)

                    



            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Exit if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture
        cap.release()  



    def qrcode():
        global valname

        #get current date
        date_obj= datetime.today().strftime('%Y-%m-%d')
        
        #import time
        cap = cv2.VideoCapture(0)
        cap.set(5,640)
        cap.set(6,480)

        # Decode the QR code
        
        while True:
            ret, frame = cap.read()
            if ret:
                for i in decode(frame):
                    qr_data = i.data.decode()
                    cv2.imshow("QR Code Scanner", frame)
                    
                        # Fetch the data from the database
                    query = "SELECT name,idnum,email FROM teacher WHERE idnum = %s"
                    mycursor.execute(query, (qr_data,))
                    result = mycursor.fetchone()
                        
                        # Compare the data
                    if  result:
                            current_time = time.strftime("%H:%M:%S")

                            queryget="SELECT idnum FROM teacherlog WHERE idnum=%s"
                            mycursor.execute(queryget,(qr_data,))
                            resultget=mycursor.fetchone()
                            if resultget:
                                messagebox.showinfo("Message","All Ready Scan The This QR CODE")
                            else:    
                                messagebox.showinfo("Message","Confirm QR Code")
                                sql = "INSERT INTO teacherLog (name,idnum,email,dateoflog,timeoflog) VALUES (%s, %s,%s,%s,%s)"
                                val = ( result[0],result[1],result[2],date_obj, current_time )
                                mycursor.execute(sql, val)
                                mydb.commit()

                                #add data to userlog table for when delete the data from studentlog daily ,we can get past/old
                                # we can get data any time using this userlog table
                                sql = "INSERT INTO userLog (name,idnum,email,dateoflog,timeoflog,keyname) VALUES (%s, %s,%s,%s,%s,%s)"
                                val = ( result[0],result[1],result[2],date_obj, current_time,"Teacher" )
                                mycursor.execute(sql, val)
                                mydb.commit()

                           
                        

                               
                    else:
                            pygame.init()
                            
                            alert_sound = pygame.mixer.Sound('C:\project\Alert\mixkit-classic-short-alarm-993.wav')
                            alert_sound.set_volume(0.5)
                            alert_sound.play()
                            time.sleep(5)
                            alert_sound.stop()
                            pygame.quit()

                            
                    #except:
                     #       messagebox.showinfo("Error"," But It Duplicate entry  for key 'teacherlog.PRIMARY")    

                        

                
                #cv2.waitKey(5)
            if keyboard.is_pressed("q"):
                break    

        cap.release()
        cv2.destroyAllWindows()  

        

    TeacherRecognizer()
  
     
loginmain()
root.mainloop()