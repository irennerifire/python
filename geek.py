import os
import psutil

print("Real program")
print("Hello!")
name=input("Имя?")
work=input("Поработаем? Y/N")

if work == "Y":
    #print("Nice!")
    #pass
    print("What you prefer to do?")
    print("1) Read file, 2) write file, 3) test code ")
    choice=int(input("1,2 or 3?"))
    if choice == 1:
        print("I will download random book...", os.listdir())
    elif choice == 2:
        print("Hmm... MS Word or Atom?")
        print("Look at the proceses", psutil.pids())
    else:
        print("Yes! Tell me what to do next!")
elif work =="N":
    print("Buy!")
else:
    print("What do you mean?")
