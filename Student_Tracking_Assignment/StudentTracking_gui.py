
#this is the gui module for the python phonebook

#first step is to import the other modules so that they can
#be used properly

import student_Tracking_Functions
import student_TrackingAssignment

def load_gui(self):
#the following is the label being created
       
       self.lbl_fname = tk.Label(self.master,text = 'First Name: ')
       self.lbl_fname.grid(row = 0,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)

       self.lbl_lname = tk.Label(self.master,text = 'Last Name: ')
       self.lbl_lname.grid(row = 2,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)


       self.lbl_phone = tk.Label(self.master,text = 'Phone: ')
       self.lbl_phone.grid(row = 4,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)


       self.lbl_email = tk.Label(self.master,text = 'Email: ')
       self.lbl_email.grid(row = 6,column= 0, padx=(27,0), pady=(10,0),sticky = N+W)

       self.lbl_user = tk.Label(self.master,text = 'User: ')
       self.lbl_user.grid(row = 0,column= 2, padx=(0,0), pady=(10,0),sticky = N+W)

#the following is the text imput just above the label
       
       self.txt_fname = tk.Entry(self.master,text = ' ')
       self.txt_fname.grid(row = 1, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)

       self.txt_lname = tk.Entry(self.master,text = '')
       self.txt_lname.grid(row = 3, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)


       self.txt_phone = tk.Entry(self.master,text = '')
       self.txt_phone.grid(row = 5, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)


       self.txt_email = tk.Entry(self.master,text = '')
       self.txt_email.grid(row = 7, column= 0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0),sticky = N+E+W)

     
#the following code is for a scrolling bar

       #self.scrollbar1 = Scrollbar(self.master,orient= VERTICAL)
       #self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand = self.scrollbar1.set)
       #self.lstList1.bind('<<ListboxSelect>>',lambda event: student_Tracking_Functions.onSelect(self,event))
       #self.scrollbar1.config(command=self.lstList1.yview)
       #self.scrollbar1.grid(row = 1,column = 5,rowspan = 7,columnspan= 1, padx(0,0),pady(0,0),sticky = N+E+S)
       #self.lst1List1.grid(row=1, column=2, rowspan = 7, columnspan = 3, padx(0,0),pady(0,0), sticky = N+E+S+W)

#the next section creates buttons
       self.btn_submit = tk.Button(self.master,width = 12,height = 2,text = 'Submit',command = lambda: student_Tracking_Functions.submit(self))
       sekf.btn_submit.grid(row= 8, column=0, padx(25,0), pady(45,10), sticky=W)
    
       self.btn_delete = tk.Button(self.master,width = 12,height = 2,text = 'Delete',command = lambda: student_Tracking_Functions.onDelete(self))
       sekf.btn_delete.grid(row= 8,column=2, padx (15,0),pady(45,10), sticky = W)


      
       student_Tracking_Functions.create_db(self)
       student_Tracking_Functions.onRefresh(self)
       






       
