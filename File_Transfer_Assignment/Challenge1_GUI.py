
#python gui challenge
import tkinter as tk
from tkinter import *
from tkinter import ttk

import tkinter as tk
import tkinter.filedialog
from tkinter import filedialog as fd
import datetime
from datetime import *
import os
from os import *
import shutil

class karl(Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.title("Check files")
        self.master.minsize(600,400) #(Height, Width)
        self.master.maxsize(800,500)
        
        self.lbl_browse = tk.Button(self.master,text = 'Browse... ', command = lambda:getsource(self))
        self.lbl_browse.grid(row = 0,column = 1, padx=(27,0), pady=(10,0),sticky = N+W)

        self.lbl_browse2 = tk.Button(self.master,text = 'Browse... ',command = lambda:getdest(self)) #lambda makes sure that the button is called only when clicked
        self.lbl_browse2.grid(row = 1,column= 1, padx =(27,0), pady=(10,0),sticky = N+W)

        self.lbl_checkforfiles = tk.Button(self.master,text = 'Check For Files: ',command =lambda:movefiles(self))
        self.lbl_checkforfiles.grid(row = 3, column = 1, padx=(27,0), pady=(10,0),sticky = N+W)

        self.lbl_CloseProgram = tk.Button(self.master,text = 'Close Program', command = self.master.destroy)                       
        self.lbl_CloseProgram.grid(row = 4, column = 3, padx=(27,0), pady=(10,0),sticky = N+W)

     #the following is the text imput just above the label
       
        self.txt_browse = tk.Entry(self.master, text = ' ',width = 60)
        self.txt_browse.grid(row = 0, column = 3, columnspan = 2 )

        self.txt_browse2 = tk.Entry(self.master, text = '', width = 60)
        self.txt_browse2.grid(row = 1, column = 3,columnspan = 2)
        
# calling fucntions
        def getsource(self):
            name1 = fd.askdirectory()
            self.txt_browse.insert(0,name1)

        def getdest(self):
            name2 = fd.askdirectory()
            self.txt_browse2.insert(0,name2)

        def movefiles(self):
            folder1 =self.txt_browse.get()
            folder2 = self.txt_browse2.get()
            files = os.listdir(folder1)
            for file in files:
               timeA = datetime.now()
               timeB = timeA - timedelta(hours = 24)
               modTime = os.path.getmtime(folder1 +'/'+ file)
               readable = datetime.fromtimestamp(modTime)
               if readable > timeB:
                    shutil.move(folder1 +'/'+ file, folder2)
                    print(file)
                       
               

       
##def main(): 
 ##   karl().mainloop()
       
if __name__ == '__main__':
   root = tk.Tk()
   App = karl(root)
   root.mainloop()
