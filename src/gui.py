import os
from tkinter import *
from tkinter import filedialog as fd, messagebox
from PIL import Image, ImageTk
from os.path import relpath


def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window = Tk()
window.protocol("WM_DELETE_WINDOW", on_close)
window.geometry('500x700')
window.title()

path = '../images/logo-upb.jpg'
logo_upb = ImageTk.PhotoImage(Image.open(path))
path = '../images/logo-acs.png'
logo_acs = ImageTk.PhotoImage(Image.open(path))
header = Canvas(window, height=120, width=500)
header.pack(side=TOP)
header.create_image(10, 10, anchor=NW, image=logo_upb)
header.create_image(480, 10, anchor=NE, image=logo_acs)


def select_file():
    file_types = (
        ('jpeg', '*.jpg'),
        ('png', '*.png'),
        ('All files', '*.*')
    )
    get_file = fd.askopenfilename(filetypes=file_types)
    if get_file:
        entry_upl.delete(0, END)
        entry_upl.insert(0, get_file)
        set_image()


def set_image(event='<Return>'):
    path = relpath(entry_upl.get(), os.getcwd())
    print(path)
    image = ImageTk.PhotoImage(Image.open(path))
    try:
        res.destroy()
    except NameError:
        res = None
    res = Label(window, image=image)
    res.place(x=250, y=350, anchor=N)
    window.mainloop()


label_upl = Label(window, text="Upload file:")
label_upl.place(x=20, y=200)
entry_upl = Entry(window, width=50)
entry_upl.bind('<Return>', set_image)
entry_upl.place(x=90, y=200)
btn_upl = Button(window, text="...", command=select_file)
btn_upl.place(x=400, y=200)

btn_start = Button(window, text="Start")
btn_start.place(x=250, y=275, anchor=CENTER)

label_count = Label(window, text="Count: 0")
label_count.place(x=20, y=550)
label_exec_time = Label(window, text="Execution time: 0s")
label_exec_time.place(x=20, y=575)
label_acc = Label(window, text="Accuracy: 0%")
label_acc.place(x=20, y=600)

window.mainloop()
