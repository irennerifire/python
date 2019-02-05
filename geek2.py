import os
import psutil
import shutil
import sys

print("Real program")
print("Hello!")
name=input("Имя?")
#work=input("Поработаем? Y/N")

work=''
while work != 'q':
    work=input("Поработаем? Y/N/q    ")
    if work == "Y":
        print("What you prefer to do?")
        print("1) Read file, 2) write file, 3) test code ")
        choice=int(input("1,2 or 3?   "))
        if choice == 1:
            print("I will download random book...")
            print("There are following files in the system  ", os.listdir())
        elif choice == 2:
            print("Hmm... MS Word or Atom?")
            print("Platform: ", sys.platform)
            print("Number of procecors: ", psutil.cpu_count())
            print("File system encoding: ", sys.getfilesystemencoding())
            print("Directory: ", os.getcwd())
            print("Current user: ", os.getlogin())
        elif choice == 3:
            print("Yes! Tell me what to do next!")
            print("Look at the proceses", psutil.pids())
        elif choice == 4:
            print("Copying files in current directory:   ")
            file_list=os.listdir()
            i=0
            while i < len(file_list):
                newfile=file_list[i]+'.dupl'
                shutil.copy(file_list[i], newfile)
                i+=1
        else:
            pass
    elif work =="N":
        print("Buy!")
    elif work =="q":
        print("Stop the program!")
    else:
        print("What do you mean?")
