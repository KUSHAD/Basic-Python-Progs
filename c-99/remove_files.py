from os import path,walk,stat,remove
from pathlib import Path
from time import time
from shutil import rmtree

seconds_to_live = time() - (30*24*60*60)


def main():
  while True:
    folder_path = str(raw_input("Enter the exact path of the folder you wish to clean :- "))
    check_path(folder_path)


def check_path(folder_path):
  if(path.exists(folder_path)):
    path_folder = Path(folder_path)
    if(Path.is_dir(path_folder)):
      walk_dir(folder_path)
    else:
      print("The path you provided was actually a file. Submit a folder path")
  else :
    print("Path doesn't exist")

def walk_dir(folder_path):
  for root_folder, folders, files in walk(folder_path):
    if (seconds_to_live >= check_file_folder_age(folder_path)):
      remove_folder(folder_path)
      break
    else:
      for folder in folders:
        new_path = path.join(root_folder,folder)
        if (seconds_to_live >= check_file_folder_age(new_path)):
						remove_folder(new_path)

      for one_file in files:
        file_path = path.join(root_folder,one_file)
        if (seconds_to_live >= check_file_folder_age(file_path)):
          remove_file(file_path)
  
def check_file_folder_age(folder_path):
  
  x = stat(folder_path).st_ctime

  return x

def remove_folder(folder_path):
  if not rmtree(folder_path):
    print(folder_path, " was deleted successfully")
  else:
    print("unable to delete path :- ",folder_path)

def remove_file(file_path):
  if not remove(file_path):
    print(file_path, " was deleted successfully")
  else:
    print("unable to delete path :- ",file_path)

main()