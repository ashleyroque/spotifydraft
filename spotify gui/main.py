import tkinter as tk
from tkingergui import TabGenerator

root = tk.Tk()
root.geometry("500x250")
root.resizable(height=False, width=False)
tab_names = {0: "Home", 1 : "Profile", 2: "Away"}
tab_generator = TabGenerator(root, 3, tab_names)

root.mainloop()