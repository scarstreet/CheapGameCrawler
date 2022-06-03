import crawler as cr
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

'''======================================================
A class to define the scrollable frame
when displaying the search results on the app
======================================================'''
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

'''======================================================
Some runtime functions that are activated
when the search button is pressed
======================================================'''

# Creating the UI for displaying each data
def changeContent(data):
    global content_frame
    global allImg
    content_frame.destroy()
    content_frame = ScrollableFrame(root)
    allImg = []
    for d in data:
        if(len(data[d])!=0):
            data_frame = tk.Frame(content_frame.scrollable_frame)
            title = tk.Label(data_frame,text=d,font=("Impact", 18),bg="#e3631e",fg="#ffffff")
            title.pack(side="top",fill="x")
            for idx,row in enumerate(data[d].to_dict('records')):
                color = "#e5e5e5" if idx%2 == 0 else "#d4d4d4"
                info_frame = tk.Label(data_frame,bg=color)
                print(row)
                try:
                    allImg.append('.')
                    allImg[-1] = Image.open(row['imgPath'])
                    w,h = allImg[-1].size
                    if h >= 50:
                        ratio = h//50
                        print(allImg[-1].size,(w//ratio,h//ratio))
                        allImg[-1] = allImg[-1].resize((w//ratio,h//ratio),Image.ANTIALIAS)
                    allImg[-1] = ImageTk.PhotoImage(allImg[-1])
                    tk.Label(info_frame,image=allImg[-1]).pack(side="left")
                except:
                    tk.Label(info_frame,bg="#ffffff",text="ImageError!",width=10,height=5,anchor="center").pack(side="left")
                tk.Label(info_frame,text=row['title'],font=("Helvatica", 12),bg=color).pack(side="left", expand=True, fill='x')
                tk.Label(info_frame,text=f"NT$ {row['price']}",font=("Impact", 14),bg=color).pack(side="right")
                info_frame.pack(side="top", fill='x', expand=True)
            data_frame.pack(side="top", fill='x')
    content_frame.pack(expand=True, fill="both",side="bottom",anchor="center")

# Start searching the results by connecting to the
# crawler file. After obtaining results, call the
# above function
def startSearch():
    all = cr.search(search.get())
    changeContent(all)



'''======================================================
GUI setup for the app's general information
======================================================'''
global root
root = tk.Tk()
root.title("Crawly Boi")

window_width = 900
window_height = root.winfo_screenheight() - 80

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2) - 40

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

'''======================================================
GUI setup for the app's contents
======================================================'''

allImg = []

mainTitle = tk.Label(root, text="CRAWLY BOI",font=("Impact", 30))
mainTitle.pack(fill='x', side="top")
desc = tk.Label(root, text="a webcrawler to look for cheap games from websites",font=("Helvatica", 12), fg="#cf4800")
desc.pack(fill='x', side="top")

global search
searchFrame = ttk.Frame(root)
searchFrame.pack(fill='x')

search = tk.StringVar()
search_entry = ttk.Entry(searchFrame, textvariable=search)
search_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=10,pady=20)

button = ttk.Button(searchFrame, text='Search', command=startSearch)
button.pack(side=tk.LEFT, padx=10,pady=20)

global content_frame
content_frame = tk.Frame(root)
placeholdr = tk.Label(content_frame,text="Note : This app takes a while to load.\nPlease don't close the chrome tab during it's loading process",bg="#d4d4d4",fg="#999999")
placeholdr.pack(expand=True, fill="both",side="bottom")
content_frame.pack(expand=True, fill="both",side="bottom")

'''======================================================
Starting the app
======================================================'''
root.mainloop()