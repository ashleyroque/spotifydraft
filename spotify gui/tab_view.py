import tkinter as tk

def handle_tab_view(tab_index, tab_frames):
    tab_color(tab_index, tab_frames)
    tab_label(tab_index, tab_frames)




def tab_color(tab_index, tab_frames):
    tab_colors = {0: "red", 1: "green", 2: "blue"}  # Define tab colors
    for tab_frame_id, frame in tab_frames.items():
        color = tab_colors.get(tab_frame_id, "white")  # Get color for the tab index or default to white
        frame.config(bg=color)


def tab_label(tab_index, tab_frames):
   tab_labels = {0: "Hello", 1: "Let's die", 2: "green"}
   for tab_frame_id, frame in tab_frames.items():

        label_text = tab_labels.get(tab_frame_id, "white")
        label = tk.Label(frame, text=label_text, font=('Ms Sans Serif', 24))
        label.pack(padx=10,pady=10)