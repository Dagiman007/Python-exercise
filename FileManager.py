import shutil
import os
import time
import subprocess

def read():
    path = input("Enter the file path to read: ")
    file = open(path)
    print(file.read())
    input("Press enter...")
    file.close()

def write():
    path = input("Enter the path of file to write or create: ")
    if os.path.isfile(path):
        print("Rebuilding the existing file")
    else:
        print("Creating the new file")

    text = input("Enter text: ")
    file = open(path, 'w')
    file.write(text)

def add():
    path = input("Enter the file path: ")
    text = input("Enter the text to add: ")
    file = open(path, 'a')
    file.write('\n' + text)

def delete():
    path = input("Enter the path of the file for deletion: ")
    if os.path.isfile(path):
        print("File found")
        os.remove(path)
        print("File has been deleted")
    else:
        print("File doesnot exist")

def dirlist():
    path = input("Enter the directory path to display: ")
    sortlist = sorted(os.listdir(path))
    i = 0
    while i < len(sortlist):
        print(sortlist[i] + '\n')
        i += 1

def check():
    fp = int(input("Check existence of \n1. File \n2. Directory\n"))
    if fp == 1:
        path = input("Enter the file path: ")
        if os.path.isfile(path):
            print("File found")
        else:
            print("File does not exist")
    elif fp == 2:
        path = input("Ente the directory path: ")
        if os.path.isdir(path):
            print("Directory found.")
        else:
            print("Directory not found.")

def move():
    path1 = input("Enter the source path of file to move: ")
    mr = int(input("1. Rename \n2. Move \n"))
    if mr == 1:
        path2 = input("Enter the destination path and file name: ")
        shutil.move(path1, path2)
        print("File renamed")
    elif mr == 2:
        path2 = input("Enter the path to move: ")
        shutil.move(path1, path2)
        print("File moved")

def copy():
    path1 = input("Enter the path of the file to copy or rename: ")
    path2 = input("Ente the path to copy to: ")
    shutil.copy(path1, path2)
    print("File copied")

def makedir():
    path = input("Enter the directory name with path to make: ")
    os.makedirs(path)
    print("Directory created.")

def removedir():
    path = input("Ente the path of directory: ")
    treedir = int(input("1. Deleted directory \n2. Delete Directory tree \n3. Exit \n"))
    if treedir == 1:
        os.rmdir(path)
    elif treedir == 2:
        shutil.rmtree(path)
        print("Directory deleted.")
    elif treedir == 3:
        exit()

def openfile():
    path = input("Enter the path of program: ")
    try:
        os.startfile(path)
    except:
        print("File not found.")

def main():
    run = 1
    while run == 1:
        try:
            os.system("cls")
        except OSError:
            os.system("clear")

        print("\n>>>>>>>>>>>>>>>>>   File Manager <<<<<<<<<<<<<<<<<<\n")
        print("The current time and date is : ", time.asctime())
        print("\nChoose the option number: \n")
        dec = int(input('''1. Read a file
2. Write to a file
3. Append text to a file
4. Delete a file
5. List files in a directory
6. check file existence
7. Move a file
8. Copy a file
9. Create a directory
10, Delete a directory
11. Open a program
12. Exit
    '''))

        if dec == 1:
            read()
        elif dec == 2:
            write()
        elif dec == 3:
            add()
        elif dec == 4:
            delete()
        elif dec == 5:
            dirlist()
        elif dec == 6:
            check()
        elif dec == 7:
            move()
        elif dec == 8:
            copy()
        elif dec == 9:
            makedir()
        elif dec == 10:
            removedir()
        elif dec == 11:
            openfile()
        elif dec == 12:
            exit()

        run = int(input("1. Return to menu\n2. Exit\n"))
        if run == 2:
            exit()

main()
              
                    
                
             
            
        
