# Hello! Bonjour ! 안녕하세요! Saluton!

import tkinter as tk   # You might need to download. 

root = tk.Tk()      # Making the window.
root.title("Hello World with Tkinter!")
root.geometry("400x200")
tk.Label(root, text="Hello World!").pack() # Hello Wold


R2 = tk.Frame(root) # Row 2 is a seperate frame
R2.pack()   # The frame must be put there


tk.Label(R2, text="Whats your name?").pack(side="left") 
name_entry = tk.Entry(R2) # Input Box in Row 2
name_entry.pack() # puting it there

# @KingHenrytheGreat36


root.mainloop() # This must go at the end