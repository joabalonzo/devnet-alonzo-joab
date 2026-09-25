"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Alonzo, Joab P.]
Date: [September 25, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[i built a simple Python program that organize the files into different folders. The program checks the files inside the 
file-to-sort folder and sorts them based on their extension. For example .txt files go into a text folder .jpg go into the 
jpg folder and .pdf go to the pdf folder. it uses the os module to check the file and the shutil to move the files.]


============================================
KEY VOCABULARY
============================================
- os module: This is a python module that work with the files, folders and file paths.
- shutil module: This is a python module used to oporate the file or move them.
- file path: This is the locati on of the file or folder on the computer.
- directory:  This is a another term for folder or another name for folder.
- file extension: This is a part of the file name that shows its file type. Example .txt .jpg and .pdf.

(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# This is the folder name
source_folder = "file-to-sort"
# Get all the files that included in the folder and shows them
for filename in os.listdir(source_folder):

  # Getting the complete file path
  file_path = os.path.join(source_folder, filename)

  # Check if the item is a file
  if os.path.isfile(file_path):

  # Get the file extension
  extension = os.path.splitext(filename)[1].lower()
  # Remove the dot from the extension
  extension = extension.replace(".", "")

  # Create the destination folder
  destination_folder = os.path.join(source_folder, extension)

  # Create the folder if it does not exist 
  os.makedirs(destination_folder, exist_ok=True)

  # Create the final destination path
  destination_path = os.path.join(destination_folder, filename)

  # Move the file 
  shutil.move(file_path, destination_path) 

print("Files have been sorted successfully!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[When i am doing this, i encountered a simple error when i ran it, it shows that FileNotFoundError because 
the folder name in my code did not match the actual folder name. The folder name that i made is file to sort 
and the one that i used in my code is file_to_sort and then i am wondering because i think my code is right,
i kept looking at my code for about 5 minutes and then i figured out i put the wrong symbol. After i fixed the 
symbol the code ran seccessfully. ]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[This activity is similar to a real automation because a program or a code that can organize files
automatically instead of moving them manually one by one. For example, it could be use to organize our 
files in school. Such as the .txt .jpg amd the .pdf.]
"""
