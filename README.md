# MassRenameinPython
 Script that mass renames files in a folder 


This script provides a simple tool for batch-renaming files in a selected directory. It allows the user to specify a prefix, and the script appends sequential numbers to the filenames while preserving their original extensions. Using a graphical interface, the user can select a directory and input the desired prefix. The script then processes the files, ensuring they are renamed in a consistent and organized manner, making it useful for managing collections of files like photos, documents, or media.


1. List all files in the directory

2. Sort files to maintain order

3. Initialize the starting number for the suffix

4. Split the filename into name and extension

5. Create the new filename using the prefix and the current number, while keeping the extension

6. Rename the file

7. Increment the number for the next file

8. Set up the Tkinter root window

9. we don't want a full GUI, so keep the root window from appearing

10. Show an "Open" dialog box and return the path to the selected file

11. Prompt for the prefix

12. Make sure the directory and prefix are not empty