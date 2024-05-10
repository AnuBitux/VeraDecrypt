import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_file1():
    file_path = filedialog.askopenfilename()
    file_entry1.delete(0, tk.END)
    file_entry1.insert(0, file_path)

def select_file2():
    file_path = filedialog.askopenfilename()
    file_entry2.delete(0, tk.END)
    file_entry2.insert(0, file_path)

def start_tool():
    file1_path = file_entry1.get()
    file2_path = file_entry2.get()
    if file1_path and file2_path:
        command = f'sudo /opt/Tools/Recovery/VeraDecrypt/vdve/bin/python3 /opt/Tools/Recovery/VeraDecrypt/VeraDecrypt.py -v {file1_path} -p {file2_path}'
        os.system(command)
        root.destroy()


# Create main window
root = tk.Tk()
root.title("VeraDecrypt")

# Create widgets
file_label1 = tk.Label(root, text="Volume to unlock:")
file_label1.grid(row=0, column=0, padx=10, pady=5)

file_entry1 = tk.Entry(root, width=50)
file_entry1.grid(row=0, column=1, padx=10, pady=5)

select_button1 = tk.Button(root, text="Choose", command=select_file1, bg="black", fg="blue")
select_button1.grid(row=0, column=2, padx=10, pady=5)

file_label2 = tk.Label(root, text="Password list:")
file_label2.grid(row=1, column=0, padx=10, pady=5)

file_entry2 = tk.Entry(root, width=50)
file_entry2.grid(row=1, column=1, padx=10, pady=5)

select_button2 = tk.Button(root, text="Choose", command=select_file2, bg="black", fg="blue")
select_button2.grid(row=1, column=2, padx=10, pady=5)

start_button = tk.Button(root, text="GO!", command=start_tool, bg="black", fg="blue")
start_button.grid(row=2, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
