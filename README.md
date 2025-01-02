# MassRenameinPython
 Script that mass renames files in a folder 


This script provides a simple tool for batch-renaming files in a selected directory. It allows the user to specify a prefix, and the script appends sequential numbers to the filenames while preserving their original extensions. Using a graphical interface, the user can select a directory and input the desired prefix. The script then processes the files, ensuring they are renamed in a consistent and organized manner, making it useful for managing collections of files like photos, documents, or media.


 List all files in the directory
 Sort files to maintain order
 Initialize the starting number for the suffix
 Split the filename into name and extension
 Create the new filename using the prefix and the current number, while keeping the extension
 Rename the file
 Increment the number for the next file
 Set up the Tkinter root window
 we don't want a full GUI, so keep the root window from appearing
 Show an "Open" dialog box and return the path to the selected file
 Prompt for the prefix
 Make sure the directory and prefix are not empty