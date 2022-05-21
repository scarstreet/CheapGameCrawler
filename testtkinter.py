import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Crawley Boi")

window_width = 900
window_height = root.winfo_screenheight()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

# TODO - get an icon!!
# root.iconbitmap('./assets/pythontutorial.ico')
# SETUP^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FUNCTIONS vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def button_clicked():
    print(search.get())

# GUI vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

mainTitle = tk.Label(root, text="CRAWLY BOI",font=("Impact", 30))
mainTitle.pack(fill='x', side="top")
desc = tk.Label(root, text="a webcrawler to look for cheap games from websites",font=("Helvatica", 12))
desc.pack(fill='x', side="top")

global search
searchFrame = ttk.Frame(root)
searchFrame.pack(fill='x')

search = tk.StringVar()
search_entry = ttk.Entry(searchFrame, textvariable=search)
search_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=10,pady=20)

button = ttk.Button(searchFrame, text='Search', command=button_clicked)
button.pack(side=tk.LEFT, padx=10,pady=20)

frame = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)
frame.pack(expand=True, fill="both",side="bottom")

# RUN vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
root.mainloop()