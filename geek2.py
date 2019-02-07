import os
import psutil
import shutil
import sys

def duplicate_file (filename):
    if os.path.isfile(filename):
        newfile=file_list[i]+'.dupl'
        shutil.copy(file_list[i], newfile)
        if os.path.exists(newfile):
            print("Файл",  newfile, " был успешно создан")
            return True
        else:
            print("Some problems have appeared")
            return False

def sys_info ():
    print("Hmm... MS Word or Atom?")
    print("Platform: ", sys.platform)
    print("Number of procecors: ", psutil.cpu_count())
    print("File system encoding: ", sys.getfilesystemencoding())
    print("Directory: ", os.getcwd())
    print("Current user: ", os.getlogin())

print("Real program")
print("Hello!")
name=input("Имя?")
#work=input("Поработаем? Y/N")

work=''
while work != 'q':
    work=input("Поработаем? Y/N/q    ")
    if work == "Y":
        print("What you prefer to do?")
        print("1) Read file, 2) write file, 3) test code 4)To copy files 5)Special file duplicating  6) Remove duplicates ")
        choice=int(input("1,2 or 3, 4, 5, 6?   "))
        if choice == 1:
            print("I will download random book...")
            print("There are following files in the system  ", os.listdir())
        elif choice == 2:
            sys_info()
        elif choice == 3:
            print("Yes! Tell me what to do next!")
            print("Look at the proceses", psutil.pids())
        elif choice == 4:
            print("Copying files in current directory:   ")
            file_list=os.listdir()
            i=0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i+=1
        elif choice == 5:
            print("Your file duplicating")
            filename = input("Filename?")
            duplicate_file(filename)
            i+=1
        elif choice == 6:
            print("Delete the duplicates in the directory")
            dirname = input("Directory?")
            file_list = os.listdir(dirname)
            #i=0
            #while i < len(file_list):
            for i in file_list:
                #fullfilename = dirname + file_list[i]
                fullfilename=os.path.join(dirname, file_list[i])
                if fullfilename.endswith('.dupl'):
                    os.remove(fullfilename)
                #i+=1
        else:
            pass
    elif work =="N":
        print("Buy!")
    elif work =="q":
        print("Stop the program!")
    else:
        print("What do you mean?")
