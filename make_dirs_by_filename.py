import os
from re import match
from datetime import datetime

# main_path = os.getcwd() # current working directory
main_path = input("Podaj bezwzględną ścieżkę do katalogu: ") # the path has to be valid

for root, _, files in os.walk(main_path):
   for file in files:
       _, ext = os.path.splitext(file)
       ext = ext.lower()
       if ext in {".jpg", ".cr2", ".jpeg", ".mov"}:
           date = file[:10]
           if not match("^\d{4}_\d{2}_\d{2}", date):
               continue

           filename = file[10:]
           new_dest = os.path.join(main_path, date)

           if not os.path.exists(new_dest):
               os.mkdir(new_dest)
           os.replace(os.path.join(root,file), os.path.join(new_dest, filename))
   break # only one level

print("Zrobione!")
