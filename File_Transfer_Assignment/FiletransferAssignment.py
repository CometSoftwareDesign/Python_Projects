import shutil
import os

#set where the source of files are

source = 'C:/Python_Projects/Python_Challenges/File_Transfer_Assignment/FolderA/'

#Set destination

destination = 'C:/Python_Projects/Python_Challenges/File_Transfer_Assignment/FolderB/'
files = os.listdir(source)

for i in files:
       #we are saying move the files represented by 'i' to their new destination
       shutil.move(source+i, destination)
