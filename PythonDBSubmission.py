"""This is the python/database submission assignment by Henry Lee
created on 07/20/21. The purpose of this submission is to create and
use a database using python. """

import sqlite3

conn = sqlite3.Connection('PythonDataBase.db')


with conn:
       cur = conn.cursor()
       cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
              ID INTEGER PRIMARY KEY AUTOINCREMENT, \
              col_filename varchar(30))")
       conn.commit()
conn.close()

conn = sqlite3.Connection('PythonDataBase.db')
fileList= ('information.docx', 'Hello.txt', 'myImage.png', \
           'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.gif')

with conn:
       cur = conn.cursor()
       for file in fileList:
              if file.endswith('.txt'):
                     cur.execute("INSERT INTO tbl_files (col_filename) VALUES(?) " , (file,))
              
conn.commit()

conn.close()


conn = sqlite3.Connection('PythonDataBase.db')

with conn:
       cur = conn.cursor()
       cur.execute("SELECT col_filename FROM tbl_files")
       varPerson = cur.fetchall()
       for item in varPerson:
              msg = "File Name is {}".format(item[0])
              print(msg)
