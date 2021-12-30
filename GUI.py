import tkinter as tk
from tkinter import Frame, filedialog, Text
import os

root = tk.Tk()
apps = []
buttonColor = "#ff00ff"
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f: # 'r' = reads from file
        tempApps = f.read()
        tempApps = tempApps.split(',') # Split apps seperated by a comma and store into tempApps
        apps = [x for x in tempApps if x.strip()] # Strips out the empty spaces

def addApp():
    # Destroys anything stored in the frame (apps in the window)
    for widget in frame.winfo_children():
        widget.destroy()

    # Adds app to apps
    fileName = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

# Outer frame
canvas = tk.Canvas(root, height = 700, width = 700, bg="#000000")
canvas.pack()

# Inner frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely= .1)

# Button to open a file location
# text="" is the text on the button
openFile = tk.Button(root, text="Open File" , padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

# Button to run apps based on the list of opened file locations
runApps = tk.Button(root, text="Run Apps" , padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Saves app locations in a text file
# seperated by a comma
with open('save.txt', 'w') as f: # 'w' = write to file
    for app in apps:
        f.write(app + ',')