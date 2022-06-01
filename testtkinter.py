import tkinter as tk
from tkinter import ttk
import crawler as cr
from PIL import ImageTk, Image

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

global root
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

def changeContent(data):
    global content_frame
    content_frame.destroy()
    content_frame = ScrollableFrame(root)
    for d in data:
        if(len(data[d])!=0):
            data_frame = tk.Frame(content_frame.scrollable_frame)
            title = tk.Label(data_frame,text=d)
            title.pack(side="top",fill="x")
            for idx,row in enumerate(data[d].to_dict('records')):
                # while(True):
                try:
                    info_frame = tk.Label(data_frame,bg="#0000ff")
                    print(row)
                    image = ImageTk.PhotoImage(Image.open(row['imgPath']))
                    canv = tk.Canvas(info_frame,width=100, height=100)
                    canv.pack(side="left")
                    color = "#ff0000" if idx%2 == 0 else "#00ff00"
                    canv.create_image(20,20,image=image)
                    tk.Label(info_frame,text=row['title'],bg=color).pack(side="left")
                    tk.Label(info_frame,text=f"NT$ {row['price']}",bg=color).pack(side="right")
                    info_frame.pack(side="top", fill='x')
                except Exception as e:
                    print(e)
            # ttk.Separator(data_frame,orient="horizontal").pack()
            data_frame.pack()
    # placeholdr = tk.Label(text="I tried", bg="#b3b3b3")
    # placeholdr.pack(expand=True, fill="both",side="bottom")
    content_frame.pack(expand=True, fill="both",side="bottom")

def button_clicked():
    all = cr.search(search.get())
    changeContent(all)
    print(all)

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

global content_frame
content_frame = tk.Frame(root)
placeholdr = tk.Label(content_frame,text="Temp text",bg="#b3b3b3")
placeholdr.pack(expand=True, fill="both",side="bottom")
content_frame.pack(expand=True, fill="both",side="bottom")

# RUN vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
root.mainloop()