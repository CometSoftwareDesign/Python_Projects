import tkinter as tk
from tkinter import *
from tkinter import ttk

import tkinter as tk
import tkinter.filedialog
from tkinter import filedialog as fd
import webbrowser


class karl(Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.title("Create Website")
        self.master.minsize(600,400) #(Height, Width)
        self.master.maxsize(800,500)

        #button that starts the search
        self.lbl_search = tk.Button(self.master,text = 'Create website ', command = lambda:opensite(self))
        self.lbl_search.grid(row = 0,column = 1, padx=(27,0), pady=(10,0),sticky = N+W)

              #entry field for the search
        self.txt_search = tk.Entry(self.master, text = ' ',width = 60)
        self.txt_search.grid(row = 0, column = 3, columnspan = 2 )
#function to get the site to open
        def opensite(self):
               tommy = self.txt_search.get()
               f= open("website.html", "r")
               text = f.write("""<html><body><h1>"""+tommy+"""</h1></body></html> """)
               f.close()
               webbrowser.open("website.html");



if __name__ == '__main__':
   root = tk.Tk()
   App = karl(root)
   root.mainloop()
