#pip install tk


import tkinter as tk
from tkinter import messagebox
import uuid

def generate_uuids():
    try:
        num_uuids = int(entry.get())
        if num_uuids <= 0:
            raise ValueError("Number must be positive")
        uuid_list.delete(0, tk.END)
        for _ in range(num_uuids):
            new_uuid = uuid.uuid4()
            uuid_list.insert(tk.END, new_uuid)
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# Set up the main application window
root = tk.Tk()
root.title("UUID Generator___0abd0___")

# Create and place widgets
label = tk.Label(root, text="Enter number of UUIDs to generate:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate UUIDs", command=generate_uuids)
generate_button.pack(pady=10)

uuid_list = tk.Listbox(root, width=50, height=10)
uuid_list.pack(pady=10)

# Run the application
root.mainloop()
