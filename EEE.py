#!/usr/bin/python3

from UpdateXML import UpdateXMSLoad

from tkinter import *
from tkinter import messagebox

fields = 'User ID', 'Pin'

def ControlValue(entries, control):
    uid = entries[0][1].get()
    pin = entries[1][1].get()
    val=UpdateXMSLoad(uid, pin, control)
    if val=='Done':
        if control=='0':
            controls='Lamp 0 OFF'
        elif control=='1':
            controls='Lamp 0 ON'
        elif control=='2':
            controls='Lamp 1 ON'
        elif control=='3':
            controls='Lamp 1 OFF'
        elif control=='4':
            controls='Lamp 2 ON'
        elif control=='5':
            controls='Lamp 2 OFF'
        else:
            controls='Undefined'            
        cs.configure(text = "Current Status: " + controls)
    else:
        msgerr()
        
def initservice(entries):
    uid = entries[0][1].get()
    pin = entries[1][1].get()
    val=UpdateXMSLoad(uid, pin, '0')
    if val=='Done':
        #msginit()
        csinit()
    else:
        msgerr()
        tservice
def msginit():
    showinfo(title="Answer", message="Initialization done successfully")

def msgerr():
    showerror(title="Answer", message="Failed. Check Internet")

def csinit():
    cs.configure(text = "Current Status: " + str('Initialized'))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=LEFT, expand=NO, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   root.title("Load Control (IoT Based)")
   t1=Label(root, 
		 text="Load Control (IoT Based)",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic")
   t1.pack()
   
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: initservice(e)))   
   bi = Button(root, text='Initialize at First Use', command=(lambda e=ents: initservice(e)))
   bi.pack(side=LEFT, padx=5, pady=5, fill=X)

   b0 = Button(root, text='Lamp 0 OFF', command=(lambda e=ents: ControlValue(e,'0')))
   b0.pack(side=LEFT, padx=5, pady=5, fill=X)

   b1 = Button(root, text='Lamp 0  ON', command=(lambda e=ents: ControlValue(e,'1')))
   b1.pack(side=LEFT, padx=5, pady=5, fill=X)
   
   b2 = Button(root, text='Lamp 1 OFF', command=(lambda e=ents: ControlValue(e,'2')))
   b2.pack(side=LEFT, padx=5, pady=5, fill=X)

   b3 = Button(root, text='Lamp 1 ON', command=(lambda e=ents: ControlValue(e,'3')))
   b3.pack(side=LEFT, padx=5, pady=5, fill=X)

   b4 = Button(root, text='Lamp 2 OFF', command=(lambda e=ents: ControlValue(e,'4')))
   b4.pack(side=LEFT, padx=5, pady=5, fill=X)   

   b5 = Button(root, text='Lamp 2 ON', command=(lambda e=ents: ControlValue(e,'5')))
   b5.pack(side=LEFT, padx=5, pady=5, fill=X)
   
   bq = Button(root, text='Quit', command=root.quit)
   bq.pack(side=LEFT, padx=5, pady=5, fill=X)

   cs = Label(root, width=30, text='Current Status', anchor='w')
   cs.pack(side=LEFT, padx=50, pady=30, fill=X)
   
   root.mainloop()
