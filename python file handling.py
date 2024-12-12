import os
#orig_name = input("original file name: ")
#chan_name = input("change name to : ")

while True:
  print(" This is a file handling application")
  print("specialized at making an easy approach to your directory\\file")
  print("instructions to follow: 'l' to show list\n 'x' to create a new file,\n 'r' to read a file,\n 'w' to write to a file,\n 'd' to delete a file, \n 'a' to append to a file, \n and 'q' to quit")
  print("/////////////////////////////")
  value = input("input your alpha: ")
  if value == "x":
    file_name = input("file name: ")
    print("------------------------") 

    if not os.path.splitext(file_name)[1]:
      print("Error: file must have an extention(e.g.,'.txt','.doc','.csv','.ods',)")
      print("_____________________")
      continue
    try:
      f = open(file_name, "x")
      print(f"file {file_name} has been created ")
      print("_____________________")
      
    except FileExistsError:
      print(f"Error: File '{file_name}' already exists.")
      print("**********************")
    f.close()
  elif value == "w":
    file_name = input("file name: ")

    if not os.path.exists(file_name):
      print(f"Error: The file '{file_name}' does not exist. ")
      print("_____________________") 
    elif os.path.exists(file_name):
      f= open(file_name,"w")
      f.write(input("put in your info: ") + "\n")
      print("writing successful ")
      f.close()
    else:
      print(f"Error: Permission denied to write file {file_name}.")
      print("**********************")
 
  elif value == "r" :
    file_name = input("file name: ")
    try:
      f = open(file_name, "r" )
      print(f"You are reading file {file_name} right now ")  
      print(f.read())
      print("_____________________")
    except FileNotFoundError:
      print(f"Error: File {file_name} not found.")
      print("**********************")
    except PermissionError:
      print(f"Error: Permission denied to read file {file_name}.")
      print("**********************")
      f.close()
  elif value == "a" :
    file_name = input("file name: ")

    if not os.path.exists(file_name):
      print(f"Error: The file '{file_name}' does not exist. ")
      print("_____________________") 
    elif os.path.exists(file_name):
      f= open(file_name,"a")
      f.write(input("put in your info: ") + "\n")
      print("appending successful ")
      f.close()
    else:
      print(f"Error: Permission denied to append file {file_name}.")
      print("**********************")
    
  elif value == "d" :
    file_name = input("file name: ")

    if not os.path.exists(file_name):
      print(f"Error: The file '{file_name}' does not exist. ")
      print("_____________________") 
    elif os.path.exists(file_name):
      os.remove(file_name)
      print(f"file {file_name} has been deleted")
      print("_____________________") 
    else:
      print(f"Error: Permission denied to delete file {file_name}.")
      print("**********************")
  elif value == "l" :
    directory = input("Enter directory to list (or press Enter to list current directory): ")
    if not directory:
      directory = os.getcwd()  # Get the current working directory
      try:
        files = os.listdir(directory)
        print("Files in directory:", directory)
        for file in files:
          print(file)
          print("_____________________")
      except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        print("**********************")
      except PermissionError:
        print(f"Error: You don't have permission to access '{directory}'.")
        print("**********************")
  elif value == "q" :
    print("thank you for using this program")
    print("**********************")
    break   
  else :
   print("nah wah oooo")
   print ("you no see instructions")
   print ("mad oooo")
   print(".   /|") 
   print("   / | ")
   print("  /  |")
   print(" /   |")
   print("/__|")
   


