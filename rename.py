import os
from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk

def rename_files_in_directory(directory, prefix):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # Sort files to maintain order
    files.sort()
    # Initialize the starting number for the suffix
    num = 1
    for filename in files:
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        # Create the new filename using the prefix and the current number, while keeping the extension
        new_filename = f"{prefix}{num}{extension}"
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        # Increment the number for the next file
        num += 1

if __name__ == "__main__":
    # Set up the Tkinter root window
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    
    # Show an "Open" dialog box and return the path to the selected file
    directory = filedialog.askdirectory(title="Select Directory")
    
    # Prompt for the prefix
    prefix = simpledialog.askstring("Input", "Enter the prefix for the files:", parent=root)
    
    # Make sure the directory and prefix are not empty
    if directory and prefix:
        rename_files_in_directory(directory, prefix)
        print(f"Files in '{directory}' have been renamed with the prefix '{prefix}'.")
    else:
        print("Operation cancelled or invalid input.")
