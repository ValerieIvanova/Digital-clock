from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
root.geometry('300x90')


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


# Problem with the background color
label = Label(root, font='ds-digital 80', background='black', foreground='pink')
label.pack(anchor='center')
time()

mainloop()
