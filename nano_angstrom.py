##!/usr/bin/python3.5

#Copyright 2018 Błażej Twardy
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import os


def info_button():
    messagebox.showinfo('Author', ' Author: Błażej Twardy \n')


def close_window():
    window.destroy()
    exit()


def opener(box, b='dat'):
    path = os.getcwd()
    a = filedialog.askopenfilename(initialdir=path, title="Select file",
                                   filetypes=((str(b) + " files", "*." + str(b)), ("all files", "*.*")))
    box.delete(0, tkinter.END)
    box.insert(0, str(a))
    return a


def ten_buton():
    messagebox.showerror('Error', 'Jeszcze nie działa :(')


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def convert(box, a=1):
    try:
        entry_box = box.get()
        data = np.genfromtxt(entry_box)
        x = data[:, 0]
        y = data[:, 1]
        dl = len(x)
        try:
            err = data[:, 2]
        except IndexError:
            err = np.zeros(dl)
        dlug = len(entry_box.split('/'))
        nametemp = entry_box.split('/')[dlug - 1]
        name = nametemp.split('.')[0]
        if a == 1:
            x1 = x / 10
            touch(name + '.txt')
            f = open(name + '.txt', 'a')
            f.write('waveobs flux err \n')
            for i in range(0, dl):
                f.write(str(x1[i]) + ' ' + str(y[i]) + ' ' + str(err[i]) + '\n')
            f.close()
        else:
            x1 = x * 10
            touch(name + '.dat')
            f = open(name + '.dat', 'a')
            for i in range(1, dl):
                f.write(str(x1[i]) + ' ' + str(y[i]) + '\n')
            f.close()
        messagebox.showinfo('Info', 'Done')
        print("Done")
    except OSError:
        messagebox.showerror('Error', 'File Error')
        print("File Error")


window = tkinter.Tk()
window.title('NanoAngstrom Converter 2000 for iSpec')
window.geometry('560x250')
window.resizable(width=False, height=False)

info = tkinter.Button(window, text='Info', command=lambda: info_button())
info.grid(row=0)

l1 = tkinter.Label(window, text='Angstrom => nanometre, File:')
l1.grid(row=1, column=0, padx=10, pady=10)

e1 = tkinter.Entry(window, width=20)
e1.grid(row=1, column=1)

o1 = tkinter.Button(window, text='Open', bg='lime', command=lambda: opener(e1, b='dat'))
o1.grid(row=2, column=0)

con1 = tkinter.Button(window, text='Convert to nano', command=lambda: convert(e1, a=1))
con1.grid(row=1, column=2)

l2 = tkinter.Label(window, text='nanometre => Angstrom, File:')
l2.grid(row=3, column=0, padx=10, pady=10)

e2 = tkinter.Entry(window, width=20)
e2.grid(row=3, column=1)

o2 = tkinter.Button(window, text='Open', bg='lime', command=lambda: opener(e2, b='txt'))
o2.grid(row=4, column=0)

con2 = tkinter.Button(window, text='Convert to Angstrom', command=lambda: convert(e2, a=2))
con2.grid(row=3, column=2)

clos = tkinter.Button(window, text='EXIT', bg="red", command=lambda: close_window())
clos.grid(column=2)

window.mainloop()

