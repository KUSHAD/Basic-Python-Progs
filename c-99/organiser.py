import os
import shutil

path = 'd:/Pics'

files = os.listdir(path)

for one_file in files:
  name,ext = os.path.splitext(one_file)
  ext = ext[1:]
  if(ext == ""):
    continue

  if(os.path.exists(path+'/'+ext)):
    shutil.move(path+'/'+one_file,path+'/'+ext)
  else:
    os.mkdir(path+'/'+ext)
    shutil.move(path+'/'+one_file,path+'/'+ext)

