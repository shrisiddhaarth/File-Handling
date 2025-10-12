#Using write() function along with with open()
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("We are learning file handling in Python.\n")

 #Using write() function along with split()
text = "Python is fun and easy to learn"
with open("sample.txt", "w") as file:
    words = text.split()
    for i in words:
        file.write(i+ "\n")

import os

# Create a new file
try:

    with open("newfile.txt", "x") as file:
        file.write("This is a newly created file")
    print("File created sucessfully")
except  FileExistsError:
   print("File already exists")
# Check if a file exsists
filename = "sample.txt"
if os.path.exists(filename):
   print(f"The file exists")

else:
   print("File doest not exist")

# Create a new file if it does not exsist
filename = "data.txt"
if not os.path.exists(filename):
    with open(filename, "x") as file:
        file.write("This is a newly created file.\n")
else:
    print("File already exists")

import os

# Delete a file
filename = "newsfile.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"File'{filename}' deleted sucessfully")
else:
    print(f"File '{filename}' does not exist")

# Delete a folder
folder_name = "test_folder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder'{folder_name}' deleted succesfully")
else:
    print(f"File '{filename}' does not exist")
