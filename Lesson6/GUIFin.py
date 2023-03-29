# Create a basic Graphical User Interface using TKinter





# Import TKinter
import tkinter as tk
from tkinter import Frame, messagebox



# Functions
def good_click():
    messagebox.showinfo('Pop up', 'This is a pop up box!')

def bad_click():
    messagebox.showwarning('Virus Installation.exe', 'Downloading malware...')
    root.destroy()

def rand_click():
    messagebox.showerror('ERROR', 'Please Check Console For More Info')
    print('Just wanted to waste your time :p')

# This will make the window for our GUI
root = tk.Tk()

root.title('My App!')           # We can give our window a title using the title method
root.geometry('650x350')        # We can give our window specific dimensions 
root.resizable(False, False)    # We can disable the user from resizing the window

name_label = tk.Label(root, text='Name:')                           # This is how we make a label
name_label.grid(row=0, column=0, pady=10, padx=15, sticky='se')     # Place the label using grid layout management
name_entry = tk.Entry(root)                                         # We can now make an entry field for text
name_entry.grid(row=0, column=1, pady=10)                           # We now place the entry field at row 0, col 1

age_label = tk.Label(root, text='Age:')                         # Label for Age
age_label.grid(row=1, column=0, pady=8, padx=15, sticky='e')    # Place the label underneath the first label
age_entry = tk.Entry(root)                                      # Age entry field
age_entry.grid(row=1, column=1)                                 # Place entry field

color_label = tk.Label(root, text='Favorite Color:')                # Label for color
color_label.grid(row=2, column=0, pady=8, padx=15, sticky='e')      # Place the label in the next row
color_entry = tk.Entry(root)                                        # Color entry field
color_entry.grid(row=2, column=1, pady=8, padx=20)                  # Place entry field to the right of corresponding label

# Buttons Frame
btns_frame = Frame(root)
btns_frame.grid(row=3, columnspan=2, sticky='w')

good_btn = tk.Button(btns_frame, text='Click Me!', command=good_click)    # Here is how we make a button and make it do something
good_btn.grid(row=0, column=0, pady=8, padx=20)                     # Place the button in the next row

bad_btn = tk.Button(btns_frame, text="Don't Click Me!", command=bad_click)
bad_btn.grid(row=0, column=1, pady=8, padx=20)

rand_btn = tk.Button(btns_frame, text='Click Me?', command=rand_click)
rand_btn.grid(row=0, column=2, pady=8, padx=20)


# This will display the window on out screen
root.mainloop() 