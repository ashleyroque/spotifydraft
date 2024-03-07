import tkinter as tk
from tab_view import handle_tab_view

class TabGenerator:
    def __init__(self, root, num_tabs, tab_names):
        self.root = root #creates the main window

        self.tab_menu = tk.Menu(self.root) #creates the tab menu
        self.root.config(menu=self.tab_menu) #configs the tab menu to the main window

        self.tab_frames = {} #dict to hold the frames of each tab
        for i in range(num_tabs): #num_tabs determines the number of tabs
            self.tab_frame = tk.Frame(self.root) #creates a frame for each individual tab
            self.tab_frames[i] = self.tab_frame


            name = tab_names.get(i, f"tab {i+1}")
            self.create_tab(name, i) #tab name

        self.selected_tab = tk.IntVar()
        self.selected_tab.set(0)
        self.show_tab(self.selected_tab.get())

        self.root.mainloop()

    def show_tab(self, tab_id):
        handle_tab_view(tab_id, self.tab_frames)
        for tab_frame_id, frame in self.tab_frames.items():
            if tab_frame_id == tab_id:
                frame.place(relx=0,rely=0,relwidth=1,relheight=1)
                frame.lift()
                print(f"Tab {tab_id} clicked")
            else:
                frame.pack_forget()
            self.selected_tab.set(tab_id)

    def create_tab(self, name, tab_id):
        self.tab_frame = tk.Frame(self.root)
        self.tab_frames[tab_id] = self.tab_frame

        self.tab_menu.add_command(label=name, command=lambda: self.show_tab(tab_id))

    def add_tab(self, name):
        self.new_tab_id = len(self.tab_frames)
        self.create_tab(name, self.new_tab_id)

    def get_tab_frames(self):
        return self.tab_frames
    