import os
import shutil
source = input("enter the source folder's name")
destination = input("enter the destination folder name")

source = source + '/' 
destination = destination + '/'

listofiles = os.listdir(source)
for file in listofiles:
    shutil.copy((source + file),destination)