'''

Command Prompt V2.0

Author: Jake Grice

Purpose: A Conventional Terminal With A Few Extra Commands For Ease Of Use

'''


# all the modules used while making the command prompt

import os # allows for operating system manipulation
import shutil # used to center text on the console
from datetime import datetime
try:
    import wget # used to download files
except ImportError:
    print("no module called wget")
    input()

try:
    from columnar import columnar # used to put all the files and folders in the ls command into columns
except ImportError as ie:
    print(ie)
    input()



def find_file(file_name): # searches the system for file_name
    for root, dirs, files in os.walk("C:\\"): # goes through every file in the c drive
        if file_name in files: # if it finds the file the user wants
            print(f"Found {file_name} At {root}") # tells the user that it found it and where it found it

def find_from_dir(file_dir, file_name): # searches file_dir for file_name
    for root, dirs, files in os.walk(file_dir): # goes through a directory provided by the user
        if file_name in files: # if it finds the file specified
            print(f"Found {file_name} At {root}") # tells the user that the file was found and where

def print_centre(text): # centres any text in a command prompt
    print(text.center(shutil.get_terminal_size().columns)) # gets the size(width) of the cli and centers the text onceit knows

os.system("cls") # clears the console before starting the program

print("")
print_centre('* Command Prompt Updated V2.0 *')
print_centre('-------------------------------')
print("")
print_centre('Added ls Command')
print_centre('ls [dir name] - lists all the items in the current directory')
print("")
print_centre('Added cd Command')
print_centre('cd [dir name] - changes directory to one specified by the user')
print("")
print_centre('Added dwd Command')
print_centre('dwd [file url] [file name] - downloads a file from a given link')
print("")
print_centre("Added out Command")
print_centre("out [file path] [num of lines] - outputs data from a file")
print("")
print_centre("Added find Command")
print_centre("find [file name] [file dir] - searches the entire machine for the specified file(SLOW), file dir isnt required")
print_centre('--------------------------------------------------------------------------------------------------------------')
      




