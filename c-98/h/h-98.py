from os.path import exists,dirname,join,abspath
from pathlib import Path

# The testing is done in files in client folder

def main():
  while True:
    print("===================== Rickroll Content =====================")
    print("Swap the contents of any file with Rick Astley's Famous Song")
    file_path = str(raw_input("Enter the exact path of the file (with extension) you want to swap with Rick Roll :- "))
    get_file(file_path)


def get_file(file_path):
  try:
    path_exists = exists(file_path)
    
    if (path_exists):
        is_file = Path(file_path)

        if(Path.is_file(is_file)):
          swap_data(file_path)
        else:
          print("That is not a file.That is a folder")

    else:
      print("That path doesn't exist.")
  
  except:
    print("Something went wrong")


def swap_data(file_path):
  try:
    master_file_path = join(dirname(abspath(__file__)),"data","master.txt")
    
    master_file = open(master_file_path,"r")
    victim_file = open(file_path,"w")

    master_file_contents = master_file.read()

    victim_file.write(master_file_contents)

    master_file.close()
    victim_file.close()

    print("Process Done.")
    

  except:
    print("Something went wrong")

  
main()
