import os
import shutil

src = str(raw_input("Enter source folder anem :- "))
dest = str(raw_input("Enter desctind folder name :- "))

src = src + "/"
dest = dest+ "/"

list_of_files = os.listdir(src)

for file_ in list_of_files:
  shutil.copy((src+file_),dest)