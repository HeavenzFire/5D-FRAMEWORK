import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Spirit Engine Demo")

# Define a sample function
def sample_function():
    result = "Hello, this is a function display from Spirit Engine!"
    messagebox.showinfo("Function Output", result)

# Create a button to trigger the function
button = tk.Button(root, text="Run Function", command=sample_function)
button.pack(pady=20)

# Run the application
root.mainloop()