while True:
    try:
        command = input(f"\n{os.getcwd()}> ") # sets the input to the current directory(like windows)
        command = command.strip() # removes any unnecessary whitespace from the command
        
        # all code for the ls command
        if command.strip() == "ls": # if the users wants to list all files in the current directory
            info = []
            try:
                for root, dirs, files in os.walk(os.getcwd()): # goes through all folders and files in the current directory
                    for i in dirs: # for any folders it finds
                        last_mod_time = datetime.fromtimestamp(os.stat(os.path.join(str(root), i)).st_mtime) # last time the folder was modified
                        file_extension = os.path.splitext(os.path.join(str(root), i)) # finds the file extension for the folder
                        info.append(["Folder", i, str(os.path.getsize(os.path.join(str(root), i))/1000), str(root), file_extension[1], last_mod_time]) # adds the type of file, the name, root folder and extension to the list
                    for i in files: # for any files it finds
                        last_mod_time = datetime.fromtimestamp(os.stat(os.path.join(str(root), i)).st_mtime) # last time the file was modified
                        file_extension = os.path.splitext(os.path.join(str(root), i)) # finds the file extension
                        info.append(["File", i, str(os.path.getsize(os.path.join(str(root), i))/1000), str(root), file_extension[1], last_mod_time]) # adds the type of file, the name, root folder and extension to the list
                file_list_table = columnar(info, headers=["Type", "File Name", "File Size(kb)", "Root Folder", "Extension", "Last Modified"], no_borders=True) # creates an organised column of information which can be outputted
                print(file_list_table) # prints the table of information
            except Exception as e:
                print(f"An Error Occured\nError Type: {type(e).__name__}\nError Reason: {e}") # if any type of error occurs, outputs the type of error and why it happened
                
        elif command.startswith("ls"): # if a user wants to list all files in a different directory
            if len(command.split()) == 2: # checks if a user has added a directory to search
                command = command.replace("ls", "").split() # removes the ls from the string and extracts the directory path
                command[0] = command[0].strip() # removes any whitesapce from the directory path
                directory_path = command[0] # sets the directory path to an easy to use variable
                info = []
                try:
                    for root, dirs, files in os.walk(command[0]): # searches the given directory
                        for i in dirs:
                            file_ext = os.path.splitext(os.path.join(str(root), i)) # extracts the file extension
                            info.append(["Folder", i, str(os.path.getsize(os.path.join(str(root), i))/1000), str(root), file_ext[1]]) # adds the type of file, the name, root folder and extension to the list
                        for i in files:
                            file_ext = os.path.splitext(os.path.join(str(root), i)) # extracts the file extension
                            info.append(["File", i, str(os.path.getsize(os.path.join(str(root), i))/1000), str(root), file_ext[1]]) # adds the type of file, the name, root folder and extension to the list
                    file_table = columnar(info, headers=["Type", "File Name", "File Size(kb)", "Root Folder", "Extension"], no_borders=True) # creates an organised column of information which can be outputted
                    
                    print(file_table) # prints the table of information
                except Exception as e:
                    print(f"An Error Occured\nError Type: {type(e).__name__}\nError Reason: {e}") # if an error occurs, it tells the user the error type and reason for the error
                
        # all code for the find command        
        elif command.startswith("find"): # if a user wants to fina a certain file on the system
            if len(command.split()) == 3: # if a user wants to search in a specific directory
                command = command.replace("find", "").split() # removes "find" and extracts the file they want to search for
                command[0] = command[0].strip() # removes whitespace from the file name
                command[1] = command[1].strip() # removes whitespace from the file directory
                file_name, file_dir = command[0], command[1] # sets the file name/directory to variables
                find_from_dir(file_dir, file_name) # searches for [ file_name ] inside [ file_dir ]
            else:
                command = command.replace("find", "").strip() # extracts file name
                find_file(command) # searches the entire system for the file
               
        # all code for the cd command       
        elif command.startswith("cd"): 
            command = command.replace("cd", "").strip() # removes "cd" and removes any whitespace
            os.chdir(command) # uses the built in os.chdir function to change the directory to the one specified by the user
            print(f"Directory Changed To: {os.getcwd()}\n") # tells the user that they changed directory successfully
            
        # all code for the start command - BUG - FIXED
        elif command == "start": 
            os.startfile(os.path.join(os.getcwd(), __file__)) # starts a new instance of the command prompt v2
        
        # all code for the dwd command
        elif command.startswith("dwd"):
            if command == "dwd": # if a user hasnt provided a url to download from
                print("Please Provide A Url To The File You Wish To Download") # asks suser to provide a url
            
            elif len(command.split()) == 3: # if a user wants to name the file something once its downloaded
                url = command.replace("dwd", "").split() # removes "dwd" and extracts the url and file name
                for i in url:
                    file_url = url[0].strip() # sets the file url to a variable and removes whitespace
                    file_name = url[1].strip() # sets the file name to a variable and removes whiteapce
                try:
                    wget.download(file_url, file_name) # downloaded the file from the url and names it [ FILE_NAME ]
                except Exception as e:
                    print(f"An Error Occured While Trying To Run The Command: {command}") # runs if the command prompt cant run a certain command
                    print(f"Error Type: {type(e).__name__}")
                    print(f"Error Reason: {e.__cause__}")
            else: # if a user doesnt provide a file name
                url = command.replace("dwd", "") # removes "dwd" from the string
                url = url.strip() # removes whitespace
                try:
                    wget.download(url) # downloads the file without renaming it
                except Exception as e:
                    print(f"Error: {type(e).__name__}")
                    print("Unable To Download File From The Url Provided")
                    
        # BUG - splittext() needs fixing so it finds the file type - [ FIXED ]
        elif command.startswith("out"): # if a user wants to print a files contents
            if command == "out": # if they dont provide a file directory
                print("Please Provide A Path To The File You Want To Output") # asks user to provide a valid directory
            elif len(command.split()) == 2: # if a user has provided a directory
                command = command.split() # extracts the directory path from the rest of the string
                command.remove(command[0]) #removes useless parts of the string
                command[0] = command[0].strip() # removes any whitespace
                file_type = os.path.splitext(command[0])
                if file_type[1] != ".txt":
                    print("the out command only works with files ending in .txt")
                else:
                    try:
                        with open(command[0]) as file: # opens up the file the user wants and sets it to a variable called file
                            file_data = file.readlines() # gets every line from the file
                            print(file_data) # outputs every line from the file
                    except Exception as e:
                        print(f"Error Type: {type(e).__name__}\nError Reason: {e}")
                    
            elif len(command.split()) == 3:
                command = command.split()
                command.remove(command[0]) # removes the out word
                file_path = str(command[0]).strip()
                lines_printed = int(command[1])
                file_type = os.path.splitext(file_path)
                if file_type[1] != ".txt":
                    print("the out command only works with files ending in .txt")
                else:
                    try:
                        with open(command[0]) as file:
                            file_data = file.readlines()
                            for i in file_data[0:lines_printed]:
                                print(i)
                    except Exception as e:
                        print(f"Error Type: {type(e).__name__}\nError Reason: {e}")
            else:
                print(f"the out command takes 3 arguments, you provided {len(command.split())}")
        
        else:
            os.system(f"{command}") # all other commands are run here
    except Exception as e:
        print(f"An Error Occured While Trying To Run The Command: {command}") # runs if the command prompt cant run a certain command
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Reason: {e}")
        