import os
from src.Counter import Counter
from pathlib import Path
from tkinter import *
from tkinter import filedialog as fd, messagebox, ttk
from PIL import Image, ImageTk
from os.path import relpath


def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window = Tk()
window.protocol("WM_DELETE_WINDOW", on_close)
window.geometry('1600x800')
window.title('Aplicație desktop pentru identificarea arborilor dintr-o imagine folosind un clasificator')
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)


def select_file():
    file_types = (
        ('jpeg', '*.jpg'),
        ('png', '*.png'),
        ('All files', '*.*')
    )
    get_file = fd.askopenfilename(filetypes=file_types)
    if get_file:
        try:
            files.delete(files.get_children())
        except:
            pass
        files.insert(parent='', index='end', iid=0, text='',
                     values=(os.path.abspath(get_file).replace('\\', '\\\\')))
        set_image(path=os.path.abspath(get_file))


def select_dir():
    folder = fd.askdirectory()
    file_list = list(Path(folder).glob('*.jpg'))
    btn_next['state'] = 'normal'
    btn_prev['state'] = 'normal'
    try:
        files.delete(files.get_children())
    except:
        pass
    iid = 0
    for file in file_list:
        files.insert(parent='', index='end', iid=iid, text='',
                     values=(str(file).replace('\\', '\\\\')))
        iid += 1
    Counter.reset_counter()
    files.selection_set(files.get_children()[Counter.get_counter()])
    set_image(path=file_list[Counter.get_counter()])


def set_image(path, event='<Return>'):
    image = Image.open(path).resize((640, 480))
    image_tk = ImageTk.PhotoImage(image)
    image_lbl = Label(window, image=image_tk)
    image_lbl.grid(row=0, column=1, columnspan=2, rowspan=6)
    window.mainloop()


def next_image():
    Counter.count_up()
    cur_iid = Counter.get_counter()
    sel_item = files.get_children()[cur_iid]
    files.selection_set(sel_item)
    path = files.item(sel_item)['values'][0]
    set_image(path=path)


def prev_image():
    if Counter.get_counter() > 0:
        Counter.count_down()
    cur_iid = Counter.get_counter()
    sel_item = files.get_children()[cur_iid]
    files.selection_set(sel_item)
    path = files.item(sel_item)['values'][0]
    set_image(path=path)


def start_detect():
    im = Image.open('../exemplu_22.jpg')
    im.show()


image_upl_one = ImageTk.PhotoImage(Image.open("../images/file.png"))
btn_upl_one = Button(window, text="Choose file", image=image_upl_one, compound="top", command=select_file)
btn_upl_one.grid(row=0, rowspan=2, padx=15, pady=5)

image_upl_dir = ImageTk.PhotoImage(Image.open("../images/folder.png"))
btn_upl_dir = Button(window, text="Choose directory", image=image_upl_dir, compound="top", command=select_dir)
btn_upl_dir.grid(row=2, rowspan=2, padx=15, pady=5)

image_next = ImageTk.PhotoImage(Image.open("../images/next.png"))
btn_next = Button(window, text="Next image", image=image_next, compound="top", command=next_image)
btn_next['state'] = 'disabled'
btn_next.grid(row=4, rowspan=2, padx=15, pady=5)

image_prev = ImageTk.PhotoImage(Image.open("../images/prev.png"))
btn_prev = Button(window, text="Previous image", image=image_prev, compound="top", command=prev_image)
btn_prev['state'] = 'disabled'
btn_prev.grid(row=6, rowspan=2, padx=15, pady=5)

btn_start = Button(window, text="Start", command=start_detect)
btn_start.grid(row=6, column=1, columnspan=2)

label_count = Label(window, text="Count: 0")
label_count.grid(row=0, column=3)
label_exec_time = Label(window, text="Execution time: 0s")
label_exec_time.grid(row=1, column=3, padx=15)

table_frame = Frame(window)
table_frame.grid(row=2, column=3, rowspan=4, padx=0)

files_scroll = Scrollbar(table_frame)
files_scroll.pack(side=RIGHT, fill=Y)

files = ttk.Treeview(table_frame, yscrollcommand=files_scroll.set, height=20)
files['columns'] = ('file_path')
files.column('#0', width=0, stretch=NO)
files.column('file_path', width=500)
files.heading('#0', text='', anchor=CENTER)
files.heading('file_path', text='File Path', anchor=CENTER)
files.pack()

window.mainloop()
