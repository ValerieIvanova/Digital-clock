from tkinter import Label, Tk
from time import strftime

window = Tk()
window.title('Digital Clock')
window.geometry('300x90')
window.configure(background='black')


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = Label(window, font='ds-digital 80', background="black", foreground='light green')
label.pack(anchor='center')

time()
window.mainloop()