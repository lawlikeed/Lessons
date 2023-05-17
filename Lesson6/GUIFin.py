# Create a basic Graphical User Interface using TKinter





# Import TKinter
import tkinter as tk
from tkinter import Frame, Image, messagebox

# Constant for what color we want the background, buttons and text to be
BG_COLOR = 'Red'
BTN_COLOR = 'Black'
BTN_TXT_COLOR = 'White'
OTHER_BG_COLORS = ['Green', 'Gold', 'Blue']







# Functions
def good_click():
    messagebox.showinfo('Pop up', 'This is a pop up box!')

def bad_click():
    messagebox.showwarning('Virus Installation.exe', 'Downloading malware...')
    root.destroy()

def rand_click():
    messagebox.showerror('ERROR', 'Please Check Console For More Info')
    print('Just wanted to waste your time :p')

def UnCheck_box():
    if chVarUn.get() == 0:
        print('Unchecked box is unchecked!')
    else: print('Unchecked box is now checked!')

def EnCheck_box():
    if chVarEn.get() == 1:
        print('Enabled box is checked!')
    else: print('Enabled box is unchecked!')

# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if   radSel == 1: root.configure(background=OTHER_BG_COLORS[0])
    elif radSel == 2: root.configure(background=OTHER_BG_COLORS[1])
    elif radSel == 3: root.configure(background=OTHER_BG_COLORS[2])
    else: root.configure(background=BG_COLOR)





# This will make the window for our GUI
root = tk.Tk()

root.title('My App!')                   # We can give our window a title using the title method
root.geometry('650x350')                # We can give our window specific dimensions 
root.resizable(False, False)            # We can disable the user from resizing the window
root.configure(background=BG_COLOR)     # Set the color of the background

name_label = tk.Label(root, text='Name:', background=BTN_COLOR, foreground=BTN_TXT_COLOR)                           # This is how we make a label
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

submit_btn = tk.Button(root, text='  Submit  ')
submit_btn.grid(row=2, column=2)


# Buttons Frame
btns_frame = Frame(root)                                # We can use a frame to and create a new container to place our things in
btns_frame.grid(row=3, columnspan=2, sticky='w')        # We can place our frame on the grld layout

good_btn = tk.Button(btns_frame, text='Click Me!', command=good_click)      # Here is how we make a button and make it do something
good_btn.grid(row=0, column=0, pady=8, padx=20)                             # Place the button in the first row of this new container

bad_btn = tk.Button(btns_frame, text="Don't Click Me!", command=bad_click)  # Here is another button
bad_btn.grid(row=0, column=1, pady=8, padx=20)                              # We place it in the next column

rand_btn = tk.Button(btns_frame, text='Click Me?', command=rand_click)      # Here is another button
rand_btn.grid(row=0, column=2, pady=8, padx=20)                             # We place it in the next column

# Creating check buttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(root, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(row=4, column=0, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(root, text='Unchecked', variable=chVarUn, background=BG_COLOR, command=UnCheck_box)
check2.deselect()
check2.grid(row=4, column=1, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(root, text='Enabled', variable=chVarEn, background=BG_COLOR, activebackground=BG_COLOR, command=EnCheck_box)
check3.select()
check3.grid(row=4, column=2, sticky=tk.W)

# create three Radio buttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(root, text=OTHER_BG_COLORS[0], variable=radVar, value=1, command=radCall)
rad1.grid(row=5, column=0, sticky=tk.W, columnspan=4)

rad2 = tk.Radiobutton(root, text=OTHER_BG_COLORS[1], variable=radVar, value=2, command=radCall)
rad2.grid(row=5, column=1, sticky=tk.W, columnspan=4)

rad3 = tk.Radiobutton(root, text=OTHER_BG_COLORS[2], variable=radVar, value=3, command=radCall)
rad3.grid(row=5, column=2, sticky=tk.W, columnspan=4)

rad4 = tk.Radiobutton(root, text='Original Color', variable=radVar, value=4, command=radCall)
rad4.grid(row=5, column=3, sticky=tk.W, columnspan=4)




#======================
# Start GUI
#======================
root.mainloop() 