import os
from datetime import datetime

# main_path = os.getcwd() # current working directory
main_path = input("Podaj bezwzględną ścieżkę do katalogu: ") # the path has to be valid

for root, _, files in os.walk(main_path):
   for file in files:
       date = os.stat(os.path.join(root,file)).st_mtime
       date_str = datetime.fromtimestamp(date).strftime('%Y_%m_%d')
       new_dest = os.path.join(main_path, date_str)
       if not os.path.exists(new_dest):
           os.mkdir(os.path.join(main_path, date_str))
       os.replace(os.path.join(root,file), os.path.join(new_dest, file))
   # break # only one level

print("Zrobione!")
