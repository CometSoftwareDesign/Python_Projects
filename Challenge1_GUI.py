
#python gui challenge
import tkinter as tk
from tkinter import *
from tkinter import ttk

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Check files")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()

        
def load_gui(self):
    
#the following is the label being created
       
       self.lbl_browse = tk.Label(self.master,text = 'Browse... ')
       self.lbl_browse.grid(row = 0,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)

       self.lbl_browse2 = tk.Label(self.master,text = 'Browse... ')
       self.lbl_browse2.grid(row = 2,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)


       self.lbl_checkforfiles = tk.Label(self.master,text = 'Check For Files: ')
       self.lbl_checkforfiles.grid(row = 4,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)

       
       self.lbl_CloseProgram = tk.Label(self.master,text = 'Check For Files: ')
       self.lbl_CloseProgram.grid(row = 4,column= 0, padx=(40,0), pady=(30,0),sticky = N+W)




     #the following is the text imput just above the label
       
       self.txt_browse = tk.Entry(self.master,text = ' ')
       self.txt_browse.grid(row = 1, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)

       self.txt_browse2 = tk.Entry(self.master,text = '')
       self.txt_browse2.grid(row = 3, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)


      

     


       
def main(): 
    karl().mainloop()
if __name__ == '__main__':
   pass
